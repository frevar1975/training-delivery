# Demo — Agente de Microsoft Foundry

Aplicación Flask de chat que envía mensajes a un agente de Microsoft Foundry y muestra las respuestas. El código utiliza `agent_reference`.

## Requisitos

- Python instalado.
- Azure CLI.
- Acceso a un proyecto de Microsoft Foundry y a un agente.
- Permisos para ejecutar el agente en ese proyecto.

## Clonar el repositorio del delivery

En PowerShell:

```powershell
cd C:\clases
git clone https://github.com/frevar1975/training-delivery.git
cd .\training-delivery\AI-901\Netxpress\demo-nuevo-agente\ai-900-demo
```

Si ya clonaste el repositorio:

```powershell
cd C:\clases\training-delivery\AI-901\Netxpress\demo-nuevo-agente\ai-900-demo
```

## Crear el entorno e instalar dependencias

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Si PowerShell bloquea la activación:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Configurar el proyecto y el agente

Copia el archivo de ejemplo y edítalo:

```powershell
Copy-Item .env.example .env
notepad .env
```

Completa `.env` con los datos del proyecto y el agente al que tienes acceso:

```env
FOUNDRY_PROJECT_ENDPOINT=https://<tu-proyecto>.services.ai.azure.com/api/projects/<nombre-proyecto>
FOUNDRY_AGENT_NAME=<nombre-exacto-del-agente>
```

Inicia sesión con la cuenta que tiene acceso:

```powershell
az login
az account show
```

El archivo `.env` contiene configuración local. No lo subas a GitHub.

## Ejecutar y probar

```powershell
python app.py
```

Abre en el navegador:

```text
http://127.0.0.1:5000
```

Escribe un mensaje y compara la respuesta con las instrucciones del agente en Foundry.

## Archivos

- `app.py`: servidor Flask y llamada al agente.
- `templates/index.html`: interfaz de chat.
- `static/styles.css`: estilos.
- `requirements.txt`: dependencias.
- `.env.example`: formato de configuración sin valores de acceso.
- `.gitignore`: excluye `.env`, el entorno virtual y cachés.

## Solución rápida

- **Error de autenticación:** ejecuta `az login` y confirma la cuenta con `az account show`.
- **Endpoint o agente no válido:** revisa el endpoint, el nombre exacto del agente y que la cuenta tenga acceso al proyecto.
- **Dependencias no encontradas:** confirma que `.venv` está activo y vuelve a ejecutar `pip install -r requirements.txt`.
- **El puerto está ocupado:** cierra otra instancia del demo o libera el puerto 5000.
