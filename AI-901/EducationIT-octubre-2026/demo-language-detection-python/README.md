# Demo: detección de idioma con Azure AI Language

En esta práctica ejecutarás una aplicación web local. Escribirás un texto en el navegador y Azure AI Language devolverá el idioma, el código ISO 639-1 y la confianza de detección.

## Requisitos

- Python 3.10 o posterior
- Visual Studio Code
- Recurso Azure AI Language ya creado
- Endpoint y clave del recurso

## Preparar el entorno

Abre PowerShell en esta carpeta y ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell no permite activar el entorno, revisa el mensaje con el instructor.

## Configurar Azure

Crea el archivo local `.env` a partir del ejemplo:

```powershell
Copy-Item .env.example .env
notepad .env
```

Completa los datos del recurso Language:

```dotenv
LANGUAGE_ENDPOINT=https://TU-RECURSO.cognitiveservices.azure.com/
LANGUAGE_KEY=TU_CLAVE
```

Guarda el archivo. No compartas la clave ni subas el archivo `.env` al repositorio. El archivo está excluido por `.gitignore`.

## Ejecutar la demo web

Inicia el servidor:

```powershell
python web_app.py
```

Abre en el navegador:

```text
http://127.0.0.1:5000
```

Escribe una frase en el cuadro y pulsa **Detectar idioma**. Prueba español, inglés y francés para comparar resultados. Para detener el servidor, vuelve a PowerShell y presiona **Ctrl + C**.

## Qué ocurre detrás de la página

1. El navegador envía el texto a la ruta local `/detect`.
2. Flask recibe la solicitud y crea el cliente del SDK.
3. El SDK llama a Azure AI Language usando el endpoint y la clave del archivo local `.env`.
4. La página muestra idioma, código ISO y confianza.

## Demo de consola opcional

El archivo `app.py` ejecuta ejemplos de texto predefinidos:

```powershell
python app.py
```

## Seguridad y costo

Usa textos de prueba, no datos personales. Cada análisis se envía al servicio Azure y puede generar consumo según el nivel de precios del recurso. No publiques la clave; si se expone, rótala desde Azure.
