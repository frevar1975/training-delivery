# Demo AI-901: cargar audio y transcribir con Azure Speech

Copia del laboratorio para la entrega **Netxpress**. La plantilla reutilizable se mantiene en [training-templates/AI-901/demos/speech-audio-upload](https://github.com/frevar1975/training-templates/tree/main/AI-901/demos/speech-audio-upload).

La aplicación permite cargar un audio, normalizarlo con FFmpeg y transcribirlo con Azure Speech SDK. Usa WAV, MP3, M4A, MP4, OGG, WEBM o FLAC; el límite es 25 MB. Para esta demo, utiliza audios breves (menos de 30 segundos).

## Requisitos

- Windows 10/11, Python 3.10 o superior.
- FFmpeg en PATH (winget install Gyan.FFmpeg; luego reinicia PowerShell).
- Un recurso Azure Speech y su clave y región.

## Preparación en PowerShell

```powershell
Set-Location C:\clases
# Si training-delivery ya está clonado, omite el siguiente comando.
git clone https://github.com/frevar1975/training-delivery.git
Set-Location .\training-delivery\AI-901\Netxpress\demo-speech-audio-upload
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Completa .env con la clave y región del recurso Speech (no Azure Language):

```text
SPEECH_KEY=tu_clave
SPEECH_REGION=eastus
FLASK_SECRET_KEY=demo-local
```

Guarda el archivo. No compartas .env ni lo subas a GitHub.

## Generar audios de prueba en español boliviano

Con el entorno virtual activo y .env configurado:

```powershell
py generar_audios_es.py
```

Se crean dos archivos WAV y sus transcripciones: confirmación de cita y consulta por un pedido. El script usa el mismo recurso Azure Speech.

## Iniciar y probar

```powershell
py app.py
```

Abre http://127.0.0.1:5000, selecciona **Español (Bolivia)** y carga uno de los WAV. Detén la app con Ctrl+C.

## Seguridad y notas

- .env, .venv/ y __pycache__/ se excluyen de Git.
- La aplicación solo escucha en 127.0.0.1.
- El audio se procesa con el recurso Azure configurado y el archivo temporal se elimina al completar la solicitud.
- El reconocimiento puede equivocarse con ruido, acentos o nombres propios; revisa la transcripción.
- Esta versión usa recognize_once_async para audios breves.
