# Netxpress | Demo web: detección de idioma

Práctica de Azure AI Language con Python. El alumno ingresa un texto desde una página web local y revisa idioma, código ISO 639-1 y nivel de confianza.

## Requisitos

- Python 3.10 o posterior
- Visual Studio Code
- Recurso Azure AI Language activo
- Endpoint y clave del recurso

## Preparación en PowerShell

Abre esta carpeta en VS Code y ejecuta en su terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Crea el archivo local de configuración:

```powershell
Copy-Item .env.example .env
notepad .env
```

Completa las dos variables con los datos del recurso Azure AI Language:

```dotenv
LANGUAGE_ENDPOINT=https://TU-RECURSO.cognitiveservices.azure.com/
LANGUAGE_KEY=TU_CLAVE
```

Guarda el archivo. No compartas la clave ni subas `.env` a GitHub.

## Ejecutar la página web

```powershell
python web_app.py
```

Abre `http://127.0.0.1:5000`, escribe un texto y pulsa **Detectar idioma**. Prueba frases en español, inglés y francés. Para detener el servidor, vuelve a PowerShell y presiona **Ctrl + C**.

## Flujo de la demo

1. El alumno escribe el texto en el navegador.
2. Flask recibe el texto en el endpoint local `/detect`.
3. El SDK envía la solicitud a Azure AI Language usando las credenciales locales.
4. La página muestra el idioma, su código ISO y la confianza.

Para mostrar también la versión por consola, ejecuta `python app.py`.

## Seguridad

- La aplicación escucha solo en `127.0.0.1` (equipo local).
- `.env` está excluido por `.gitignore`; no se incluye ninguna clave en GitHub.
- Usa textos ficticios, nunca información personal.
- Las llamadas al servicio pueden generar consumo según el nivel de precios configurado en Azure.
