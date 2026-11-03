"""Demo educativo: audio/texto -> agente Foundry -> caso de atención."""
import asyncio
import json
import os
import re
import subprocess
import tempfile
import threading
from pathlib import Path
from typing import Annotated

from dotenv import load_dotenv
from flask import Flask, render_template, request
from pydantic import Field
from werkzeug.utils import secure_filename

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "demo-local")
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

ALLOWED_EXTENSIONS = {"wav", "mp3", "m4a", "mp4", "ogg", "webm", "flac"}
SAMPLE_TRANSCRIPT = (
    "Hola, señora Camila. Le llamo de la Clínica San Gabriel para confirmar "
    "su cita de mañana a las diez y media. Por favor, llegue quince minutos antes."
)
LANGUAGES = {
    "es-BO": "Español (Bolivia)",
    "es-ES": "Español (España)",
    "es-MX": "Español (México)",
    "en-US": "English (United States)",
}
AGENT_INSTRUCTIONS = """Eres el agente de atención de DemoTel, un caso educativo con datos completamente ficticios.
Analiza la transcripción de una llamada. Identifica motivo, resumen, prioridad (baja, normal, alta),
cliente y datos explícitos. No inventes datos faltantes. Si menciona a Camila o una cita, llama
a consultar_registro con tipo='cita' e identificador='Camila'. Si menciona el pedido B4829,
llama con tipo='pedido' e identificador='B4829'. Basa la respuesta en el resultado de la herramienta.
Devuelve únicamente un objeto JSON válido con estas claves:
motivo, resumen, prioridad, cliente, datos_extraidos (objeto), consulta_encontrada (objeto o null),
respuesta_sugerida, requiere_revision (boolean). No confirmes acciones que no se hayan realizado.
Los registros son ficticios y solo sirven para la demostración."""


def transcribe_audio(audio_path: str, language: str) -> str:
    """Transcribe todos los segmentos de un archivo de audio con Azure Speech."""
    import azure.cognitiveservices.speech as speechsdk

    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ["SPEECH_KEY"],
        region=os.environ["SPEECH_REGION"],
    )
    speech_config.speech_recognition_language = language
    audio_config = speechsdk.audio.AudioConfig(filename=audio_path)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    finished = threading.Event()
    segments = []
    errors = []

    def on_recognized(event):
        if event.result.reason == speechsdk.ResultReason.RecognizedSpeech and event.result.text:
            segments.append(event.result.text.strip())

    def on_canceled(event):
        details = event.result.cancellation_details
        errors.append(details.error_details if details else "Reconocimiento cancelado.")
        finished.set()

    recognizer.recognized.connect(on_recognized)
    recognizer.canceled.connect(on_canceled)
    recognizer.session_stopped.connect(lambda _event: finished.set())
    recognizer.start_continuous_recognition_async().get()
    try:
        if not finished.wait(timeout=90):
            raise RuntimeError("La transcripción tardó más de 90 segundos. Prueba con un audio más corto.")
    finally:
        try:
            recognizer.stop_continuous_recognition_async().get()
        except Exception:
            pass
    if errors:
        raise RuntimeError("Azure Speech no pudo completar la transcripción: " + errors[0])
    return " ".join(segments)


def normalize_audio(source: str, destination: str) -> None:
    try:
        result = subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", source, "-ac", "1", "-ar", "16000",
             "-c:a", "pcm_s16le", destination],
            capture_output=True, text=True, timeout=90, check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("No encuentro ffmpeg. Instálalo y vuelve a abrir PowerShell.") from exc
    if result.returncode:
        raise RuntimeError("No pude convertir el audio. Revisa que se reproduzca correctamente.")


def run_agent(transcript: str):
    """Run a Foundry model agent with a local Python function tool."""
    from agent_framework import Agent, tool
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT", "").strip()
    model = os.getenv("FOUNDRY_MODEL", "").strip()
    if not endpoint or not model:
        raise RuntimeError("Configura FOUNDRY_PROJECT_ENDPOINT y FOUNDRY_MODEL en .env.")

    tool_events = []

    @tool(approval_mode="never_require")
    def consultar_registro(
        tipo: Annotated[str, Field(description="Tipo de registro: cita o pedido.")],
        identificador: Annotated[str, Field(description="Nombre del cliente o código del pedido.")],
    ) -> str:
        """Consulta un registro ficticio de citas o pedidos para esta demo."""
        key = re.sub(r"[^a-z0-9]", "", identificador.casefold())
        if tipo.casefold() == "cita" and key in {"camila", "camilaejemplo", "camilasra"}:
            record = {
                "tipo": "cita",
                "cliente": "Camila (ficticio)",
                "estado": "programada",
                "fecha": "mañana",
                "hora": "10:30",
                "lugar": "Clínica San Gabriel (demo)",
            }
        elif tipo.casefold() == "pedido" and key in {"b4829", "4829"}:
            record = {
                "tipo": "pedido",
                "codigo": "B4829 (ficticio)",
                "estado": "en preparación",
                "actualizacion": "El pedido está en preparación para despacho.",
            }
        else:
            record = {"encontrado": False, "mensaje": "No hay coincidencia en los registros ficticios."}
        tool_events.append({"name": "consultar_registro", "input": {"tipo": tipo, "identificador": identificador}})
        return json.dumps(record, ensure_ascii=False)

    async def ask_agent():
        agent = Agent(
            client=FoundryChatClient(
                project_endpoint=endpoint,
                model=model,
                credential=AzureCliCredential(),
            ),
            name="AgenteAtencionAI901",
            instructions=AGENT_INSTRUCTIONS,
            tools=[consultar_registro],
        )
        return await agent.run("Analiza esta transcripción y prepara el caso:\n\n" + transcript)

    response = asyncio.run(ask_agent())
    output = getattr(response, "text", None) or str(response)
    cleaned = re.sub(r"^\s*```(?:json)?\s*|\s*```\s*$", "", output, flags=re.I)
    try:
        case = json.loads(cleaned)
    except json.JSONDecodeError:
        case = None
    return case, output, tool_events


@app.errorhandler(413)
def too_large(_error):
    return render_template("index.html", error="El archivo supera el límite de 25 MB.", languages=LANGUAGES, sample_transcript=SAMPLE_TRANSCRIPT), 413


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", languages=LANGUAGES, sample_transcript=SAMPLE_TRANSCRIPT)

    language = request.form.get("language", "es-BO")
    if language not in LANGUAGES:
        language = "es-BO"
    transcript = request.form.get("transcript", "").strip()
    audio = request.files.get("audio")
    filename = ""
    try:
        if audio and audio.filename:
            filename = secure_filename(audio.filename)
            suffix = Path(filename).suffix.lower().lstrip(".")
            if suffix not in ALLOWED_EXTENSIONS:
                raise RuntimeError("Formato no admitido. Usa WAV, MP3, M4A, MP4, OGG, WEBM o FLAC.")
            if not os.getenv("SPEECH_KEY") or not os.getenv("SPEECH_REGION"):
                raise RuntimeError("Para transcribir audio, configura SPEECH_KEY y SPEECH_REGION.")
            with tempfile.TemporaryDirectory(prefix="agente-ai901-", ignore_cleanup_errors=True) as workdir:
                original = os.path.join(workdir, filename or "audio." + suffix)
                wav_path = os.path.join(workdir, "audio-normalizado.wav")
                audio.save(original)
                normalize_audio(original, wav_path)
                transcript = transcribe_audio(wav_path, language)
            if not transcript:
                raise RuntimeError("No se detectó voz en el audio. Prueba con una grabación más clara.")
        if not transcript:
            raise RuntimeError("Escribe una transcripción o selecciona un audio.")
        case, agent_text, tool_events = run_agent(transcript)
        return render_template(
            "index.html", languages=LANGUAGES, transcript=transcript, filename=filename,
            language=language, case=case, agent_text=agent_text, tool_events=tool_events,
            sample_transcript=SAMPLE_TRANSCRIPT,
        )
    except Exception as exc:
        app.logger.exception("Atención agent demo failed")
        return render_template(
            "index.html", languages=LANGUAGES, transcript=transcript, filename=filename,
            language=language, error=str(exc), sample_transcript=SAMPLE_TRANSCRIPT,
            case=None, agent_text="", tool_events=[],
        ), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5001")), debug=False)
