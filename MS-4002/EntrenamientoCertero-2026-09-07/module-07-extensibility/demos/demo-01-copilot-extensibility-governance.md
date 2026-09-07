
# DEMO 01 - Copilot Extensibility and Governance

## MS-4002 - Module 07: Microsoft 365 Copilot Extensibility

---

## Duración

15 a 20 minutos

## Tipo

DEMO INSTRUCTOR - CONCEPTUAL + PORTAL ORIENTATION

## Portales

```text
Microsoft 365 Admin Center
https://admin.microsoft.com

Microsoft Entra Admin Center
https://entra.microsoft.com
```

---

# Objetivo

Mostrar cómo Microsoft 365 Copilot puede extenderse mediante diferentes componentes y explicar por qué cada extensión agrega una nueva superficie de gobierno.

El objetivo NO es construir un agente completo.

El alumno debe comprender:

```text
Copilot
   ↓
Extension
   ↓
Data / Actions / Permissions
   ↓
Governance
```

---

# Escenario

Contoso ya preparó:

```text
Identity
Secure access
Roles
Apps
DLP
Sensitivity Labels
```

Ahora desea ampliar Copilot con:

```text
Agents
Apps
Connectors
Custom solutions
```

La pregunta ya no es solamente:

```text
¿Qué puede hacer Copilot?
```

Ahora también debemos preguntar:

```text
¿Quién creó la extensión?

¿Quién puede usarla?

¿Qué datos utiliza?

¿Qué acciones puede ejecutar?

¿Qué permisos necesita?

¿Quién la aprobó?
```

---

# 1. Introducir extensibilidad

Explicar:

Microsoft 365 Copilot puede ampliarse para trabajar con:

```text
organizational knowledge

business processes

external systems

specialized agents
```

---

# 2. Modelo mental

Mostrar:

```text
Microsoft 365 Copilot
        |
        +---- Agents
        |
        +---- Apps
        |
        +---- Connectors
        |
        +---- Custom solutions
```

La terminología y experiencias pueden evolucionar, pero el principio de gobierno permanece.

---

# 3. Ejemplo simple

Una empresa crea un:

```text
HR Agent
```

que responde preguntas sobre:

```text
Vacation policy

Benefits

Internal procedures

Onboarding
```

La pregunta importante es:

```text
¿De dónde obtiene esa información?
```

---

# 4. Fuentes de conocimiento

El agente podría utilizar:

```text
SharePoint

Microsoft 365 data

Connected systems

Custom data sources
```

---

# 5. Riesgo principal

Si conectamos una fuente de datos:

```text
Copilot
   ↓
Agent
   ↓
Data source
```

también debemos revisar:

```text
permissions
access
data quality
sensitivity
ownership
```

---

# 6. Conectar con lo aprendido

Mostrar:

```text
Bad permissions
      ↓
Oversharing
      ↓
Agent / Copilot can surface
what the user already has access to
```

Por eso extensibilidad no elimina los controles anteriores.

Los hace todavía más importantes.

---

# 7. Abrir Microsoft 365 Admin Center

Entrar a:

```text
https://admin.microsoft.com
```

No realizar cambios.

Utilizar el portal únicamente para orientar al alumno sobre administración y gobierno del entorno Microsoft 365.

---

# 8. Explicar gobierno de extensiones

Cada extensión debería pasar por preguntas como:

```text
Who owns it?

Who approves it?

Who can use it?

What data can it access?

What actions can it perform?

How is it monitored?

How is it retired?
```

---

# 9. Ejemplo de agente de Recursos Humanos

Mostrar conceptualmente:

```text
HR Agent
   |
   +--> Employee handbook
   |
   +--> Vacation policies
   |
   +--> Benefits information
```

El agente podría ser útil.

Pero debemos evitar conectarlo innecesariamente a:

```text
Payroll

Medical records

Executive salaries

Disciplinary records
```

si no existe una necesidad legítima.

---

# 10. Least Privilege aplicado a agentes

Conectar con Module 03:

```text
User
→ Least Privilege
```

también aplica a:

```text
Agent
→ Least Privilege
```

Una extensión debe tener:

```text
only the permissions
required for its function
```

---

# 11. Extensión con acciones

Explicar que algunas extensiones pueden no limitarse a leer información.

También pueden ejecutar acciones.

Ejemplo:

```text
Support Agent
   ↓
Create ticket
```

o:

```text
HR Agent
   ↓
Start onboarding process
```

---

# 12. Riesgo de acciones

Comparar:

```text
READ
```

con:

```text
WRITE / EXECUTE
```

Una acción puede modificar sistemas.

Por eso necesita mayor control.

---

# 13. Ejemplo

Un agente que responde:

```text
¿Cuántos días de vacaciones tengo?
```

es distinto de uno que puede:

```text
aprobar vacaciones
```

---

# 14. Identidad

Toda interacción debe considerar:

```text
Who is the user?
```

Conectar con:

```text
Microsoft Entra ID
```

---

# 15. Abrir Microsoft Entra

Entrar a:

```text
https://entra.microsoft.com
```

Mostrar áreas como:

```text
Users
Groups
Enterprise applications
App registrations
Roles
```

No modificar nada.

---

# 16. Enterprise Applications

Mostrar:

```text
Enterprise applications
```

Explicar conceptualmente que aplicaciones integradas pueden tener:

```text
Permissions

Users / Groups

Consent

Sign-in activity
```

---

# 17. App Registrations

Mostrar:

```text
App registrations
```

Explicar que las soluciones personalizadas pueden depender de identidades de aplicación.

No crear ninguna.

---

# 18. Permisos de aplicación

Explicar:

Una aplicación o solución puede solicitar permisos.

Ejemplo conceptual:

```text
Read user profile
```

es muy diferente de:

```text
Read all files
```

---

# 19. Admin Consent

Explicar:

Algunos permisos pueden requerir:

```text
Administrator consent
```

Esto representa un punto de gobierno importante.

---

# 20. Pregunta para la clase

> Si una aplicación solicita acceso a todos los archivos de la organización, ¿debemos aprobarla simplemente porque el proveedor es conocido?

Respuesta:

```text
No.
```

Primero debemos evaluar:

```text
business need
permissions
scope
risk
data
owner
```

---

# 21. Connectors

Explicar conceptualmente:

Un connector puede ampliar el conocimiento disponible.

Ejemplo:

```text
Copilot
   ↓
Connector
   ↓
External knowledge source
```

---

# 22. Riesgos de connectors

Preguntar:

```text
What data enters?

Who can discover it?

Who maintains it?

How fresh is it?

Does it contain sensitive information?
```

---

# 23. Calidad de datos

Gobierno no significa solamente seguridad.

También debemos pensar en:

```text
accuracy

ownership

freshness

duplication

obsolete content
```

---

# 24. Ejemplo

Conectar una base documental con:

```text
policies from 2019
```

puede producir una experiencia técnicamente correcta pero operacionalmente equivocada.

---

# 25. Shadow AI

Introducir el concepto:

```text
Shadow AI
```

como uso de herramientas o soluciones de IA fuera del gobierno establecido por la organización.

Ejemplo:

```text
Employee creates agent
        ↓
Connects sensitive data
        ↓
No review
        ↓
No owner
        ↓
No monitoring
```

---

# 26. Qué busca el gobierno

El objetivo no es:

```text
block all innovation
```

El objetivo es:

```text
enable innovation safely
```

---

# 27. Modelo de ciclo de vida

Mostrar:

```text
Request
   ↓
Review
   ↓
Approve
   ↓
Pilot
   ↓
Monitor
   ↓
Production
   ↓
Review
   ↓
Retire
```

---

# 28. Request

Preguntas:

```text
Who needs it?

Why?

What problem does it solve?
```

---

# 29. Review

Revisar:

```text
Data

Permissions

Actions

Risk

Ownership
```

---

# 30. Approval

Definir:

```text
Who is accountable?
```

---

# 31. Pilot

Conectar con Module 01:

```text
Small audience
      ↓
Validate
      ↓
Expand
```

---

# 32. Monitor

Preguntar:

```text
Who uses it?

What does it access?

Does it generate errors?

Does its scope change?
```

---

# 33. Production

Solo después de:

```text
validated behavior
approved permissions
defined ownership
```

---

# 34. Retirement

Toda extensión debe poder retirarse.

Preguntar:

```text
What happens when the owner leaves?

What happens when the process changes?

What happens when the data source disappears?
```

---

# 35. Ejemplo empresarial completo

Contoso desea un:

```text
Sales Agent
```

que accede a:

```text
Product catalog

Sales procedures

Customer FAQ
```

Proceso recomendado:

```text
Business owner
      ↓
Data review
      ↓
Permission review
      ↓
Pilot sales team
      ↓
Monitoring
      ↓
Production
```

---

# 36. Ejemplo de mala implementación

```text
Create agent
      ↓
Connect everything
      ↓
Give access to everyone
      ↓
No owner
      ↓
No monitoring
```

---

# 37. Relación con DLP

Una extensión puede trabajar con información sensible.

Por eso:

```text
Extensibility
   +
DLP
```

deben pensarse juntos.

---

# 38. Relación con Sensitivity Labels

Una extensión también puede encontrarse con contenido clasificado.

Por eso:

```text
Extensibility
   +
Sensitivity Labels
```

forman parte del mismo modelo de gobierno.

---

# 39. Relación con Conditional Access

El acceso a servicios conectados también depende de:

```text
Identity

Authentication

Conditional Access
```

---

# 40. Relación con Roles

Administrar extensiones requiere:

```text
appropriate administrative roles
```

No todos necesitan:

```text
Global Administrator
```

---

# 41. Mapa integrador

Mostrar:

```text
                 COPILOT
                    |
         +----------+----------+
         |                     |
      Identity               Data
         |                     |
      Entra ID          Permissions
         |                     |
         |               DLP / Labels
         |                     |
         +----------+----------+
                    |
              Extensibility
                    |
          Agents / Apps /
          Connectors / Actions
                    |
                Governance
```

---

# 42. Preguntas de gobierno

Antes de aprobar cualquier extensión:

```text
1. Who owns it?

2. Who can use it?

3. What data does it access?

4. What actions can it perform?

5. What permissions does it require?

6. Who approved it?

7. How will it be monitored?

8. How will it be retired?
```

---

# 43. Qué NO hacer en esta demo

No:

```text
create production agents

grant admin consent

approve unknown applications

change enterprise application permissions

connect real sensitive data

register applications unnecessarily
```

---

# 44. Resultado esperado

El alumno debe entender:

```text
Extensibility
≠
Only functionality
```

También significa:

```text
new data access

new permissions

new actions

new governance responsibilities
```

---

# 45. Mensaje clave

> Cada vez que extendemos Copilot, extendemos también la superficie que debemos gobernar.

---

# 46. Transición

Siguiente módulo:

```text
Module 08
Final Review
```

Ahí integraremos:

```text
Identity

Secure Access

Roles

Apps

DLP

Sensitivity Labels

Extensibility
```

en un único modelo de readiness para Microsoft 365 Copilot.
