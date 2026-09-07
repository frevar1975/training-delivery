# DEMO 01 - Crear una política DLP en Microsoft Purview

## MS-4002 - Module 05: Data Loss Prevention

---

## Duración

20 a 25 minutos

## Tipo

DEMO INSTRUCTOR - CONFIGURACIÓN GUIADA

## Portal

```text
Microsoft Purview
https://purview.microsoft.com
```

---

# Objetivo

Crear una política personalizada de Data Loss Prevention para demostrar cómo Microsoft Purview puede detectar información sensible y aplicar diferentes acciones dependiendo de la cantidad de coincidencias encontradas.

Crearemos:

```text
IP Address DLP Policy
```

con dos reglas:

```text
IP Address DLP Policy
│
├── Single IP Address Rule
│      1 IP
│      ↓
│      Policy Tip
│      ↓
│      Allow
│
└── Multiple IP Address Rule
       2 o más IP
       ↓
       Policy Tip
       ↓
       Restrict / Block
       ↓
       Override con justificación
       ↓
       Alert
```

---

# Escenario

Contoso quiere controlar documentos y comunicaciones que contienen direcciones IP.

Una sola dirección IP puede representar un caso informativo.

Pero múltiples direcciones IP pueden representar información técnica que la organización desea proteger.

La organización decide:

```text
1 IP
→ advertir al usuario

2 o más IP
→ aplicar una restricción mayor
```

---

# 1. Introducción antes de entrar al portal

Explicar:

DLP significa:

```text
Data Loss Prevention
```

Su objetivo es ayudar a identificar y proteger información sensible mientras los usuarios trabajan con Microsoft 365.

---

# 2. Modelo mental de una política DLP

Antes de entrar al portal mostrar:

```text
WHERE
   ↓
Locations

WHAT
   ↓
Sensitive information

WHEN
   ↓
Conditions

THEN
   ↓
Actions
```

Ejemplo:

```text
WHERE
Exchange / SharePoint / OneDrive / Teams

WHAT
IP Address

WHEN
1 occurrence

THEN
Warn
```

y:

```text
WHEN
2+ occurrences

THEN
Restrict
```

---

# 3. Abrir Microsoft Purview

Abrir:

```text
https://purview.microsoft.com
```

Iniciar sesión con la cuenta administrativa del tenant de práctica.

---

# 4. Localizar Data Loss Prevention

La experiencia de navegación puede cambiar.

Buscar:

```text
Solutions
```

y localizar:

```text
Data Loss Prevention
```

Si el menú no coincide exactamente, utilizar la búsqueda del portal:

```text
Data Loss Prevention
```

---

# 5. Mostrar la página de DLP

Antes de crear nada, detenerse unos minutos.

Mostrar áreas como:

```text
Policies

Activity explorer

Alerts
```

según lo disponible en el tenant.

---

## Qué explicar

```text
Policies
```

define cómo queremos proteger la información.

```text
Activity explorer
```

permite investigar actividad relacionada con datos.

```text
Alerts
```

permite revisar determinados eventos generados por políticas.

---

# 6. Entrar a Policies

Seleccionar:

```text
Policies
```

Mostrar las políticas existentes.

---

## Importante

No modificar políticas que ya existan.

Nuestro objeto será claramente identificable como laboratorio:

```text
IP Address DLP Policy
```

---

# 7. Crear una política

Seleccionar la opción equivalente a:

```text
Create policy
```

---

# 8. Seleccionar el tipo de política

Elegir una opción que permita crear una política:

```text
Custom
```

y posteriormente:

```text
Custom policy
```

La denominación exacta puede variar según la experiencia actual del portal.

---

## Qué explicar

Microsoft Purview dispone de:

```text
Templates
```

para escenarios conocidos.

Pero utilizaremos:

```text
Custom
```

porque queremos comprender cómo se construye la lógica.

---

# 9. Nombre de la política

Utilizar exactamente:

```text
Name:
IP Address DLP Policy
```

Descripción sugerida:

```text
MS-4002 lab policy for detecting IP address information.
```

---

# 10. Elegir ubicaciones

Seleccionar las ubicaciones disponibles correspondientes al laboratorio:

```text
Exchange email

SharePoint sites

OneDrive accounts

Teams chat and channel messages
```

---

## Qué explicar

Aquí respondemos:

```text
WHERE?
```

Es decir:

```text
¿Dónde queremos detectar la información?
```

---

# 11. Alcance del laboratorio

Si el portal permite limitar fácilmente usuarios, grupos, sitios o cuentas, utilizar únicamente objetos del laboratorio cuando sea práctico.

Evitar afectar innecesariamente a todo un tenant compartido.

---

# 12. Llegar a la configuración avanzada

Seleccionar la opción equivalente a:

```text
Create or customize advanced DLP rules
```

o:

```text
Advanced DLP rules
```

según la interfaz disponible.

---

# 13. Crear la primera regla

Seleccionar:

```text
Create rule
```

Nombre:

```text
Single IP Address Rule
```

---

# 14. Definir la condición

Buscar una condición relacionada con:

```text
Content contains
```

y agregar:

```text
Sensitive info types
```

---

# 15. Buscar IP Address

Buscar:

```text
IP Address
```

Seleccionar el Sensitive Information Type disponible para direcciones IP.

---

## Qué explicar

Un:

```text
Sensitive Information Type
```

es una definición utilizada por Microsoft Purview para identificar determinados patrones o tipos de información.

Ejemplos:

```text
Credit Card Number

Passport Number

National identifiers

IP Address
```

---

# 16. Instance Count

Configurar la primera regla para representar:

```text
1 occurrence
```

o el rango equivalente disponible en el portal.

Conceptualmente:

```text
Instance Count = 1
```

---

## Qué explicar

La misma información sensible puede requerir distintas acciones dependiendo de:

```text
cantidad

contexto

ubicación

usuario

actividad
```

---

# 17. Primera acción

Para esta regla queremos:

```text
Notify / Policy Tip
```

pero NO queremos bloquear el contenido.

---

# 18. Configurar notificación

Activar las opciones disponibles relacionadas con:

```text
User notifications
```

y:

```text
Policy tips
```

---

## Mensaje conceptual

Queremos que el usuario reciba una advertencia similar a:

```text
This content contains information
that matches your organization's DLP policy.
```

No necesitamos que el texto sea idéntico.

---

# 19. No bloquear en la primera regla

Confirmar que la primera regla NO aplique una acción equivalente a:

```text
Block
```

o:

```text
Restrict access
```

---

# 20. Resultado de la primera regla

Debemos terminar conceptualmente con:

```text
Single IP Address Rule

IF
Content contains IP Address

AND
Instance Count = 1

THEN
Show notification / Policy Tip

BUT
Allow user action
```

---

# 21. Crear la segunda regla

Agregar otra regla:

```text
Multiple IP Address Rule
```

---

# 22. Agregar Sensitive Information Type

Nuevamente:

```text
Content contains
→ Sensitive info types
→ IP Address
```

---

# 23. Configurar Instance Count

Esta vez queremos representar:

```text
2 or more
```

Conceptualmente:

```text
Instance Count >= 2
```

Configurar el rango equivalente que ofrezca el portal.

---

# 24. Explicar la diferencia

Mostrar:

```text
RULE 1

1 IP
↓
Warn
↓
Allow
```

frente a:

```text
RULE 2

2+ IPs
↓
Warn
↓
Restrict
```

---

# 25. Configurar Policy Tip

Activar nuevamente:

```text
User notifications
```

y:

```text
Policy tips
```

---

# 26. Configurar restricción

En esta segunda regla habilitar la acción disponible equivalente a:

```text
Restrict access
```

o:

```text
Block
```

según la ubicación y experiencia actual del portal.

---

## Importante

Antes de guardar cualquier acción restrictiva:

```text
confirmar el alcance
```

No queremos bloquear contenido real de usuarios de producción.

---

# 27. Configurar Override

Si el tenant y la acción seleccionada lo permiten, habilitar:

```text
Allow users to override
```

con:

```text
Business justification
```

---

## Qué explicar

DLP no siempre significa:

```text
NO
```

Puede significar:

```text
STOP
   ↓
WARN
   ↓
ASK WHY
   ↓
ALLOW EXCEPTION
   ↓
AUDIT
```

---

# 28. Ejemplo de justificación

Durante el laboratorio utilizaremos:

```text
Authorized lab test for MS-4002 training.
```

---

# 29. False Positive

Si aparece la opción:

```text
Report as false positive
```

mostrarla.

Explicar que permite al usuario indicar que considera incorrecta la detección.

---

# 30. Configurar alerta

Si está disponible, configurar la regla para generar una alerta administrativa cuando corresponda.

Mostrar las opciones relacionadas con:

```text
Incident reports

Alerts

Admin notifications
```

---

## Qué explicar

Ahora tenemos dos experiencias distintas:

```text
USER
↓
Policy Tip

ADMIN
↓
Alert / Event
```

---

# 31. Revisar prioridad de reglas

Explicar que cuando existen varias reglas debemos considerar:

```text
conditions

actions

priority

evaluation
```

La lógica debe evitar que una regla general produzca un resultado contrario al esperado por una regla más restrictiva.

---

# 32. Revisar las dos reglas

Antes de avanzar, confirmar visualmente:

```text
IP Address DLP Policy

Single IP Address Rule

Multiple IP Address Rule
```

---

# 33. Elegir modo de implementación

Si el asistente ofrece opciones como:

```text
Run the policy in simulation mode

Turn it on right away

Keep it off
```

para clase preferimos inicialmente una modalidad controlada como:

```text
Simulation / Test
```

cuando esté disponible y sea compatible con lo que queremos demostrar.

---

## Qué explicar

Una política de seguridad no debería pasar directamente de:

```text
idea
```

a:

```text
production blocking
```

Una estrategia más segura es:

```text
Design
   ↓
Test
   ↓
Observe
   ↓
Tune
   ↓
Enforce
```

---

# 34. Estrategia empresarial

Mostrar:

```text
Stage 1
Detect

Stage 2
Notify

Stage 3
Restrict with override

Stage 4
Block
```

---

# 35. Crear la política

Revisar:

```text
Name

Locations

Rules

Sensitive Information Type

Instance Count

Notifications

Restrictions

Override

Alerts

Mode
```

Después seleccionar:

```text
Create
```

o la opción equivalente.

---

# 36. Resultado esperado

Debe aparecer:

```text
IP Address DLP Policy
```

en la lista de políticas.

---

# 37. No esperar funcionamiento instantáneo

Explicar:

```text
Policy created
≠
Policy immediately active everywhere
```

Las políticas de Microsoft 365 pueden requerir tiempo para propagarse.

---

# 38. Preparar la prueba posterior

En el siguiente demo utilizaremos dos escenarios.

### Test 1

```text
192.168.0.1
```

Resultado esperado:

```text
Single IP Address Rule
→ Policy Tip
→ User can continue
```

### Test 2

```text
192.168.0.1

172.16.0.1
```

Resultado esperado:

```text
Multiple IP Address Rule
→ Policy Tip
→ Restriction
→ Override if configured
```

---

# 39. Pregunta para la clase

> ¿Qué cambia entre el Test 1 y el Test 2?

Respuesta:

```text
Instance Count
```

No cambió:

```text
Sensitive Information Type
```

Cambió:

```text
cantidad de coincidencias
```

y por lo tanto:

```text
acción aplicada
```

---

# 40. Relación con Copilot

Explicar:

Copilot trabaja con información a la que el usuario ya tiene acceso.

Por eso necesitamos una estrategia de protección de datos.

Conceptualmente:

```text
Microsoft 365 Data
        ↓
Permissions
        ↓
DLP / Labels
        ↓
Governance
        ↓
Copilot
```

---

# 41. DLP no corrige permisos

Muy importante:

```text
DLP
≠
Permissions
```

Si un archivo está compartido incorrectamente, DLP no reemplaza una correcta administración de permisos.

Son capas diferentes.

---

# 42. Diferenciar DLP de Sensitivity Labels

Anticipar el siguiente módulo:

```text
DLP
→ detecta condiciones
→ controla actividades
```

mientras:

```text
Sensitivity Label
→ clasifica
→ marca
→ puede proteger el contenido
```

---

# 43. Qué NO hacer

No:

```text
modificar políticas existentes

crear políticas globales agresivas

bloquear usuarios reales

utilizar datos sensibles reales

probar con información personal real

asumir que la propagación es inmediata
```

---

# 44. Plan B - No aparece IP Address

Si el Sensitive Information Type no está disponible o aparece con otra denominación:

```text
no improvisar una política de producción
```

Mostrar la búsqueda y explicar el concepto.

Podemos continuar la explicación con el diseño:

```text
Sensitive Information Type
+
Instance Count
+
Action
```

y revisar posteriormente la disponibilidad del tenant.

---

# 45. Plan B - No aparece alguna ubicación

La disponibilidad puede depender de:

```text
tenant

license

service configuration

portal experience
```

Utilizar las ubicaciones disponibles para demostrar el concepto.

---

# 46. Plan B - La política todavía no funciona

No recrear inmediatamente la política.

Primero revisar:

```text
Status

Mode

Locations

Rules

Users

Propagation time
```

---

# 47. Resultado pedagógico

El alumno debe poder construir mentalmente:

```text
DLP Policy
    |
    +-- Locations
    |
    +-- Sensitive Information Types
    |
    +-- Conditions
    |
    +-- Instance Count
    |
    +-- Actions
    |
    +-- Notifications
    |
    +-- Override
    |
    +-- Alerts
```

---

# 48. Mensaje clave

> DLP no consiste simplemente en bloquear información. Consiste en detectar el contexto, aplicar una acción proporcional al riesgo y permitir que la organización controle cómo se utiliza la información sensible.

---

# 49. Transición

Siguiente demo:

```text
DEMO 02
DLP Testing and Policy Tips
```

Ahí comprobaremos:

```text
1 IP
vs
2 IPs
```

y veremos la experiencia desde dos perspectivas:

```text
USER
+
ADMINISTRATOR
```