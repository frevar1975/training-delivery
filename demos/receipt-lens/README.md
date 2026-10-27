# Receipt Lens — plantilla de demo OCR

Aplicación Flask para explicar dos etapas: OCR con Azure Computer Vision Read y extracción didáctica de campos de recibo mediante patrones.

> La extracción de campos es demostrativa y puede equivocarse. Esta versión no llama a Document Intelligence.

## Requisitos

- Python 3.10 o superior
- Recurso Azure Computer Vision con endpoint y clave
- Conectividad a Azure desde el equipo

## Ejecutar en Windows PowerShell

Desde esta carpeta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Completa `.env` con el endpoint de Azure y una clave local. No pegues la clave en el código, GitHub, capturas o chats. Inicia la app:

```powershell
python app.py
```

Abre http://127.0.0.1:5000. Para detenerla, presiona Ctrl+C en PowerShell.

## API de OCR

`POST {endpoint}/computervision/imageanalysis:analyze?api-version=2024-02-01&features=read`

La llamada se realiza desde Flask y la clave no se envía al navegador.

## Flujo didáctico

1. Carga una imagen JPG, PNG, WEBP o BMP de hasta 10 MB.
2. En modo recibo, revisa tanto los campos tentativos como el texto OCR.
3. En modo imagen general, observa solo el texto detectado.
4. Compara OCR (lectura) con extracción (asignación de significado).

Usa imágenes nítidas y evita datos personales o bancarios reales.
