# Receipt Lens — demo OCR y extracción

Aplicación Flask para demostrar dos etapas: OCR con Azure Computer Vision (Read) y extracción didáctica de campos de recibo mediante patrones.

> La extracción de campos es demostrativa y puede equivocarse. No se usa una API de Document Intelligence en esta versión.

## Requisitos

- Python 3.10 o superior
- Recurso Azure Computer Vision con endpoint y clave
- Conectividad a Azure desde el equipo

## Ejecutar en Windows PowerShell

```powershell
cd ruta\a\receipt-lens
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
python app.py
```

En `.env`, pega el endpoint mostrado en Overview y una clave de **Keys and Endpoint**. No pegues la clave en el código, GitHub, capturas o chats. Luego abre `http://127.0.0.1:5000`.

## API utilizada

`POST {endpoint}/computervision/imageanalysis:analyze?api-version=2024-02-01&features=read`

El endpoint procesa la imagen y devuelve líneas detectadas. El navegador no recibe ni conoce la clave: la llamada se hace desde Flask.
