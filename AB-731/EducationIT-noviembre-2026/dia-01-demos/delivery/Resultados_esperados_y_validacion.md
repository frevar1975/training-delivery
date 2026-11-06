# Ejemplo resuelto y criterios de validación — AB-731 Día 1

Todos los nombres, casos y cifras son ficticios. Las respuestas generadas en vivo pueden variar; valida los criterios, no la redacción literal.

## Demo 1 — Poner a prueba una respuesta

**Primera instrucción:** “Respondé este reclamo como si fueras la empresa. Sé amable y breve.”

**Qué revisar en la salida:** si ofrece una fecha, afirma que ya abrió o escaló un caso, o confirma una solución, esos datos no están en el reclamo y no deben presentarse como hechos.

**Con contexto y límites:** una respuesta adecuada reconoce la molestia, no promete una fecha y dice que un representante debe verificar el estado del reclamo.

## Demo 2 — Analítica y generación

Aplicando la regla didáctica acordada en clase (prioridad alta si el cliente está marcado como vulnerable o si el caso supera tres días): R-102 se marca por condición prioritaria; R-103 por antigüedad de cinco días. R-101 puede considerarse para revisión por reincidencia según la regla adicional que el grupo defina.

Esto es una regla explícita para el ejercicio; no es una predicción de machine learning. Copilot se usa luego para redactar un borrador, no para validar hechos.

## Demo 3 — Iterar una instrucción

La versión completa debe incluir rol, tarea, contexto, límites y formato. Un resultado útil informa resumen, prioridad sugerida, borrador y dato pendiente. Sigue sin saber el estado real del reclamo.

## Demo 4 — Ejemplo de ficha de caso de uso

- Problema: los reclamos se resumen y derivan manualmente, con demoras y variación entre operadores.
- Apoyo de IA: resumir, sugerir una categoría y preparar un borrador.
- Datos: texto del reclamo, catálogo ficticio de categorías y criterios de derivación.
- Riesgos: prioridad incorrecta, promesas no autorizadas, exposición de datos y trato desigual.
- Control humano: validar prioridades sensibles y aprobar toda respuesta antes de enviarla.
- KPI piloto: tiempo promedio para preparar un borrador y porcentaje de borradores corregidos.
- Condición de revisión: aumento de errores o respuestas que incluyan afirmaciones no sustentadas.

## Demo 5 — Supuestos cuantitativos

- Piloto: 10 usuarios × 20 consultas = **200 consultas por mes**.
- Uso extendido: 500 usuarios × 50 consultas = **25.000 consultas por mes**.

El ejercicio no calcula importes. Para cotizar hacen falta modelo, región, tokens, arquitectura, integración, seguridad, monitoreo y tarifas vigentes.

## Demo 6 — Aprobación humana

El resultado debe quedar como borrador. La persona revisora valida el resumen, justificación de prioridad y promesas. Si falta el estado del caso o hay una situación sensible, corrige o escala; no se afirma que se registró o envió una respuesta.

## Lista de validación

- Separar hechos de inferencias y datos pendientes.
- No inventar fecha, diagnóstico, acción o compensación.
- Explicar que Copilot Chat no consulta un CRM ni registra casos.
- Mantener la aprobación humana antes de enviar mensajes.
- Usar solo datos ficticios en la demostración.
