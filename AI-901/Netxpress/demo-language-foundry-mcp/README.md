# Demo: Azure Language en un agente de Foundry con MCP

## Objetivo

Conectar un agente de Azure AI Foundry a una herramienta MCP de Azure Language y usarla para extraer entidades nombradas de un texto. El agente solicita autorización para ejecutar la herramienta y luego presenta los resultados.

Esta demo es independiente de la aplicación Flask de detección de idioma y reconocimiento de entidades.

## Arquitectura

- **Agente:** Azure AI Foundry Agent Service.
- **Herramienta:** servidor MCP de Azure Language (Foundry Tools).
- **Operación demostrada:** extracción de entidades nombradas.
- **Autorización:** el agente pide aprobación antes de invocar la herramienta, según la configuración seleccionada.

## Requisitos

- Suscripción y proyecto de Azure AI Foundry.
- Un agente con un modelo desplegado y acceso al área de juegos.
- Recurso de Azure AI Language / Foundry Tools y permisos para conectarlo.
- Acceso a la herramienta MCP de Azure Language desde Foundry.

> La disponibilidad de conectores MCP y las opciones de autenticación dependen de la configuración del tenant y del proyecto. Usa las opciones que aparezcan en tu entorno de Foundry.

## Configurar el agente

1. Abre el proyecto en Azure AI Foundry y crea o selecciona un agente.
2. Agrega instrucciones como estas:

   ```text
   You are a text analysis agent. Use the Azure Language tool to analyze text.
   When the user asks to extract entities, call the Azure Language tool.
   Report each entity with its category. If no entities are found, say so clearly.
   Do not invent entities that are not present in the tool results.
   ```

3. En **Tools / Herramientas**, agrega el servidor MCP de Azure Language (Foundry Tools).
4. Configura el recurso y la autenticación solicitada por Foundry. No pegues claves en el chat ni las guardes en este repositorio.
5. Guarda el agente y abre el área de juegos.

## Ejecutar la demo

Envía esta solicitud:

```text
Extract named entities in this text:
"Alex and I attended a Microsoft AI conference. It was in Las Vegas on September 21st."
```

6. Cuando Foundry solicite autorización para llamar a la herramienta, aprueba la llamada.
7. Comprueba que la respuesta enumere las entidades devueltas por Azure Language, por ejemplo persona, evento, ubicación y fecha. El resultado exacto puede variar.

## Qué observar

- El agente decide que necesita una herramienta para realizar el análisis.
- MCP conecta Foundry con Azure Language.
- La autorización controla si se ejecuta la llamada.
- La respuesta del agente debe estar fundamentada en el resultado de la herramienta.

## Modos de aprobación

Foundry puede ofrecer opciones similares a estas, según la versión y la configuración:

- **Una sola vez:** autoriza esta llamada únicamente.
- **Siempre para esta herramienta:** autoriza futuras llamadas a esta herramienta.
- **Siempre para todas las herramientas:** autoriza llamadas a todas las herramientas conectadas.

Para una demostración en clase, empieza con autorización de una sola vez y explica el alcance antes de elegir una opción persistente.

## Diferencia frente a la demo Python

La demo Flask llama directamente al SDK de Azure AI Language desde código Python y sirve para analizar texto desde una página local. Esta versión usa un agente en Foundry, conectado a una herramienta MCP; el agente decide cuándo llamar a la herramienta y presenta el resultado en el chat.

## Seguridad

- No publiques claves, cadenas de conexión ni tokens.
- Usa texto ficticio en las pruebas.
- Revisa el alcance de cada autorización antes de aprobarla.
- La autorización de una herramienta no debe confundirse con la autorización de todas las herramientas.

## Referencias

- [Azure AI Foundry](https://ai.azure.com/)
- [Azure AI Language](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
