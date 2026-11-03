# Demo AI-901: Agente de atención con Microsoft Foundry

El demo convierte una llamada o transcripción en un caso de atención. Muestra dos caminos:

1. **Foundry Portal:** crear un agente Prompt y probarlo en el playground.
2. **Python:** una aplicación Flask transcribe audio con Azure Speech y ejecuta un agente conectado a un modelo del proyecto Foundry. El agente puede invocar la función local `consultar_registro`, que busca citas o pedidos en datos ficticios.

**Flujo:** audio o texto → transcripción → agente → herramienta Python → caso estructurado y respuesta sugerida → simulación de correo. El botón de correo solo muestra una vista previa y confirma una simulación; no envía mensajes reales.

## Requisitos en Azure

- Un proyecto de Microsoft Foundry con un modelo desplegado y acceso de inferencia.
- Azure CLI instalado y autenticado con `az login`.
- Permisos de acceso al proyecto y al deployment para el usuario autenticado.
- Para entrada de audio: un recurso Azure Speech con clave y región.
- FFmpeg instalado y disponible en PATH. En Windows: `winget install --id Gyan.FFmpeg.Essentials -e`, luego reinicia PowerShell.

El texto puede probarse sin configurar Speech ni FFmpeg.

## Parte A — Crear el agente en Foundry Portal

1. Abre el proyecto en Microsoft Foundry.
2. Ve a **Build > Agents** y crea un agente Prompt.
3. Selecciona el deployment de modelo que usarás en el demo.
4. Nombre sugerido: `AgenteAtencionAI901`.
5. Pega estas instrucciones:

```text
Eres el agente de atención de DemoTel, un caso educativo con datos completamente ficticios.
Analiza la transcripción de una llamada. Identifica motivo, resumen, prioridad (baja, normal, alta),
cliente y datos explícitos. No inventes datos faltantes. Si menciona a Camila, considera que la cita
ficticia está programada para mañana a las 10:30 en Clínica San Gabriel. Si menciona el pedido B4829,
indica que el pedido ficticio está en preparación para despacho. Devuelve un objeto JSON válido con:
motivo, resumen, prioridad, cliente, datos_extraidos, consulta_encontrada, respuesta_sugerida y
requiere_revision. No confirmes acciones que no se hayan realizado.
```

6. Abre el playground del agente y prueba con la transcripción de Camila de abajo. Observa cómo el agente mantiene instrucciones y estructura la respuesta.

La versión del portal recibe los registros ficticios en las instrucciones. En la versión Python, el agente consulta esos mismos ejemplos mediante una función que se ejecuta localmente.

## Parte B — Ejecutar desde Python

Desde PowerShell:

```powershell
Set-Location C:\clases\training-delivery\AI-901\EducationIT-octubre-2026\modulo6\demo-agente-atencion-foundry
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Completa `.env` con el endpoint de proyecto, el nombre del deployment, y opcionalmente los valores del recurso Speech:

```text
FOUNDRY_PROJECT_ENDPOINT=https://<recurso>.services.ai.azure.com/api/projects/<proyecto>
FOUNDRY_MODEL=<nombre-del-deployment>
SPEECH_KEY=<clave-del-recurso-Speech>
SPEECH_REGION=<region-del-recurso-Speech>
```

No pegues claves en el código ni las subas a GitHub. En el terminal, inicia sesión:

```powershell
az login
py app.py
```

Abre **http://127.0.0.1:5001**. Puedes pegar una transcripción (sin FFmpeg ni Speech) o cargar audio breve. Para audio, Speech usa reconocimiento continuo y reúne todos los segmentos antes de enviarlos al agente.

## Pruebas de clase

**Cita ficticia:**

```text
Hola, señora Camila. Le llamo de la Clínica San Gabriel para confirmar su cita de mañana a las diez y media. Por favor, llegue quince minutos antes.
```

El agente debe invocar `consultar_registro(tipo="cita", identificador="Camila")` y usar el registro ficticio de la cita. La página muestra la transcripción, el evento de llamada a la herramienta y el caso final.

**Pedido ficticio:**

```text
Buenas tardes. Llamo para consultar el pedido B4829. Todavía no recibí el paquete. ¿Podrían verificar el estado?
```

El agente debe consultar el pedido de ejemplo y proponer una respuesta basada en el estado encontrado.

## Qué mostrar en clase

- Playground de Foundry: agente, modelo, instrucciones y respuestas.
- Aplicación: diferencia entre un chat y un agente que decide llamar una herramienta.
- Botón de correo: vista previa del mensaje sugerido y confirmación de envío simulado, sin conexión SMTP ni envío real.
- Código Python: función local, parámetros que el modelo suministra, resultado que vuelve al modelo y respuesta final.
- Límite de seguridad: los registros son solo datos ficticios; la respuesta sugerida requiere revisión humana.

## Límites

- Demo local educativa, no es un sistema para producción.
- El reconocimiento puede equivocarse; revisa la transcripción.
- Los registros de citas y pedidos viven en memoria en el código y no son una base de datos real.
- La aplicación escucha solo en `127.0.0.1:5001`.
