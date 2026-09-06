# Module 01 - Microsoft 365 Copilot Readiness

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Comprender qué debe preparar una organización antes de implementar Microsoft 365 Copilot.

La idea principal es:

```text
Copilot no se implementa sobre un entorno vacío.

Copilot utiliza el entorno Microsoft 365
que la organización ya tiene.
```

Por lo tanto, antes de desplegar Copilot debemos revisar:

```text
Identity
   +
Licensing
   +
Microsoft 365 Apps
   +
Permissions
   +
Information
   +
Security
   +
Compliance
```

---

# 2. Pregunta para iniciar la clase

Preguntar a los alumnos:

> Si mañana nuestra empresa compra Microsoft 365 Copilot para 500 usuarios, ¿lo primero que deberíamos hacer es asignar las 500 licencias?

Utilizar la discusión para introducir el concepto de:

```text
Copilot Readiness
```

El objetivo no es solamente habilitar una licencia.

Primero debemos conocer el entorno sobre el cual trabajará Copilot.

---

# 3. Explicación simple

Microsoft 365 Copilot utiliza los servicios existentes de Microsoft 365.

Conceptualmente:

```text
Microsoft 365
    |
    +---- Exchange
    |
    +---- SharePoint
    |
    +---- OneDrive
    |
    +---- Teams
    |
    +---- Microsoft Graph
    |
    v
Microsoft 365 Copilot
```

Copilot puede utilizar información a la que el usuario ya tiene acceso dentro de Microsoft 365.

---

# 4. Analogía

Imagina que Copilot es un nuevo empleado extremadamente rápido.

El empleado llega a una empresa donde existen:

```text
10 años de documentos
miles de correos
cientos de Teams
SharePoint
OneDrive
grupos
permisos
```

Antes de permitirle comenzar a trabajar debemos preguntarnos:

```text
¿Quién puede acceder a qué?

¿Los permisos están correctamente configurados?

¿Tenemos información sensible expuesta?

¿Los usuarios están correctamente protegidos?

¿Los documentos están clasificados?
```

Copilot no reemplaza estos controles.

Trabaja sobre ellos.

---

# 5. El principio fundamental

El modelo conceptual del curso será:

```text
USER
  |
  v
IDENTITY
  |
  v
PERMISSIONS
  |
  v
MICROSOFT 365 DATA
  |
  v
COPILOT
```

Por eso un problema de permisos existente puede convertirse en un problema mucho más visible cuando incorporamos herramientas de IA.

---

# 6. Ejemplo real

Supongamos que existe este archivo:

```text
SharePoint
└── Finance
    └── Salaries.xlsx
```

Por error:

```text
All Employees = Read
```

Antes de Copilot, un empleado podría no saber que el archivo existe.

Sin embargo, el problema ya existe:

```text
Empleado
   |
   v
Tiene permiso
   |
   v
Puede acceder
```

La incorporación de herramientas capaces de descubrir y resumir información hace todavía más importante revisar esos permisos.

El problema principal no es:

```text
Copilot
```

El problema es:

```text
Oversharing
```

---

# 7. Concepto de Oversharing

Oversharing ocurre cuando información está disponible para más usuarios de los que realmente deberían acceder a ella.

Ejemplos:

```text
SharePoint site
    |
    v
Everyone

OneDrive folder
    |
    v
Large group

Teams
    |
    v
Incorrect membership
```

Antes de implementar Copilot debemos revisar estas situaciones.

---

# 8. Qué debemos preparar

Podemos dividir Copilot Readiness en varias capas.

```text
COPILOT READINESS
       |
       +---- Licensing
       |
       +---- Identity
       |
       +---- Access
       |
       +---- Permissions
       |
       +---- Apps
       |
       +---- Information Protection
       |
       +---- Governance
```

Estas capas aparecerán nuevamente durante todo el curso.

---

# 9. Licensing

Antes de asignar licencias debemos conocer:

- quién utilizará Copilot;
- qué servicios Microsoft 365 utiliza;
- qué aplicaciones necesita;
- si cumple los requisitos correspondientes.

La estrategia recomendada para una adopción controlada es comenzar con:

```text
Pilot users
```

en lugar de:

```text
Entire organization
```

---

# 10. Analogía del piloto

No desplegamos una nueva tecnología a toda una organización sin probarla.

Es similar a implementar una nueva aplicación:

```text
DEV
 |
 v
TEST
 |
 v
PILOT
 |
 v
PRODUCTION
```

Para Copilot podemos pensar:

```text
Small Pilot
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

# 11. Grupo piloto

Durante el curso utilizaremos conceptualmente:

```text
M365 Copilot Pilot
```

Este grupo representa a los usuarios seleccionados para probar la implementación.

Puede utilizarse para organizar:

- usuarios piloto;
- pruebas;
- configuración;
- validaciones;
- despliegue gradual.

---

# 12. Identity

Antes de Copilot debemos revisar las identidades.

Preguntas importantes:

```text
¿Los usuarios correctos tienen acceso?

¿Utilizamos MFA?

¿Tenemos cuentas administrativas protegidas?

¿Existen cuentas antiguas?

¿Los grupos están correctamente administrados?
```

Esto conecta directamente con:

```text
Module 02 - Secure Access
```

---

# 13. Permissions

También debemos revisar:

```text
Who can access what?
```

Ejemplos:

- SharePoint permissions;
- OneDrive sharing;
- Teams membership;
- Microsoft 365 Groups;
- administrative roles.

Esto conecta con:

```text
Module 03 - Roles and Permissions
```

---

# 14. Microsoft 365 Apps

Los usuarios interactuarán con Copilot desde aplicaciones y experiencias Microsoft 365 compatibles.

Por ello debemos considerar:

```text
Apps
Updates
Deployment
Configuration
```

Esto conecta con:

```text
Module 04 - Microsoft 365 Apps
```

---

# 15. Information Protection

Después debemos preguntarnos:

```text
¿Qué información tenemos?
```

y:

```text
¿Qué información es sensible?
```

Microsoft Purview proporciona capacidades para ayudar a:

```text
Discover
Classify
Protect
Monitor
```

---

# 16. DLP

Data Loss Prevention ayuda a controlar cómo se utiliza y comparte información sensible.

Ejemplo:

```text
User
 |
 v
Email
 |
 v
Sensitive Information
 |
 v
DLP
 |
 +---- Allow
 +---- Notify
 +---- Block
 +---- Override
```

Esto será trabajado en:

```text
Module 05
Lab 03
```

---

# 17. Sensitivity Labels

Sensitivity Labels permiten clasificar y proteger información.

Ejemplo:

```text
Document
   |
   v
PII
   |
   +---- Classification
   +---- Marking
   +---- Encryption
   +---- Access Control
```

Esto será trabajado en:

```text
Module 06
Lab 04
```

---

# 18. Extensibility

Copilot también puede ampliarse mediante agentes, aplicaciones y otras capacidades.

Esto introduce otra pregunta:

```text
¿Quién puede extender Copilot
y bajo qué controles?
```

Esto será trabajado en:

```text
Module 07
```

---

# 19. Modelo completo

Presentar este modelo durante la clase:

```text
                MICROSOFT 365 COPILOT
                         |
        +----------------+----------------+
        |                |                |
     Identity         Permissions        Data
        |                |                |
       MFA           SharePoint         Purview
        |             OneDrive           |
 Conditional Access    Teams          DLP / Labels
        |                |                |
        +----------------+----------------+
                         |
                         v
                     GOVERNANCE
```

---

# 20. DEMO INSTRUCTOR - Microsoft 365 Admin Center

## Objetivo

No realizar todavía una configuración compleja.

Simplemente mostrar dónde vive el entorno que estamos preparando.

Abrir:

```text
Microsoft 365 Admin Center
```

Mostrar:

```text
Users
Teams & groups
Billing
Settings
Health
Admin centers
```

Explicar:

```text
Este es el entorno sobre el que posteriormente
trabajará Microsoft 365 Copilot.
```

---

# 21. DEMO INSTRUCTOR - Admin Centers

Desde Microsoft 365 Admin Center mostrar:

```text
Admin centers
```

y explicar que durante el curso utilizaremos principalmente:

```text
Microsoft 365
Microsoft Entra
Microsoft Purview
```

No es necesario configurar nada todavía.

---

# 22. Mapa de portales del curso

```text
Microsoft 365 Admin Center
        |
        +---- Users
        +---- Groups
        +---- Licensing
        |
        v
Microsoft Entra
        |
        +---- Identity
        +---- MFA
        +---- Conditional Access
        +---- Roles
        |
        v
Microsoft Purview
        |
        +---- DLP
        +---- Information Protection
        +---- Sensitivity Labels
```

---

# 23. Relación con Lab 01

Este módulo prepara conceptualmente:

```text
Standalone Lab 01
Initialize Microsoft 365 Tenant
```

En el laboratorio el alumno:

```text
Accede al tenant
       |
       v
Revisa Admin Center
       |
       v
Crea grupo piloto
       |
       v
Prepara Microsoft Graph
```

---

# 24. Qué NO hacer todavía

Durante este módulo no es necesario:

- configurar Conditional Access;
- modificar Smart Lockout;
- asignar roles administrativos;
- crear DLP;
- crear Sensitivity Labels.

Esas actividades pertenecen a módulos posteriores.

---

# 25. Pregunta de comprobación

Preguntar:

> Si Copilot muestra a un empleado información que ese empleado ya tenía permiso para leer, ¿el primer problema que debemos investigar es Copilot o los permisos existentes?

Respuesta conceptual esperada:

```text
Permissions / Oversharing
```

---

# 26. Caso práctico

Empresa:

```text
Contoso
```

Situación:

```text
2,000 employees
500 SharePoint sites
Several years of documents
Multiple Teams
Legacy permissions
```

La dirección quiere habilitar Copilot para todos.

Preguntar:

```text
¿Lo hacemos mañana?
```

La respuesta debería conducir a:

```text
No directamente.

Pilot
   |
   v
Assess
   |
   v
Secure
   |
   v
Govern
   |
   v
Deploy
```

---

# 27. Mensaje clave del módulo

El alumno debe recordar:

> Preparar Microsoft 365 Copilot no comienza con Copilot. Comienza preparando Microsoft 365.

---

# 28. Transición al siguiente módulo

Cerrar con:

```text
Ya sabemos QUÉ debemos preparar.

Ahora necesitamos comenzar por QUIÉN puede acceder.
```

Siguiente módulo:

```text
Module 02
Secure User Access
```

donde trabajaremos:

```text
Identity
MFA
Conditional Access
Smart Lockout
Password Protection
```