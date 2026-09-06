# Module 08 - Review and Course Integration

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Integrar los conceptos de seguridad, cumplimiento y gobierno estudiados durante MS-4002.

El objetivo final no es memorizar portales.

El alumno debe poder analizar una organización y responder:

```text
¿Está preparada para implementar
Microsoft 365 Copilot de forma
segura y gobernada?
```

---

# 2. El recorrido del curso

Durante el curso avanzamos por estas capas:

```text
Microsoft 365 Copilot Readiness
              |
              v
          Identity
              |
              v
        Secure Access
              |
              v
     Roles & Permissions
              |
              v
     Microsoft 365 Apps
              |
              v
             Data
        +-----+-----+
        |           |
       DLP      Sensitivity
                  Labels
        |           |
        +-----+-----+
              |
              v
       Extensibility
              |
              v
          Governance
```

---

# 3. Pregunta inicial

Una empresa dice:

> Compramos Microsoft 365 Copilot. Queremos asignarlo mañana a todos nuestros empleados.

¿Qué debemos preguntar antes?

No empezar por:

```text
¿Cómo asignamos las licencias?
```

Primero debemos analizar:

```text
Identity
Permissions
Apps
Data
Security
Compliance
Governance
```

---

# 4. Caso empresarial - Contoso

Contoso tiene:

```text
2,000 employees

500 SharePoint sites

Microsoft Teams

OneDrive

Exchange Online

Several years of corporate data
```

La dirección quiere implementar Microsoft 365 Copilot para toda la organización.

---

# 5. Situación actual

Durante la evaluación descubrimos:

```text
Some users do not use MFA

Legacy permissions exist

Several administrators are Global Admins

SharePoint contains overshared information

Different Microsoft 365 Apps configurations exist

No consistent DLP strategy

Documents are not consistently classified

Users want to create AI agents
```

Pregunta:

```text
¿Está Contoso preparada?
```

Respuesta:

```text
Not yet
```

---

# 6. Paso 1 - Pilot

No comenzamos con:

```text
2,000 users
```

Creamos:

```text
M365 Copilot Pilot
```

con un grupo controlado de usuarios.

Modelo:

```text
Pilot
  |
  v
Validate
  |
  v
Learn
  |
  v
Govern
  |
  v
Expand
```

---

# 7. Pregunta

¿Por qué utilizar un piloto?

Porque permite:

```text
Reduce risk
Test configuration
Discover problems
Collect feedback
Adjust governance
```

antes del despliegue amplio.

---

# 8. Paso 2 - Identity

Revisamos:

```text
Users
Groups
Authentication
MFA
Sign-in activity
```

Pregunta:

```text
¿Sabemos quién está accediendo?
```

---

# 9. Riesgo encontrado

Contoso todavía utiliza:

```text
Password-only authentication
```

para algunos usuarios.

Antes de ampliar Copilot debemos fortalecer la estrategia de identidad.

---

# 10. Paso 3 - Secure Access

Introducimos:

```text
Conditional Access
```

Modelo:

```text
User
  |
  v
Sign-in
  |
  v
Conditional Access
  |
  v
Evaluate
  |
  +---- Allow
  +---- Require control
  +---- Block
```

---

# 11. Estrategia segura

No comenzamos durante una prueba con:

```text
All Users
+
All Resources
+
Aggressive enforcement
```

Preferimos:

```text
Test Group
+
Controlled Scope
+
Report-only
+
Validation
```

---

# 12. Validación

Después revisamos:

```text
Sign-in logs
```

Pregunta:

> ¿Cómo sabemos qué efecto habría tenido nuestra política?

Respuesta:

```text
Conditional Access evaluation
in Sign-in logs
```

---

# 13. Paso 4 - Roles

Descubrimos que muchos administradores tienen:

```text
Global Administrator
```

aunque solamente realizan tareas específicas.

Aplicamos:

```text
Least Privilege
```

---

# 14. Ejemplo

Antes:

```text
Helpdesk
   |
   v
Global Administrator
```

Después:

```text
Helpdesk
   |
   v
Appropriate limited role
```

---

# 15. Pregunta

¿Qué principio estamos aplicando?

```text
Least Privilege
```

Es decir:

```text
TASK
 |
 v
Required permissions
 |
 v
Appropriate role
```

---

# 16. Paso 5 - Microsoft 365 Apps

Ahora revisamos:

```text
Applications
Versions
Updates
Configuration
```

No queremos que el piloto dependa de un entorno completamente inconsistente.

---

# 17. Estrategia

```text
Inventory
   |
   v
Pilot
   |
   v
Validate
   |
   v
Standardize
   |
   v
Expand
```

---

# 18. Hasta aquí

Ya tenemos:

```text
WHO
 |
 v
Identity

HOW THEY ENTER
 |
 v
Secure Access

WHAT THEY CAN ADMINISTER
 |
 v
Roles

WHERE THEY WORK
 |
 v
Microsoft 365 Apps
```

Ahora llega la información.

---

# 19. Paso 6 - Oversharing

Encontramos:

```text
SharePoint
└── Finance
    └── Salaries.xlsx
```

con permisos demasiado amplios.

Pregunta:

> ¿Debemos intentar solucionar este problema creando una política DLP?

No necesariamente.

El problema inicial es:

```text
Permissions / Oversharing
```

---

# 20. Regla importante

Copilot Readiness no significa solamente agregar nuevos controles.

También significa corregir problemas existentes en:

```text
Permissions
Sharing
Access
Governance
```

---

# 21. Paso 7 - DLP

Ahora aparece otro escenario.

Un empleado tiene permiso legítimo para acceder a información.

Pero intenta compartir información sensible de una forma que la organización desea controlar.

Aquí entra:

```text
Data Loss Prevention
```

---

# 22. Flujo DLP

```text
User activity
     |
     v
Sensitive information
     |
     v
DLP Policy
     |
     +---- Allow
     +---- Notify
     +---- Block
     +---- Override
     +---- Alert
```

---

# 23. Pregunta

¿Qué diferencia existe entre:

```text
Permissions
```

y:

```text
DLP
```

Respuesta conceptual:

```text
Permissions
=
¿Puede acceder?

DLP
=
¿Qué ocurre cuando la información
es utilizada o compartida?
```

---

# 24. Paso 8 - Sensitivity Labels

Contoso tiene:

```text
Public documents
Internal documents
HR information
Financial information
Customer information
```

Pero todos los documentos parecen iguales.

Necesitamos:

```text
Classification
```

---

# 25. Estrategia

Podemos establecer una clasificación como:

```text
Public
Internal
Confidential
Highly Confidential
```

y utilizar:

```text
Sensitivity Labels
```

para implementar esa estrategia.

---

# 26. Flujo

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
     +---- Access controls
     +---- Encryption
```

según la configuración utilizada.

---

# 27. Pregunta clave

¿Cuál es la diferencia entre DLP y Sensitivity Labels?

```text
Sensitivity Labels
=
¿Qué es esta información
y cómo debe clasificarse/protegerse?

DLP
=
¿Qué ocurre cuando información
sensible es utilizada o compartida?
```

---

# 28. Cómo trabajan juntas

```text
Document
   |
   v
Sensitivity Label
   |
   v
User activity
   |
   v
DLP
   |
   +---- Allow
   +---- Notify
   +---- Block
```

---

# 29. Paso 9 - Extensibility

Después del piloto, los departamentos quieren crear:

```text
HR Agent
Finance Agent
Sales Agent
Support Agent
```

La pregunta ya no es solamente:

```text
¿Podemos hacerlo?
```

También:

```text
¿Debemos permitirlo?

¿Quién lo puede utilizar?

¿Qué datos necesita?

¿Qué permisos requiere?

¿Quién lo aprueba?
```

---

# 30. Gobierno de extensibilidad

Modelo:

```text
Agent / App
     |
     v
Security Review
     |
     v
Permissions Review
     |
     v
Data Review
     |
     v
Approval
     |
     v
Pilot
     |
     v
Production
```

---

# 31. Caso final

Contoso quiere crear:

```text
HR Agent
```

Fuentes disponibles:

```text
HR Policies
Employee Handbook
Payroll
Employee Medical Records
Employee Performance Reviews
```

El agente solamente necesita responder preguntas sobre políticas de RRHH.

Pregunta:

> ¿Conectamos las cinco fuentes?

Respuesta esperada:

```text
No
```

Aplicamos:

```text
Purpose
+
Required Data
+
Least Privilege
```

---

# 32. Arquitectura final

```text
                    USER
                      |
                      v
                   IDENTITY
                      |
                      v
                SECURE ACCESS
                      |
                      v
                  PERMISSIONS
                      |
                      v
              MICROSOFT 365 APPS
                      |
                      v
                     DATA
                      |
          +-----------+-----------+
          |                       |
         DLP              SENSITIVITY LABELS
          |                       |
          +-----------+-----------+
                      |
                      v
             COPILOT EXPERIENCE
                      |
                      v
                EXTENSIBILITY
                      |
                      v
                  GOVERNANCE
```

---

# 33. Los cuatro laboratorios

Durante el curso nuestra práctica Standalone sigue este recorrido:

```text
LAB 01
Tenant Preparation
      |
      v
LAB 02
Identity + Access + Roles
      |
      v
LAB 03
DLP
      |
      v
LAB 04
Sensitivity Labels
```

---

# 34. Lab 01

El alumno prepara:

```text
Tenant
+
Pilot Group
+
Microsoft Graph
```

Mensaje:

```text
Prepare the environment
```

---

# 35. Lab 02

El alumno trabaja:

```text
Users
Groups
Conditional Access
MFA
Roles
Least Privilege
Microsoft Graph
```

Mensaje:

```text
Protect identities and privileges
```

---

# 36. Lab 03

El alumno crea:

```text
DLP Policy
```

y experimenta:

```text
Detect
Notify
Block
Override
```

Mensaje:

```text
Control sensitive data activity
```

---

# 37. Lab 04

El alumno crea:

```text
PII Sensitivity Label
```

y trabaja con:

```text
Classification
Content Marking
Protection
Publishing
Justification
```

Mensaje:

```text
Classify and protect information
```

---

# 38. Preguntas rápidas - Identity

Pregunta:

> ¿Authentication y Authorization son lo mismo?

```text
No

Authentication
=
Who are you?

Authorization
=
What can you do?
```

---

# 39. Pregunta rápida - Conditional Access

> ¿Por qué utilizar Report-only?

```text
Evaluate impact
before enforcement
```

---

# 40. Pregunta rápida - Roles

> ¿Qué principio debemos aplicar al asignar privilegios?

```text
Least Privilege
```

---

# 41. Pregunta rápida - DLP

> Un usuario puede acceder legítimamente a un documento pero intenta compartir información sensible. ¿Qué control debemos considerar?

```text
DLP
```

---

# 42. Pregunta rápida - Labels

> ¿Crear una etiqueta significa que automáticamente aparece para todos los usuarios?

```text
No

Create
  |
  v
Publish
  |
  v
Propagate
```

---

# 43. Pregunta rápida - Extensibility

> Un agente técnicamente funciona. ¿Eso significa que debemos desplegarlo a todos?

```text
No

Review
+
Approve
+
Pilot
+
Govern
```

---

# 44. El patrón común

Durante todo el curso apareció repetidamente:

```text
ASSESS
   |
   v
PILOT
   |
   v
VALIDATE
   |
   v
PROTECT
   |
   v
GOVERN
   |
   v
EXPAND
```

Este es uno de los principales mensajes de MS-4002.

---

# 45. Error 1

```text
Assign Copilot licenses
to everyone immediately
```

Problema:

```text
No readiness assessment
```

---

# 46. Error 2

```text
All administrators
=
Global Administrator
```

Problema:

```text
Excessive privilege
```

---

# 47. Error 3

```text
Conditional Access
=
Create aggressive policy
for everyone immediately
```

Problema:

```text
Potential lockout / disruption
```

Mejor:

```text
Controlled scope
+
Report-only
+
Validation
```

---

# 48. Error 4

```text
DLP
=
Block everything
```

Problema:

```text
Business disruption
```

DLP también permite:

```text
Detect
Notify
Educate
Override
Monitor
```

---

# 49. Error 5

```text
Sensitivity Labels
=
Create dozens of classifications
```

Problema:

```text
Complexity
+
User confusion
```

La clasificación debe ser:

```text
Understandable
+
Useful
+
Governable
```

---

# 50. Error 6

```text
Agent works
=
Agent approved
```

Problema:

```text
Technical functionality
!=
Security approval
```

---

# 51. Caso de evaluación final

La empresa Fabrikam quiere implementar Copilot.

Tiene:

```text
1,000 users

No MFA for some users

20 Global Administrators

SharePoint sites shared with Everyone

No DLP policies

No classification strategy

Users already requesting custom agents
```

Pedir a los alumnos que propongan el orden de trabajo.

---

# 52. Respuesta conceptual

Una posible estrategia:

```text
1. Assess environment

2. Define pilot

3. Review identities

4. Secure authentication/access

5. Review privileges

6. Review permissions and oversharing

7. Validate Microsoft 365 Apps

8. Implement information protection

9. Implement DLP

10. Govern extensibility

11. Validate

12. Expand
```

No es simplemente una lista técnica.

Es una estrategia de adopción segura.

---

# 53. Pregunta final

Preguntar:

> ¿Cuál es la primera herramienta que debemos configurar para implementar Copilot de forma segura?

La respuesta que buscamos no es necesariamente el nombre de un portal.

El alumno debería comprender:

```text
Primero debemos evaluar
el entorno Microsoft 365.
```

---

# 54. Mensaje final

> Preparar Microsoft 365 Copilot no consiste únicamente en habilitar una tecnología de IA. Consiste en preparar las identidades, los accesos, los permisos, las aplicaciones y la información sobre los que esa tecnología trabajará.

---

# 55. Modelo para recordar

```text
             COPILOT READINESS

                    DATA
                     |
         +-----------+-----------+
         |                       |
    CLASSIFICATION            CONTROL
         |                       |
       LABELS                    DLP
         |                       |
         +-----------+-----------+
                     |
                PERMISSIONS
                     |
                  ACCESS
                     |
                 IDENTITY
                     |
                   USER

              GOVERN EVERYTHING
```

---

# 56. Cierre del curso

El alumno debería finalizar MS-4002 pudiendo explicar:

```text
Why identity matters

Why MFA and Conditional Access matter

Why least privilege matters

Why Microsoft 365 Apps matter

Why oversharing matters

Why DLP matters

Why Sensitivity Labels matter

Why extensibility requires governance
```

Resultado:

```text
Microsoft 365
      |
      v
Secure
      |
      v
Governed
      |
      v
Ready for Copilot
```