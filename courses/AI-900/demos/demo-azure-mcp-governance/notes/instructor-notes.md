# Notas del Instructor - Demo Azure MCP Governance

## Curso

AI-900: Microsoft Azure AI Fundamentals

## Tipo de demo

Demo complementaria no oficial del curriculo.

## Proposito

Mostrar como la IA generativa puede conectarse con herramientas reales para consultar recursos, detectar problemas y generar explicaciones utiles para usuarios tecnicos y no tecnicos.

## Conceptos que se refuerzan

- IA generativa
- Copilots
- Agentes
- Uso de herramientas
- Grounding con datos reales
- Gobierno de recursos cloud
- Seguridad basada en permisos
- Responsabilidad humana en el uso de IA

## Historia sugerida

Una empresa tiene varios recursos en Azure. El equipo quiere revisar si todos cumplen una politica basica de gobierno, por ejemplo, tener tags.

En lugar de revisar manualmente desde el portal, usamos un agente de IA conectado a Azure para consultar los recursos, detectar problemas y generar un resumen ejecutivo.

## Analogia

Copilot es como un asistente ejecutivo.

Azure MCP es como el acceso controlado que le damos para consultar ciertos sistemas.

Azure es la oficina real donde estan los recursos.

El agente no deberia inventar: debe consultar, interpretar y explicar.

## Guion sugerido para explicar la demo

Esta demo nos permite ver una diferencia importante entre un chatbot comun y un agente.

Un chatbot normalmente responde preguntas con texto. En cambio, un agente puede usar herramientas, consultar informacion real y ayudarnos a tomar acciones controladas.

En este caso, el agente se conecta a Azure mediante MCP. Eso significa que no esta inventando informacion, sino consultando recursos reales dentro de una suscripcion de Azure.

La demo crea recursos de prueba: un grupo de recursos, una cuenta de almacenamiento con tags, una red virtual con tags y otra cuenta de almacenamiento sin tags.

El recurso sin tags representa un problema comun de gobierno cloud. En una empresa real, si los recursos no tienen etiquetas, es mas dificil saber a que proyecto pertenecen, quien es responsable, que ambiente usan o como se deben controlar los costos.

Luego usamos Copilot CLI para pedirle al agente que revise los recursos, identifique problemas y genere una explicacion entendible.

## Preguntas para hacer a los alumnos

- Que diferencia ven entre pedirle a la IA que explique Azure y pedirle que consulte Azure directamente?
- Que riesgo existiria si el agente tuviera permisos demasiado amplios?
- Por que los tags son importantes en gobierno cloud?
- Como podria ayudar este tipo de agente a un equipo de soporte o infraestructura?
- Que tareas deberian seguir teniendo aprobacion humana?

## Mensaje clave

La IA generativa se vuelve mas util cuando puede trabajar con contexto real, herramientas reales y permisos reales.

Ese es el salto de un chatbot a un agente.

El valor no esta solamente en que la IA responda, sino en que pueda ayudar a revisar informacion real, detectar problemas y explicar resultados de forma clara.
