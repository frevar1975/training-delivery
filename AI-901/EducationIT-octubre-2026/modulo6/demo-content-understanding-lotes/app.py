import io
import os
import zipfile
from datetime import datetime, timezone

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisResult
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, send_file

load_dotenv()
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

ENDPOINT = os.getenv("AZURE_CONTENT_UNDERSTANDING_ENDPOINT", "").strip()
KEY = os.getenv("AZURE_CONTENT_UNDERSTANDING_KEY", "").strip()
API_VERSION = os.getenv("AZURE_CONTENT_UNDERSTANDING_API_VERSION", "2025-11-01")
ANALYZERS = {
    "read": ("prebuilt-read", "Lectura de texto"),
    "layout": ("prebuilt-layout", "Estructura y tablas"),
    "receipt": ("prebuilt-receipt", "Recibos"),
}
ALLOWED_TYPES = {
    ".pdf": {"application/pdf"}, ".jpg": {"image/jpeg"}, ".jpeg": {"image/jpeg"},
    ".png": {"image/png"}, ".webp": {"image/webp"}, ".bmp": {"image/bmp"},
}
MAX_FILE_BYTES = 20 * 1024 * 1024
MAX_FILES = 10


def get_content_type(filename, mimetype):
    extension = os.path.splitext(filename.lower())[1]
    if extension not in ALLOWED_TYPES or mimetype not in ALLOWED_TYPES[extension]:
        raise ValueError("Formato no compatible. Usa PDF, JPG, PNG, WEBP o BMP.")
    return mimetype


def analyze_bytes(data, content_type, analyzer_id):
    if not ENDPOINT:
        raise ValueError("Configura AZURE_CONTENT_UNDERSTANDING_ENDPOINT en .env.")
    credential = AzureKeyCredential(KEY) if KEY else None
    if credential is None:
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
    client = ContentUnderstandingClient(endpoint=ENDPOINT, credential=credential, api_version=API_VERSION)
    try:
        poller = client.begin_analyze_binary(analyzer_id=analyzer_id, binary_input=data, content_type=content_type)
        result: AnalysisResult = poller.result()
        return result.as_dict()
    finally:
        client.close()


@app.get("/")
def index():
    return render_template("index.html", configured=bool(ENDPOINT), max_files=MAX_FILES)


@app.get("/samples")
def samples():
    """Genera tres documentos PDF ficticios y los entrega en un ZIP."""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
    except ImportError:
        return jsonify(error="Instala reportlab con: pip install -r requirements.txt"), 500

    examples = [
        ("01_factura_ficticia.pdf", "FACTURA DE EJEMPLO", [
            "Comercial Andina Demo", "NIT: 1020304012", "Factura: F-2026-00418",
            "Fecha: 03/11/2026", "Cliente: Martina Rojas (dato ficticio)",
            "Detalle: Servicio de mantenimiento preventivo", "Cantidad: 1",
            "Subtotal: Bs 480,00", "IVA: Bs 62,40", "TOTAL: Bs 542,40",
            "Documento ficticio creado solo para capacitación.",
        ]),
        ("02_recibo_ficticio.pdf", "RECIBO DE EJEMPLO", [
            "Cafetería La Esquina Demo", "Recibo: R-00871", "Fecha: 02/11/2026 16:42",
            "1 x Café americano                 Bs 18,00", "2 x Empanada                       Bs 30,00",
            "1 x Jugo natural                    Bs 16,00", "TOTAL                              Bs 64,00",
            "Pago: Tarjeta", "Documento ficticio creado solo para capacitación.",
        ]),
        ("03_formulario_cita_ficticio.pdf", "FORMULARIO DE CITA (FICTICIO)", [
            "Centro de Atención Demo", "Paciente: Camila Ejemplo", "Fecha de cita: 12/11/2026",
            "Hora: 10:30", "Servicio: Consulta general", "Indicaciones: Llegar 15 minutos antes.",
            "Dato de contacto: 700 000 001 (ficticio)", "No contiene información de una persona real.",
        ]),
    ]
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for filename, title, lines in examples:
            pdf = io.BytesIO()
            page = canvas.Canvas(pdf, pagesize=A4)
            page.setTitle(title)
            page.setFont("Helvetica-Bold", 17)
            page.drawString(54, 790, title)
            page.setFont("Helvetica", 11)
            y = 745
            for line in lines:
                page.drawString(54, y, line)
                y -= 29
            page.setFont("Helvetica-Oblique", 9)
            page.drawString(54, 55, "Material ficticio generado para una demostración educativa.")
            page.save()
            zf.writestr(filename, pdf.getvalue())
    archive.seek(0)
    return send_file(archive, mimetype="application/zip", as_attachment=True,
                     download_name="ejemplos_ai901_documentos.zip")


@app.post("/analyze")
def analyze():
    uploads = [item for item in request.files.getlist("files") if item and item.filename]
    mode = request.form.get("mode", "read")
    if mode not in ANALYZERS:
        return jsonify(error="Selecciona un analizador válido."), 400
    if not uploads:
        return jsonify(error="Selecciona al menos un archivo."), 400
    if len(uploads) > MAX_FILES:
        return jsonify(error=f"El máximo es {MAX_FILES} archivos por lote."), 400

    analyzer_id, analyzer_label = ANALYZERS[mode]
    results = []
    for upload in uploads:
        try:
            content_type = get_content_type(upload.filename, upload.mimetype)
            raw = upload.read(MAX_FILE_BYTES + 1)
            if len(raw) > MAX_FILE_BYTES:
                raise ValueError("El archivo supera el límite de 20 MB.")
            if not raw:
                raise ValueError("El archivo está vacío.")
            result = analyze_bytes(raw, content_type, analyzer_id)
            results.append({"filename": upload.filename, "ok": True, "result": result})
        except (AzureError, ValueError, OSError) as exc:
            results.append({"filename": upload.filename, "ok": False, "error": str(exc)})
        except Exception as exc:
            results.append({"filename": upload.filename, "ok": False,
                            "error": f"No se pudo analizar: {exc}"})
    return jsonify(analyzer=analyzer_label, processed_at=datetime.now(timezone.utc).isoformat(),
                   total=len(results), succeeded=sum(x["ok"] for x in results),
                   failed=sum(not x["ok"] for x in results), results=results)


@app.errorhandler(413)
def too_large(_error):
    return jsonify(error="El lote supera el máximo total permitido de 100 MB."), 413


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=False)
