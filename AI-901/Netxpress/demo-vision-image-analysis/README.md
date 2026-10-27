# Demo AI-901: análisis de imágenes con Azure AI Vision

Copia del laboratorio de Vision Lab para la entrega Netxpress. La plantilla reutilizable está en [demos/vision-lab](../../../../demos/vision-lab).

La aplicación Flask permite subir una imagen y muestra una descripción, objetos detectados y etiquetas visuales con Azure AI Vision Image Analysis.

## Preparar en Windows PowerShell

Desde la carpeta de este demo:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Completa `.env` con el endpoint y la clave de tu recurso Azure AI Vision. Obtén ambos en Azure Portal, en el recurso de Vision, sección **Keys and Endpoint**. No publiques el archivo `.env`.

```powershell
py app.py
```

Abre [http://127.0.0.1:5000](http://127.0.0.1:5000), carga una imagen JPG, PNG, WEBP o BMP (máximo 20 MB) y pulsa **Analizar imagen**. Detén el servidor con **Ctrl+C**.

## Requisitos y notas

- Python 3.10 o posterior y un recurso Azure AI Vision activo.
- La función Caption depende de que la región del recurso la admita.
- La clave se mantiene en el servidor local; la imagen se envía a Azure para el análisis.
- `.env`, `.venv/` y `__pycache__/` están excluidos de Git.
- No subir claves ni imágenes con datos sensibles.

## Archivos

- `app.py`: backend Flask y llamada a Azure AI Vision.
- `templates/index.html`: interfaz para cargar y analizar imágenes.
- `.env.example`: variables de configuración de ejemplo.
- `requirements.txt`: dependencias Python.
