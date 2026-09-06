# Module 05 - Data Loss Prevention

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Comprender cómo Microsoft Purview Data Loss Prevention ayuda a detectar y controlar el uso de información sensible dentro de Microsoft 365.

Hasta ahora trabajamos:

```text
Identity
Access
Roles
Apps
```

Ahora comenzamos a proteger:

```text
DATA
```

---

# 2. Pregunta para iniciar

Preguntar:

> ¿Qué ocurre si un usuario legítimo, correctamente autenticado y con permisos válidos intenta enviar información sensible a una persona que no debería recibirla?

Aquí aparece un problema diferente.

```text
Identity = Correct
Authentication = Correct
Permissions = Correct

BUT

Data movement = Risk
```

Necesitamos controles sobre la información.

---

# 3. ¿Qué es DLP?

DLP significa:

```text
Data Loss Prevention
```

Su objetivo es ayudar a identificar información sensible y controlar determinadas actividades relacionadas con ella.

Modelo:

```text
User activity
     |
     v
Content
     |
     v
DLP Policy
     |
     v
Evaluate
     |
     +---- Allow
     +---- Notify
     +---- Block
     +---- Override
     +---- Alert
```

---

# 4. Analogía

Imagina una empresa que tiene seguridad en la puerta.

El empleado puede entrar porque:

```text
Identity = valid
Access = allowed
```

Pero al salir lleva una carpeta marcada:

```text
CONFIDENTIAL
```

Seguridad puede preguntar:

```text
¿Qué información estás sacando?

¿Está permitido?

¿Necesitas autorización?
```

DLP aplica un concepto similar al movimiento y uso de información digital.

---

# 5. DLP no reemplaza Identity

DLP no sustituye:

```text
MFA
Conditional Access
Permissions
```

Son capas diferentes.

```text
Identity
   |
   v
Access
   |
   v
Permissions
   |
   v
Data activity
   |
   v
DLP
```

---

# 6. Microsoft Purview

Microsoft Purview proporciona capacidades relacionadas con:

```text
Data Security
Compliance
Information Protection
Risk
Governance
```

En este módulo nos concentramos en:

```text
Data Loss Prevention
```

---

# 7. DEMO INSTRUCTOR - Microsoft Purview

Abrir Microsoft Purview.

Mostrar:

```text
Solutions
```

Identificar:

```text
Data Loss Prevention
```

No crear todavía la política.

Primero explicar la estructura.

---

# 8. Componentes principales

Conceptualmente una política DLP responde:

```text
WHERE?
   |
   v
Locations

WHAT?
   |
   v
Sensitive information

WHEN?
   |
   v
Conditions

THEN WHAT?
   |
   v
Actions
```

---

# 9. Analogía de una política

Una regla empresarial puede decir:

```text
SI

un correo contiene información sensible

Y

se intenta compartir de determinada manera

ENTONCES

advertir o bloquear
```

Eso puede representarse como:

```text
IF
   Condition
THEN
   Action
```

---

# 10. Locations

Una política DLP puede aplicarse a ubicaciones y servicios compatibles.

En nuestro laboratorio trabajaremos conceptualmente con:

```text
Exchange
SharePoint
OneDrive
Teams
```

---

# 11. Por qué Locations importa

Una organización puede querer aplicar diferentes controles dependiendo de dónde se encuentre o utilice la información.

Modelo:

```text
Sensitive Data
      |
      +---- Email
      +---- Teams
      +---- SharePoint
      +---- OneDrive
```

DLP permite aplicar políticas sobre ubicaciones compatibles.

---

# 12. Sensitive Information Types

Para aplicar una política primero necesitamos poder reconocer información.

Microsoft Purview utiliza conceptos como:

```text
Sensitive Information Types
```

para identificar determinados patrones de información.

---

# 13. Ejemplos conceptuales

Podemos encontrar tipos relacionados con:

```text
Financial information
Personal identifiers
Government identifiers
Health information
Credentials
```

Las opciones disponibles dependen del entorno y configuración.

---

# 14. Ejemplo del laboratorio

Para hacer visible el funcionamiento utilizaremos:

```text
IP Address
```

Esto nos permite demostrar el motor de reglas sin utilizar información personal real.

---

# 15. Ejemplo

Contenido:

```text
Server address:

192.168.0.1
```

Purview puede evaluar si el contenido coincide con el tipo de información configurado en la regla.

---

# 16. Instance Count

Un concepto importante es:

```text
Instance Count
```

Esto permite diferenciar escenarios según la cantidad de coincidencias.

Ejemplo:

```text
1 IP address
```

frente a:

```text
2 or more IP addresses
```

---

# 17. Nuestro escenario

Crearemos dos comportamientos.

```text
ONE IP
   |
   v
Notify
   |
   v
Allow
```

y:

```text
TWO OR MORE IPs
        |
        v
Notify
        |
        v
Block
        |
        v
Allow override
```

---

# 18. Por qué dos reglas

Esto permite demostrar que DLP no tiene que responder siempre:

```text
BLOCK EVERYTHING
```

Podemos aplicar diferentes controles según el nivel o contexto detectado.

---

# 19. Analogía

Una empresa podría tener:

```text
Documento interno
      |
      v
Advertencia

Documento altamente sensible
      |
      v
Bloqueo
```

DLP permite construir políticas con diferentes niveles de respuesta.

---

# 20. Policy Tips

Una Policy Tip proporciona información al usuario durante una actividad.

Conceptualmente:

```text
User action
    |
    v
DLP detects condition
    |
    v
Policy Tip
    |
    v
User receives guidance
```

---

# 21. DLP también educa

Un control de seguridad no siempre tiene que comenzar bloqueando.

Puede comenzar:

```text
Detect
  |
  v
Notify
  |
  v
Educate
```

Esto ayuda a que los usuarios comprendan las políticas de la organización.

---

# 22. Analogía de Policy Tip

Es parecido a una señal:

```text
ATENCIÓN

Está intentando compartir
información sensible.
```

La señal aparece antes de que el usuario continúe.

---

# 23. Blocking

Para situaciones de mayor riesgo podemos aplicar:

```text
Block
```

Modelo:

```text
Sensitive information detected
             |
             v
            DLP
             |
             v
           BLOCK
```

---

# 24. Override

Algunas organizaciones permiten que el usuario continúe bajo determinadas condiciones.

Modelo:

```text
BLOCK
  |
  v
Override available
  |
  v
Business justification
  |
  v
Continue
```

---

# 25. Analogía de Override

Un empleado intenta realizar una acción restringida.

El sistema responde:

```text
Esta acción normalmente está bloqueada.
```

Pero existe una excepción autorizada:

```text
Explique el motivo.
```

El usuario proporciona:

```text
Business justification
```

y la actividad puede continuar según la política.

---

# 26. Override no significa eliminar el control

El objetivo puede ser permitir una excepción con:

```text
User awareness
+
Justification
+
Visibility
```

en lugar de permitir silenciosamente la acción.

---

# 27. Alerts

Una política también puede generar información para administradores.

Modelo:

```text
DLP event
   |
   +---- User notification
   |
   +---- Administrative visibility
```

Esto permite investigar actividades relevantes.

---

# 28. Detectar vs prevenir

DLP puede utilizarse progresivamente.

```text
Stage 1
Detect

Stage 2
Notify

Stage 3
Restrict

Stage 4
Block
```

No siempre es recomendable comenzar inmediatamente con el control más restrictivo.

---

# 29. Analogía del despliegue gradual

Es similar a Conditional Access.

Primero queremos saber:

```text
¿Qué impacto tendrá esta política?
```

antes de afectar a todos los usuarios.

Patrón:

```text
TEST
 |
 v
OBSERVE
 |
 v
ADJUST
 |
 v
ENFORCE
```

---

# 30. DEMO INSTRUCTOR - DLP Policies

En Microsoft Purview mostrar:

```text
Data Loss Prevention
>
Policies
```

Explicar:

```text
Policy
   |
   v
Locations
   |
   v
Rules
   |
   v
Conditions
   |
   v
Actions
```

---

# 31. DEMO INSTRUCTOR - Crear política

Si el tiempo lo permite, comenzar el asistente:

```text
Create policy
```

Mostrar:

```text
Templates
Custom
```

No es necesario terminar la política durante la explicación.

La configuración completa se realizará en:

```text
Lab 03
```

---

# 32. Custom Policy

En nuestro laboratorio utilizaremos una política personalizada.

Nombre:

```text
IP Address DLP Policy
```

Esto nos permite controlar exactamente:

```text
Conditions
+
Actions
```

---

# 33. Estructura del laboratorio

```text
IP Address DLP Policy
        |
        +---- Single IP Address Rule
        |
        +---- Multiple IP Address Rule
```

---

# 34. Single IP Address Rule

Condición:

```text
Sensitive Information Type
=
IP Address
```

Instance Count:

```text
1
```

Acción conceptual:

```text
Notify
+
Allow
```

---

# 35. Multiple IP Address Rule

Condición:

```text
Sensitive Information Type
=
IP Address
```

Instance Count:

```text
2 or more
```

Acción:

```text
Notify
+
Block
+
Override
+
Alert
```

---

# 36. Visualización completa

```text
EMAIL
  |
  v
DLP
  |
  +-------------------------+
  |                         |
1 IP                      2+ IP
  |                         |
  v                         v
Notify                    Notify
  |                         |
  v                         v
Allow                     Block
                            |
                            v
                         Override
                            |
                            v
                      Justification
```

---

# 37. Prueba 1

Contenido:

```text
192.168.0.1
```

Resultado esperado:

```text
Detection
+
Policy Tip
+
Allow
```

---

# 38. Prueba 2

Contenido:

```text
192.168.0.1

172.16.0.1
```

Resultado esperado:

```text
Detection
+
Policy Tip
+
Block
+
Override option
```

---

# 39. Justificación de laboratorio

Ejemplo:

```text
Authorized lab test for MS-4002 training.
```

Nunca utilizar información real para estas pruebas.

---

# 40. Dos identidades de prueba

Para Standalone podemos utilizar:

```text
Browser
   |
   v
LAB-User1
```

y:

```text
InPrivate
   |
   v
LAB-User2
```

Esto sustituye la necesidad de utilizar dos máquinas virtuales.

---

# 41. DEMO INSTRUCTOR - Dos sesiones

Mostrar cómo mantener:

```text
Session 1
LAB-User1
```

y:

```text
Session 2
LAB-User2
```

utilizando:

```text
normal browser
+
InPrivate / second profile
```

---

# 42. Propagación

Las políticas de Microsoft 365 pueden requerir tiempo para propagarse.

Por eso:

```text
Policy created
      |
      v
Does NOT always mean
      |
      v
Immediately testable
```

---

# 43. Regla para la clase

Si una política no funciona inmediatamente:

```text
DO NOT
recreate repeatedly
```

Primero revisar:

```text
Scope
Users
Locations
Rules
Policy mode
Propagation
```

---

# 44. Plan B para una clase

Idealmente el instructor puede disponer de:

```text
una política previamente preparada
```

para demostrar el resultado si la política creada por los alumnos todavía no se propagó.

Patrón:

```text
Students create
       |
       v
Understand configuration

Instructor pre-staged policy
       |
       v
Demonstrate behavior
```

---

# 45. Troubleshooting conceptual

Si DLP no detecta:

```text
Check policy
     |
     v
Check locations
     |
     v
Check sensitive info type
     |
     v
Check instance count
     |
     v
Check user scope
     |
     v
Check propagation
```

---

# 46. DLP y Copilot

Este es el punto importante para MS-4002.

Copilot se incorpora a un entorno donde la organización ya debe tener políticas de protección de información.

DLP forma parte de esa estrategia.

Modelo:

```text
Microsoft 365 Data
        |
        v
Security & Compliance Controls
        |
        +---- Permissions
        +---- DLP
        +---- Labels
        |
        v
Copilot environment
```

---

# 47. Qué NO debemos decir

Evitar simplificar diciendo:

```text
DLP protege Copilot
```

como si fuera una única barrera delante de Copilot.

Es más correcto explicar que DLP forma parte de los controles de seguridad y cumplimiento del entorno Microsoft 365 en el que Copilot opera.

---

# 48. Caso empresarial

Un usuario intenta enviar:

```text
Customer financial data
```

a un destinatario no autorizado.

La identidad es válida.

El usuario tiene acceso al documento.

Pero la organización tiene una política:

```text
Sensitive financial data
        |
        v
External sharing
        |
        v
BLOCK
```

Aquí DLP agrega una capa adicional de control.

---

# 49. Comparación con permisos

Permissions responden:

```text
¿Puede el usuario acceder
a esta información?
```

DLP responde:

```text
¿Qué puede ocurrir cuando
esa información es utilizada
o compartida?
```

---

# 50. Comparación con Conditional Access

Conditional Access:

```text
USER
 |
 v
ACCESS TO RESOURCE
```

DLP:

```text
DATA
 |
 v
ACTIVITY
```

Son controles distintos.

---

# 51. Relación con Lab 03

Este módulo prepara directamente:

```text
Standalone Lab 03
Data Loss Prevention
```

El alumno realizará:

```text
Purview
   |
   v
Custom DLP Policy
   |
   v
Sensitive Info Type
   |
   v
Rules
   |
   +---- Notify
   +---- Block
   +---- Override
   |
   v
Testing
```

---

# 52. Qué ejecuta el alumno

Durante el Lab 03:

```text
Create policy
Configure locations
Create rules
Configure Policy Tips
Configure block
Configure override
Test one IP
Test multiple IPs
Review behavior
```

---

# 53. Qué puede quedar como demo

Dependiendo de:

```text
Licensing
Time
Tenant
Propagation
```

el instructor puede demostrar:

```text
Alerts
Monitoring
Advanced policy configuration
```

sin exigir que cada alumno complete todas las variantes.

---

# 54. Pregunta de comprobación

Preguntar:

> ¿Cuál es la diferencia entre una Policy Tip y un Block?

Respuesta:

```text
Policy Tip
=
informa/orienta al usuario

Block
=
restringe la actividad
```

---

# 55. Segunda comprobación

Preguntar:

> ¿Por qué permitiríamos Override?

Respuesta conceptual:

```text
Porque algunas actividades
pueden tener una razón empresarial válida,
pero queremos control y justificación.
```

---

# 56. Tercera comprobación

Preguntar:

> ¿Por qué no empezamos necesariamente bloqueando todo?

Respuesta:

```text
Porque primero debemos comprender
el impacto de la política.
```

---

# 57. Mensaje clave

El alumno debe recordar:

> DLP no solamente detecta información sensible; permite decidir qué hacer cuando esa información aparece en una actividad determinada.

Modelo:

```text
Detect
  |
  v
Evaluate
  |
  v
Respond
```

---

# 58. Transición

Ahora sabemos controlar:

```text
¿Qué ocurre cuando
la información sensible
es utilizada o compartida?
```

Pero todavía falta responder:

```text
¿Qué ES esta información
y cómo debería clasificarse?
```

Siguiente:

```text
Module 06
Sensitivity Labels
```

donde veremos:

```text
Information
     |
     v
Classification
     |
     v
Sensitivity Label
     |
     +---- Marking
     +---- Protection
     +---- Encryption
```