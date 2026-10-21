# Sesión 1 — Fundamentos de IA y cargas de trabajo

**Centro:** Netxpress  
**Curso:** AI-901T00-A — Introducción a la IA en Azure

## Resultado esperado

Al finalizar, el alumno podrá:

- Diferenciar IA, aprendizaje automático, IA generativa y agentes.
- Asociar un problema con una carga de trabajo de IA.
- Identificar riesgos básicos y controles de IA responsable.
- Probar una instrucción generativa y revisar críticamente su resultado.

## Guion de clase

| Tramo | Duración | Bloque |
|---|---:|---|
| 1 | 15 min | Bienvenida, expectativas y diagnóstico |
| 2 | 30 min | Fundamentos: IA, ML, IA generativa y agentes |
| 3 | 30 min | Cargas de trabajo y selección de escenarios |
| 4 | 10 min | Pausa |
| 5 | 30 min | Principios de IA responsable |
| 6 | 25 min | Modelos generativos, instrucciones y resultados |
| 7 | 30 min | Demo guiada en Microsoft Foundry |
| 8 | 10 min | Comprobación y cierre |

## 1. Bienvenida y diagnóstico

### Apertura sugerida

> En estas sesiones vamos a reconocer qué problemas puede resolver la inteligencia artificial y cómo empezar a construir soluciones con servicios de Azure. Vamos a combinar conceptos con ejemplos y demostraciones. También revisaremos los límites: una respuesta clara o convincente no garantiza que sea correcta.

### Pregunta de entrada

> ¿Qué tarea de su trabajo o vida diaria les gustaría que una solución de IA pudiera ayudar a realizar?

Anota dos o tres ejemplos y retómalos durante la clase.

## 2. Fundamentos

- **Inteligencia artificial:** sistemas que realizan tareas asociadas con capacidades como reconocer patrones, interpretar lenguaje o generar contenido.
- **Aprendizaje automático (ML):** modelos que aprenden patrones a partir de datos para clasificar, estimar o recomendar.
- **IA generativa:** modelos que producen contenido nuevo a partir de una instrucción y contexto.
- **Agente:** solución que usa un modelo y puede apoyarse en instrucciones, conocimiento o herramientas para completar tareas.

### Analogía

> Los datos son ejemplos; el modelo es el patrón que el sistema aprendió; la inferencia es utilizar ese patrón ante un caso nuevo. Un modelo generativo puede redactar una propuesta a partir de instrucciones, pero necesita revisión porque puede equivocarse.

Aclara que las analogías ayudan a entender, pero no describen todos los detalles técnicos del modelo.

## 3. Cargas de trabajo

| Necesidad | Carga de trabajo posible |
|---|---|
| Clasificar reclamos por motivo | Análisis de texto |
| Transcribir una llamada | Reconocimiento de voz |
| Leer campos de una factura | Extracción de información |
| Describir una fotografía | Visión |
| Redactar un borrador de respuesta | IA generativa |
| Consultar información y ejecutar pasos autorizados | Agente |

### Actividad

Pide al grupo elegir la carga adecuada y justificar la elección:

1. Una mesa de ayuda recibe reclamos y quiere priorizarlos.
2. Un área administrativa captura monto, fecha y proveedor desde facturas.
3. Un equipo necesita resumir una reunión y extraer tareas pendientes.

## 4. IA responsable

Usa el caso de un sistema que filtra CV para recomendar candidatos:

- **Equidad:** evitar perjudicar grupos por patrones sesgados en los datos.
- **Confiabilidad y seguridad:** comprobar el funcionamiento y manejar fallos.
- **Privacidad y protección:** limitar los datos personales y controlar el acceso.
- **Inclusión:** considerar capacidades, idiomas y contextos diferentes.
- **Transparencia:** informar cuándo intervino IA y explicar cómo se usa el resultado.
- **Responsabilidad:** definir quién supervisa y responde por las decisiones.

Pregunta:

> Si el sistema descarta automáticamente a una persona, ¿qué evidencia necesitaríamos revisar antes de aceptar esa decisión?

## 5. Modelos generativos

Explica que el resultado depende del modelo, la instrucción, el contexto disponible y la configuración. La salida puede ser útil y aun así contener errores.

**Instrucción inicial**

> Clasifica este reclamo.

**Instrucción mejorada**

> Analiza el reclamo proporcionado. Devuelve únicamente: categoría (facturación, soporte técnico u otro), prioridad (alta, media o baja) y una justificación de una oración. Si falta información, indica “requiere revisión humana”. No inventes datos.

Pregunta:

> ¿Qué partes de la segunda instrucción ayudan a que el resultado sea más fácil de revisar?

## 6. Demo en Microsoft Foundry

### Objetivo

Observar una interacción con un modelo generativo y revisar la calidad de la respuesta.

### Preparación

- Iniciar sesión en Microsoft Foundry.
- Confirmar acceso a un proyecto y a un modelo disponible.
- Usar ejemplos sintéticos; no mostrar claves, datos personales ni información de clientes.
- Probar el entorno previamente. Si no hay acceso, recorrer capturas o la demo local preparada.

### Demo incluida en este delivery

- [Instrucciones para preparar y ejecutar el agente](demo-nuevo-agente/ai-900-demo/README.md)
- La aplicación necesita un endpoint de Microsoft Foundry, un agente accesible y autenticación con Azure CLI.

### Pasos

1. Presentar un reclamo sintético: “Me cobraron dos veces el plan de internet y necesito que revisen el débito de octubre”.
2. Enviar la instrucción: “Clasifica este reclamo”.
3. Revisar si la respuesta incluye categoría, prioridad y explicación.
4. Enviar la instrucción mejorada de la sección anterior.
5. Comparar formato, consistencia, datos inventados y necesidad de revisión humana.
6. Conectar lo observado con prompts y evaluación.

### Resultado que deben observar

Una instrucción más concreta facilita obtener una respuesta estructurada, pero no elimina la necesidad de verificarla.

## 7. Cierre

Preguntas de salida:

1. ¿Qué diferencia hay entre ML e IA generativa?
2. ¿Qué carga de trabajo elegirías para extraer datos de una factura?
3. ¿Qué control agregarías antes de usar automáticamente la clasificación de reclamos?

### Cierre sugerido

> Hoy vimos que la primera decisión no es escoger un servicio, sino entender el problema y los datos. En la próxima sesión entraremos en Microsoft Foundry para observar cómo se prueba un modelo y cómo se construye un agente sencillo.

## Registro posterior

- Temas dictados:
- Demo ejecutada:
- Resultado observado:
- Dudas pendientes:
- Cambios para la siguiente sesión:
