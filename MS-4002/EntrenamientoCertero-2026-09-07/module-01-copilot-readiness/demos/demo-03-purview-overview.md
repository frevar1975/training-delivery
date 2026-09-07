# DEMO 03 - Microsoft Purview Overview

## MS-4002 - Module 01: Copilot Readiness

---

## Duración

5 a 10 minutos

## Tipo

DEMO INSTRUCTOR

## Portal

https://purview.microsoft.com

---

## Objetivo

Mostrar a los alumnos dónde se administran los principales controles de protección de la información y cumplimiento en Microsoft Purview.

Al finalizar la demo, el alumno debe poder identificar:

```text
Data Loss Prevention
Sensitivity Labels
Information Protection
Alerts
Policy areas
```

---

## Escenario

Contoso quiere preparar Microsoft 365 antes de habilitar Copilot.

Ya revisamos:

```text
Microsoft 365 Admin Center
Microsoft Entra
```

Ahora necesitamos responder:

```text
¿Cómo protegemos información sensible?

¿Cómo evitamos que ciertos datos salgan de la organización?

¿Cómo clasificamos documentos?

¿Cómo aplicamos políticas de protección?
```

---

# 1. Entrar a Microsoft Purview

Abrir:

```text
https://purview.microsoft.com
```

Iniciar sesión con la cuenta administrativa del tenant de práctica.

---

## Qué explicar

Microsoft Purview es el portal donde administramos capacidades relacionadas con:

```text
Data Security
Information Protection
Data Loss Prevention
Compliance
Risk
```

En MS-4002 nos enfocaremos principalmente en:

```text
DLP
Sensitivity Labels
```

---

# 2. Ubicar Data Loss Prevention

Buscar la sección:

```text
Solutions
→ Data Loss Prevention
```

o la ubicación equivalente que muestre el tenant.

No crear ninguna política todavía.

---

## Qué explicar

DLP significa:

```text
Data Loss Prevention
```

Su propósito es ayudar a detectar y controlar información sensible.

Ejemplo:

```text
Email contains sensitive information
        |
        v
DLP Policy
        |
        +---- Allow
        |
        +---- Warn
        |
        +---- Block
```

---

# 3. Ejemplo sencillo de DLP

Usar este ejemplo:

```text
Employee sends:

192.168.0.1
```

Podemos configurar una regla que:

```text
detecte
notifique
permita
```

Pero si encuentra:

```text
192.168.0.1
172.16.0.1
```

otra regla podría:

```text
detect
block
allow override with justification
alert administrator
```

---

## Qué decir

Durante el curso vamos a construir una política DLP de laboratorio con:

```text
IP Address
```

porque permite practicar:

```text
Detection
Rules
Policy Tips
Blocking
Override
Alerts
```

sin utilizar información sensible real.

---

# 4. Ubicar Information Protection

Buscar:

```text
Solutions
→ Information Protection
```

o la sección equivalente.

Mostrar:

```text
Sensitivity labels
```

No crear etiquetas todavía.

---

# 5. Qué es una Sensitivity Label

Explicar:

Una etiqueta de confidencialidad permite clasificar y proteger información.

Ejemplo:

```text
Public

Internal

Confidential

Highly Confidential
```

---

## Relación conceptual

Mostrar:

```text
Document
   |
   v
Sensitivity Label
   |
   +---- Classification
   |
   +---- Marking
   |
   +---- Protection
   |
   +---- Encryption
```

---

# 6. Ejemplo del curso

Durante el laboratorio utilizaremos una etiqueta como:

```text
PII
```

con elementos visuales como:

```text
Header:
PII - CONFIDENTIAL

Footer:
Contains Personally Identifiable Information

Watermark:
CONFIDENTIAL - PII
```

---

# 7. Diferencia entre DLP y Sensitivity Labels

Explicar de forma simple:

```text
Sensitivity Label
=
¿Qué es este dato?
```

Ejemplo:

```text
Confidential
PII
Internal
```

Mientras que:

```text
DLP
=
¿Qué debemos hacer cuando ese dato
aparece en determinado contexto?
```

Ejemplo:

```text
Warn
Block
Allow override
Alert
```

---

## Analogía

Usar un paquete:

```text
Sensitivity Label
=
la etiqueta pegada en la caja

CONFIDENTIAL
```

Mientras que:

```text
DLP
=
las reglas de transporte

"Esta caja no puede salir
de la organización"
```

---

# 8. Relación con Microsoft 365 Copilot

Explicar:

Copilot trabaja sobre datos a los que el usuario ya tiene acceso.

Por eso debemos pensar en:

```text
Copilot
   |
   v
User permissions
   |
   v
Organizational data
   |
   +---- Sensitivity Labels
   |
   +---- DLP
```

Copilot no reemplaza una mala estrategia de protección de datos.

---

# 9. Ejemplo de oversharing

Plantear este caso:

```text
Salaries.xlsx
```

Tiene permisos para:

```text
All Employees
```

Aunque el archivo debería ser accesible solo por:

```text
HR
Finance
```

---

## Pregunta para la clase

> ¿Cuál es el problema principal?

Respuesta esperada:

```text
Permissions / Oversharing
```

No:

```text
Copilot
```

---

## Mensaje

Copilot puede amplificar la visibilidad de información que ya estaba incorrectamente compartida.

Por eso preparar Copilot también significa revisar:

```text
Permissions
Labels
DLP
Access
```

---

# 10. Mostrar Policies o Solutions

Hacer un recorrido rápido por el portal.

Identificar visualmente:

```text
Data Loss Prevention
Information Protection
Alerts
Policies
Reports
```

No entrar en configuración avanzada.

---

# 11. Qué NO hacer en esta demo

No:

```text
crear una política DLP
publicar etiquetas
activar políticas globales
configurar protección para toda la organización
crear reglas de bloqueo
modificar configuración productiva
```

La configuración práctica se realizará más adelante.

---

# 12. Resultado esperado

El alumno puede responder:

```text
¿Dónde se administra DLP?

¿Dónde están las Sensitivity Labels?

¿Qué diferencia existe entre DLP y Labels?

¿Qué relación tienen con Copilot?
```

---

# 13. Mapa de los tres portales

Mostrar:

```text
Microsoft 365 Admin Center
        |
        v
Users / Groups / Licenses

Microsoft Entra
        |
        v
Identity / Access / Roles

Microsoft Purview
        |
        v
Data Protection / DLP / Labels
```

---

# 14. Mensaje clave

> Preparar Microsoft 365 Copilot no consiste solamente en habilitar una licencia. También debemos preparar identidad, acceso, permisos y protección de la información.

---

# 15. Cierre de Module 01

Hasta aquí tenemos:

```text
Tenant
   |
   v
Users
   |
   v
Groups
   |
   v
Identity
   |
   v
Access
   |
   v
Data Protection
```

---

# 16. Transición

Siguiente etapa:

```text
Module 02
Secure User Access
```

Y comenzaremos a configurar:

```text
MFA
Conditional Access
Sign-in validation
```