# DocuLens — portal de análisis de documentos por lote

Demo web Flask para AI-901. Permite cargar documentos individualmente o lotes de hasta 10 archivos y enviarlos a Azure Content Understanding con Read, Layout o Receipt.

## Ejemplos ficticios

Pulsa **Descargar ejemplos ficticios** en el portal. La aplicación genera un ZIP con tres PDF listos para analizar: una factura, un recibo y un formulario de cita. Los datos son inventados para capacitación.

## Preparación en Windows PowerShell

```powershell
cd C:\clases\training-delivery\demos\foundry-batch-document-portal
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

En `.env`, configura el endpoint de Content Understanding. Deja la clave vacía para usar `az login` y `DefaultAzureCredential`, o configura una clave de recurso.

```dotenv
AZURE_CONTENT_UNDERSTANDING_ENDPOINT=https://TU-RECURSO.services.ai.azure.com/
AZURE_CONTENT_UNDERSTANDING_KEY=
AZURE_CONTENT_UNDERSTANDING_API_VERSION=2025-11-01
PORT=5000
```

```powershell
az login
python app.py
```

Abre http://127.0.0.1:5000. Descarga los ejemplos, carga uno para mostrar la modalidad individual o selecciona los tres para procesarlos en lote.

## Guion breve para clase

1. Ejecutar **Read** sobre la factura y observar el texto reconocido.
2. Ejecutar **Layout** sobre la factura y comparar cómo representa estructura y tablas.
3. Ejecutar **Receipt** sobre el recibo y revisar los campos extraídos.
4. Cargar varios documentos a la vez y observar que cada archivo tiene su propio resultado y estado.

## Límites

PDF, JPG, PNG, WEBP o BMP; máximo 10 archivos por lote, 20 MB por archivo y 100 MB en total. Los documentos se envían al endpoint de Azure configurado. Usa únicamente material ficticio. El endpoint, cuotas y analizadores deben estar habilitados en el recurso.

Python 3.10 o superior. Dependencias: `requirements.txt`.
