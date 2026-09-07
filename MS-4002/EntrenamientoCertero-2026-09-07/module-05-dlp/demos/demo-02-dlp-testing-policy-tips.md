# DEMO 02 - Probar DLP y Policy Tips

## MS-4002 - Module 05: Data Loss Prevention

---

## Duración

15 a 20 minutos

## Tipo

DEMO INSTRUCTOR - PRUEBA CONTROLADA

## Portales

```text
Microsoft 365
https://www.microsoft365.com

Microsoft Purview
https://purview.microsoft.com
```

---

# Objetivo

Probar la política creada en el Demo 01:

```text
IP Address DLP Policy
```

y comparar dos situaciones:

```text
TEST 1
1 IP Address
→ Policy Tip
→ Allow
```

contra:

```text
TEST 2
2+ IP Addresses
→ Policy Tip
→ Restriction
→ Override / Justification
→ Alert
```

---

# Escenario

Contoso ya configuró:

```text
IP Address DLP Policy
```

con:

```text
Single IP Address Rule
Multiple IP Address Rule
```

Ahora debemos comprobar si la política produce la experiencia esperada.

---

# 1. Antes de probar

No comenzar creando contenido inmediatamente.

Primero revisar:

```text
Policy exists
Policy status
Policy mode
Locations
Rules
Scope
```

---

# 2. Abrir Microsoft Purview

Entrar a:

```text
https://purview.microsoft.com
```

Ir a:

```text
Solutions
→ Data Loss Prevention
→ Policies
```

Buscar:

```text
IP Address DLP Policy
```

---

# 3. Revisar la política

Abrir la política.

Confirmar que existen:

```text
Single IP Address Rule

Multiple IP Address Rule
```

---

# 4. Recordar la lógica

Mostrar:

```text
1 IP
 |
 v
Single IP Address Rule
 |
 v
Policy Tip
 |
 v
Allow
```

y:

```text
2+ IPs
 |
 v
Multiple IP Address Rule
 |
 v
Policy Tip
 |
 v
Restrict
 |
 +--> Override
 |
 +--> Alert
```

---

# 5. Importante: propagación

Explicar:

```text
Policy configured
≠
Policy immediately available
```

Los cambios de DLP pueden requerir tiempo para propagarse.

Por eso, si la prueba no funciona inmediatamente:

```text
NO recrear la política
NO modificar cinco opciones a la vez
NO asumir que DLP está roto
```

---

# 6. Preparar dos identidades

Para el laboratorio podemos utilizar:

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>
```

y:

```text
Laura Rojas - Test User 2
lab-user2@<TU-DOMINIO>
```

---

# 7. Estrategia de navegador

Utilizar:

```text
Browser normal
→ Carlos

InPrivate / segundo perfil
→ Laura
```

Esto permite demostrar diferentes experiencias sin cerrar continuamente la sesión administrativa.

---

# 8. TEST 1 - Una dirección IP

Iniciar sesión como:

```text
Carlos Mendoza - Test User 1
```

Abrir una aplicación Microsoft 365 compatible con la ubicación y política configuradas.

Para una demostración simple puede utilizarse:

```text
Outlook on the web
```

si Exchange está disponible en el tenant.

---

# 9. Crear mensaje de prueba

Crear un nuevo correo.

Destinatario:

```text
Laura Rojas - Test User 2
```

Asunto:

```text
DLP Policy Test 1
```

Cuerpo:

```text
MS-4002 authorized lab test.

Test IP address:

192.168.0.1
```

---

# 10. Detenerse antes de enviar

No enviar inmediatamente.

Esperar y observar si aparece:

```text
Policy Tip
```

o una advertencia equivalente.

---

## Qué explicar

La política está evaluando:

```text
Content
   ↓
Sensitive Information Type
   ↓
IP Address
   ↓
Instance Count
```

---

# 11. Resultado esperado del Test 1

Conceptualmente:

```text
1 IP Address detected
        ↓
Single IP Address Rule
        ↓
Policy Tip
        ↓
User can continue
```

---

# 12. Qué mostrar al alumno

Señalar la advertencia.

Explicar:

```text
DLP detected something
```

pero:

```text
DLP did not necessarily block the user
```

---

# 13. Policy Tip

Explicar:

Un Policy Tip permite informar al usuario durante su flujo de trabajo.

Conceptualmente:

```text
User action
    ↓
DLP detects risk
    ↓
Policy Tip
    ↓
User becomes aware
```

---

# 14. Pregunta para la clase

> ¿DLP siempre tiene que bloquear?

Respuesta:

```text
No.
```

Puede:

```text
Detect
Notify
Audit
Restrict
Block
Allow override
Generate alerts
```

dependiendo de la política.

---

# 15. Completar Test 1

Si el entorno permite enviar el mensaje y está dentro del alcance controlado del laboratorio:

```text
Send
```

Si no queremos generar correo:

```text
cancelar el mensaje después de observar el Policy Tip
```

---

# 16. TEST 2 - Dos direcciones IP

Crear otro correo.

Destinatario:

```text
Laura Rojas - Test User 2
```

Asunto:

```text
DLP Policy Test 2
```

Cuerpo:

```text
MS-4002 authorized lab test.

Test IP addresses:

192.168.0.1

172.16.0.1
```

---

# 17. Comparar

TEST 1 tenía:

```text
192.168.0.1
```

TEST 2 tiene:

```text
192.168.0.1

172.16.0.1
```

---

# 18. Preguntar antes de ver el resultado

> ¿Qué cambió?

Respuesta:

```text
Instance Count
```

---

# 19. Resultado esperado del Test 2

Conceptualmente:

```text
2 IP Addresses detected
        ↓
Multiple IP Address Rule
        ↓
Policy Tip
        ↓
Restriction
```

---

# 20. Mostrar la restricción

Dependiendo de la ubicación y configuración de la política, mostrar el mensaje equivalente a:

```text
This action is restricted by your organization's policy.
```

El texto exacto puede variar.

---

# 21. Mostrar Override

Si configuramos:

```text
Allow override
```

mostrar la opción disponible para continuar.

---

# 22. Justificación

Cuando solicite una justificación utilizar:

```text
Authorized lab test for MS-4002 training.
```

---

# 23. Qué explicar

El usuario no está simplemente ignorando la política.

Está realizando una:

```text
documented exception
```

Conceptualmente:

```text
Policy
   ↓
Restriction
   ↓
Business justification
   ↓
Exception
   ↓
Audit trail
```

---

# 24. False Positive

Si aparece:

```text
Report as false positive
```

mostrarlo.

Explicar la diferencia.

### Business justification

```text
La detección es correcta,
pero existe una razón empresarial
para continuar.
```

### False positive

```text
El usuario considera
que la detección no corresponde.
```

---

# 25. No confundir ambas opciones

Mostrar:

```text
Detected correctly
+
Need exception
=
Business justification
```

frente a:

```text
Detection considered incorrect
=
False positive
```

---

# 26. Completar o cancelar la prueba

Si el entorno es exclusivamente de laboratorio y está autorizado:

```text
complete the override
```

Si solamente queremos demostrar la experiencia:

```text
cancel
```

después de mostrarla.

---

# 27. Cambiar a la perspectiva administrativa

Ahora pasar de:

```text
USER EXPERIENCE
```

a:

```text
ADMIN EXPERIENCE
```

Abrir:

```text
https://purview.microsoft.com
```

con la cuenta administrativa.

---

# 28. Revisar Alerts

Ir a la sección disponible relacionada con:

```text
Data Loss Prevention
→ Alerts
```

o la experiencia equivalente del portal.

---

# 29. Buscar eventos relacionados

Buscar actividad relacionada con:

```text
IP Address DLP Policy
```

o:

```text
Multiple IP Address Rule
```

según lo que muestre el tenant.

---

# 30. Qué mostrar

Si existe un evento disponible, revisar:

```text
Policy

Rule

User

Activity

Location

Timestamp
```

y cualquier información adicional disponible.

---

# 31. Mostrar Activity Explorer

Si está disponible:

```text
Data Loss Prevention
→ Activity explorer
```

Mostrar cómo un administrador puede investigar eventos relacionados con información protegida.

---

# 32. Aplicar filtros

Cuando sea posible, mostrar filtros como:

```text
Date

User

Activity

Policy

Location
```

No es necesario realizar una investigación completa.

---

# 33. Relacionar usuario y administrador

Mostrar:

```text
USER SIDE

Content
  ↓
Detection
  ↓
Policy Tip
  ↓
Restriction / Override
```

y:

```text
ADMIN SIDE

Event
  ↓
Alert
  ↓
Investigation
  ↓
Governance
```

---

# 34. Ejemplo empresarial

Supongamos que un empleado intenta enviar:

```text
500 credit card numbers
```

La empresa podría decidir:

```text
detect
↓
block
↓
alert security
↓
investigate
```

Mientras que otro escenario podría ser:

```text
1 internal identifier
↓
warn
↓
allow
```

---

# 35. Acción proporcional al riesgo

Mensaje importante:

```text
Different risk
=
Different response
```

Por eso nuestro laboratorio utiliza:

```text
1 IP
```

y:

```text
2+ IPs
```

para demostrar dos comportamientos distintos.

---

# 36. DLP como experiencia educativa

Explicar que Policy Tips también ayudan a:

```text
educate users
```

en el momento en que ocurre la acción.

No todo control de seguridad necesita ser invisible.

---

# 37. DLP y comportamiento del usuario

Mostrar:

```text
Without DLP

User
→ Send
```

frente a:

```text
With DLP

User
→ Send
→ Warning
→ Think
→ Decide
```

---

# 38. DLP y Copilot

Relacionar nuevamente:

```text
Copilot
   ↓
Works with organizational data
   ↓
Data requires governance
   ↓
DLP provides controls
```

---

# 39. DLP no reemplaza permisos

Reforzar:

```text
Permissions
→ Who can access?
```

```text
DLP
→ What can they do with sensitive information?
```

Son problemas relacionados pero diferentes.

---

# 40. DLP vs Sensitivity Labels

Preparar Module 06:

```text
DLP
→ detects conditions and controls activities
```

```text
Sensitivity Labels
→ classify and protect information
```

Ejemplo:

```text
DLP:
"Este documento contiene PII."

Label:
"Este documento es Confidential."
```

---

# 41. Si NO aparece el Policy Tip

No cambiar inmediatamente la política.

Revisar:

```text
Policy status

Policy mode

Locations

User scope

Rule condition

Sensitive Information Type

Instance Count

Propagation
```

---

# 42. Si ambas pruebas producen el mismo resultado

Revisar especialmente:

```text
Instance Count
```

y:

```text
Rule priority
```

También comprobar que ambas reglas no estén configuradas de forma que la primera condición capture ambos escenarios.

---

# 43. Si no aparece Alert

No significa necesariamente que la detección haya fallado.

Revisar:

```text
Alert configuration

Incident reporting

Rule configuration

Propagation / processing delay
```

Los eventos administrativos pueden no aparecer de forma inmediata.

---

# 44. Si Outlook no está disponible

Utilizar otra ubicación habilitada en la política.

Por ejemplo:

```text
SharePoint
```

o:

```text
OneDrive
```

Crear un documento de prueba con:

```text
192.168.0.1
```

y posteriormente:

```text
192.168.0.1
172.16.0.1
```

---

# 45. Si el entorno no está listo

No detener la clase.

Utilizar el flujo conceptual:

```text
CONTENT
   ↓
DETECTION
   ↓
RULE
   ↓
ACTION
   ↓
USER EXPERIENCE
   ↓
ADMIN EXPERIENCE
```

y continuar posteriormente con el Lab 03.

---

# 46. Qué NO hacer

No utilizar:

```text
real credit card numbers

real passwords

real customer data

real employee PII

production documents
```

Utilizar únicamente datos ficticios de laboratorio.

---

# 47. Resultado esperado

El alumno debe poder explicar la diferencia entre:

```text
Detection

Policy Tip

Restriction

Block

Override

False Positive

Alert

Activity Explorer
```

---

# 48. Resumen visual

```text
             IP Address DLP Policy
                       |
          +------------+------------+
          |                         |
          v                         v
       1 IP                      2+ IPs
          |                         |
          v                         v
   Single IP Rule          Multiple IP Rule
          |                         |
          v                         v
     Policy Tip                Policy Tip
          |                         |
          v                         v
        Allow                  Restrict
                                    |
                            +-------+-------+
                            |               |
                            v               v
                         Override         Alert
```

---

# 49. Mensaje clave

> Una buena política DLP no se limita a bloquear. Detecta el riesgo, informa al usuario, aplica una respuesta proporcional y proporciona visibilidad administrativa.

---

# 50. Cierre de Module 05

Ya recorrimos:

```text
Design DLP Policy
       ↓
Configure Rules
       ↓
Detect Sensitive Information
       ↓
Policy Tip
       ↓
Restriction
       ↓
Override
       ↓
Alert
       ↓
Investigation
```

---

# 51. Relación con Lab 03 Standalone

El laboratorio completo está en:

```text
labs
└── standalone
    └── lab-03-dlp
        ├── student-guide.md
        └── instructor-guide.md
```

El demo muestra el flujo.

El laboratorio permite que el alumno lo ejecute.

---

# 52. Transición

Con esto terminamos el bloque principal de la Clase 2:

```text
Module 03
Roles & Permissions
        ↓
Module 04
Microsoft 365 Apps
        ↓
Module 05
Data Loss Prevention
```

El siguiente gran bloque será:

```text
Module 06
Sensitivity Labels
```

que dejaremos principalmente para la Clase 3.