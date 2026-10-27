# Foundry Content Understanding — demo local

Aplicación educativa en Flask para cargar un documento o imagen y comparar tres analizadores de Azure Content Understanding: **Read**, **Layout** y **Receipt**. La aplicación usa el SDK oficial de Python y muestra la respuesta JSON completa que reciben las aplicaciones cliente.

## Requisitos

- Python 3.10 o superior
- Un recurso de Content Understanding conectado a un proyecto de Microsoft Foundry
- El endpoint del recurso y, opcionalmente, una clave. También se admite autenticación local mediante `DefaultAzureCredential`.
- Para Receipt, verifica en Foundry que los despliegues/modelos requeridos estén configurados. En el laboratorio guiado, Microsoft recomienda no ejecutar análisis Receipt si no se preparó el modelo; se pueden revisar los resultados precargados en el playground.

## Preparar el proyecto en Foundry

1. Entra a https://ai.azure.com y abre o crea un proyecto.
2. Selecciona una región admitida por Content Understanding y agrega/configura el recurso desde **Build > Services > Content Understanding**.
3. Copia el endpoint del recurso desde su página de configuración. No uses el endpoint de Computer Vision `rsv-vision`: este demo necesita Content Understanding.
4. Si vas a usar clave, guárdala solo en `.env`. Si usarás identidad local, inicia sesión con `az login` y deja vacía la variable de clave.

## Ejecutar en Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
python app.py
```

Abre http://127.0.0.1:5000. Elige un analizador, carga una imagen o PDF y pulsa **Analizar**. Detén el servidor con Ctrl+C.

## Qué demuestra

- **Read**: reconoce texto sin organizarlo por significado.
- **Layout**: extrae texto y estructura del documento, por ejemplo párrafos y tablas.
- **Receipt**: intenta asociar valores del recibo con campos semánticos estructurados.

A diferencia del demo anterior, Receipt usa el analizador prebuilt de Content Understanding, no patrones locales. El servicio procesa el archivo en Azure; usa documentos de prueba sin datos personales o financieros reales.

## API usada

El backend llama a `ContentUnderstandingClient.begin_analyze_binary` con los analizadores `prebuilt-read`, `prebuilt-layout` o `prebuilt-receipt`. La versión de API se configura con `AZURE_CONTENT_UNDERSTANDING_API_VERSION`.
