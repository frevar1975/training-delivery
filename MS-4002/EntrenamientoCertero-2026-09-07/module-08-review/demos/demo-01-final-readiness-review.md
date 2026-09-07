
# DEMO 01 - Final Microsoft 365 Copilot Readiness Review

## MS-4002 - Module 08: Final Review

---

## Duración

20 a 25 minutos

## Tipo

DEMO INSTRUCTOR - REPASO INTEGRADOR

---

# Objetivo

Cerrar el curso integrando los controles principales revisados durante MS-4002 y mostrar cómo se relacionan para preparar una organización antes de implementar Microsoft 365 Copilot.

El objetivo no es revisar cada portal nuevamente.

El objetivo es responder:

```text
¿Qué debería revisar una organización
antes de ampliar el uso de Copilot?
```

---

# Escenario final

Contoso tiene:

```text
2,000 employees

Microsoft 365

SharePoint

OneDrive

Teams

Microsoft Entra ID
```

La empresa quiere desplegar Microsoft 365 Copilot.

Dirección pregunta:

```text
¿Estamos preparados?
```

---

# 1. No empezar por Copilot

Explicar:

El error sería comenzar con:

```text
Enable Copilot
```

sin revisar previamente:

```text
Identity

Access

Permissions

Applications

Data

Compliance

Extensibility
```

---

# 2. Modelo completo de readiness

Mostrar:

```text
Microsoft 365 Copilot
        |
        v
+-------------------------+
| Identity                |
+-------------------------+
        |
        v
+-------------------------+
| Secure Access           |
+-------------------------+
        |
        v
+-------------------------+
| Roles & Permissions     |
+-------------------------+
        |
        v
+-------------------------+
| Microsoft 365 Apps      |
+-------------------------+
        |
        v
+-------------------------+
| Data Protection         |
| DLP + Labels            |
+-------------------------+
        |
        v
+-------------------------+
| Extensibility           |
+-------------------------+
        |
        v
+-------------------------+
| Governance              |
+-------------------------+
```

---

# 3. Module 01 - Copilot Readiness

Pregunta:

> ¿Cuál es el primer error que una organización debería evitar?

Respuesta:

```text
Pensar que Copilot readiness
es solamente asignar licencias.
```

Antes debemos revisar:

```text
Users

Licenses

Apps

Permissions

Data

Security

Compliance
```

---

# 4. Pilot deployment

Recordar:

```text
Small pilot
   ↓
Validate
   ↓
Learn
   ↓
Expand
```

---

# 5. Escenario

Contoso tiene 2,000 usuarios.

No comenzar con:

```text
2,000 users
```

Comenzar con:

```text
Pilot group
```

por ejemplo:

```text
50 selected users
```

---

# 6. Module 02 - Secure Access

Pregunta:

> ¿Cómo protegemos el acceso?

Respuesta:

```text
Microsoft Entra ID

MFA

Conditional Access

Sign-in Logs

Smart Lockout

Password Protection
```

---

# 7. Modelo

```text
User
  ↓
Authentication
  ↓
Conditional Access
  ↓
Microsoft 365
```

---

# 8. Error común

Evitar:

```text
CA Policy
→ All users
→ All resources
→ Enable immediately
```

en un entorno sin pruebas.

---

# 9. Estrategia correcta

```text
Test Group
    ↓
Report-only
    ↓
Validate Sign-ins
    ↓
Controlled Enablement
```

---

# 10. Laboratorio relacionado

```text
LAB 02A
```

donde usamos:

```text
CA-MFA-Lab

LAB - Require MFA
```

---

# 11. Module 03 - Roles and Permissions

Pregunta:

> ¿Todos los administradores necesitan Global Administrator?

Respuesta:

```text
No.
```

Aplicar:

```text
Least Privilege
```

---

# 12. Ejemplo

Diego trabaja en soporte.

Necesita:

```text
Helpdesk Administrator
```

No:

```text
Global Administrator
```

---

# 13. Direct assignment vs Role Group

Mostrar:

```text
User
  ↓
Role
```

frente a:

```text
User
  ↓
Role-assignable Group
  ↓
Role
```

---

# 14. Mensaje importante

```text
Administrative role
≠
Content permission
```

Tener un rol administrativo no significa automáticamente tener acceso a todos los documentos empresariales.

---

# 15. Module 04 - Microsoft 365 Apps

Pregunta:

> ¿Qué necesita el usuario para trabajar correctamente con Copilot?

Revisar:

```text
Licensing

Supported Apps

Updates

Configuration

Deployment

Service health
```

---

# 16. Web Apps

En laboratorios:

```text
Word for the web

Outlook on the web

SharePoint

OneDrive
```

son útiles porque reducen dependencia de configuraciones locales.

---

# 17. Module 05 - DLP

Pregunta:

> ¿Qué hacemos cuando detectamos información sensible?

Microsoft Purview DLP permite:

```text
Detect
   ↓
Evaluate
   ↓
Notify / Restrict / Block
```

---

# 18. Modelo DLP

```text
WHERE?
WHAT?
WHEN?
THEN?
```

---

# 19. Nuestro laboratorio

Creamos conceptualmente:

```text
IP Address DLP Policy
```

con:

```text
Single IP Address Rule

Multiple IP Address Rule
```

---

# 20. Primera prueba

Contenido:

```text
192.168.0.1
```

Resultado esperado:

```text
Notify
Allow
```

---

# 21. Segunda prueba

Contenido:

```text
192.168.0.1

172.16.0.1
```

Resultado esperado:

```text
Policy Tip

Block / Restrict

Possible override

Alert
```

según la configuración del laboratorio.

---

# 22. Estrategia DLP

No comenzar directamente con bloqueo severo.

Mejor:

```text
Detect
   ↓
Notify
   ↓
Restrict
   ↓
Block
```

---

# 23. Module 06 - Sensitivity Labels

Pregunta:

> ¿Cómo clasificamos un documento?

Respuesta:

```text
Sensitivity Label
```

---

# 24. Ejemplo

Creamos:

```text
PII
```

con:

```text
Header

Footer

Watermark

Protection
```

---

# 25. Create vs Publish

Recordar:

```text
CREATE LABEL
≠
PUBLISH LABEL
```

---

# 26. Flujo completo

```text
Create PII
    ↓
Configure
    ↓
Publish
    ↓
PII Policy
    ↓
Carlos + Laura
    ↓
Word
    ↓
Apply PII
```

---

# 27. DLP vs Label

Mostrar:

```text
DLP
→ controls activity
```

```text
Sensitivity Label
→ classifies and protects content
```

---

# 28. Trabajan juntos

```text
Sensitive Data
    |
    +---- DLP ----> Control
    |
    +---- Label --> Classification / Protection
```

---

# 29. Module 07 - Extensibility

Pregunta:

> ¿Qué cambia cuando extendemos Copilot?

Respuesta:

Aparecen nuevas superficies:

```text
Data

Permissions

Actions

Applications

Connectors

Agents
```

---

# 30. Ejemplo

```text
HR Agent
   ↓
SharePoint policies
```

Puede ser razonable.

Pero:

```text
HR Agent
   ↓
Payroll + Medical Records
```

requiere una revisión mucho más estricta.

---

# 31. Gobernanza

Antes de aprobar una extensión preguntar:

```text
Who owns it?

Who uses it?

What data does it access?

What actions can it perform?

What permissions does it need?

Who approved it?

How is it monitored?

How is it retired?
```

---

# 32. Lifecycle

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
Retire
```

---

# 33. Caso final Contoso

Situación:

```text
2,000 employees

Copilot deployment planned

Many SharePoint sites

Different admin teams

Sensitive HR and finance content

Multiple business apps
```

---

# 34. Problema 1 - Oversharing

Descubrimos:

```text
Salaries.xlsx
```

en un sitio accesible a más personas de las necesarias.

Pregunta:

> ¿Copilot creó el problema?

Respuesta:

```text
No.
```

El problema ya existía:

```text
permissions / oversharing
```

---

# 35. Acción recomendada

```text
Review permissions

Reduce access

Apply appropriate labels

Consider DLP
```

antes de ampliar Copilot.

---

# 36. Problema 2 - Admin permissions

Hay 18 usuarios con:

```text
Global Administrator
```

Pregunta:

> ¿Qué deberíamos hacer?

Respuesta:

```text
Review roles

Apply least privilege

Reduce unnecessary privilege
```

---

# 37. Problema 3 - Weak access controls

Solo algunos usuarios utilizan MFA.

Acción:

```text
Pilot Conditional Access

Require MFA

Review sign-in risk and logs
```

---

# 38. Problema 4 - Sensitive documents

HR almacena documentos con PII.

Acción:

```text
Sensitivity Labels

DLP

Access review
```

---

# 39. Problema 5 - New Sales Agent

Ventas solicita un agente conectado a:

```text
CRM

SharePoint

Customer records
```

Antes de aprobarlo revisar:

```text
Owner

Business purpose

Data

Permissions

Actions

Monitoring
```

---

# 40. Orden recomendado

Mostrar:

```text
1. Identity

2. Access

3. Permissions

4. Apps

5. Data

6. Protection

7. Extensibility

8. Governance
```

---

# 41. Checklist rápido

Antes del despliegue revisar:

```text
[ ] Users identified

[ ] Licenses planned

[ ] Pilot group defined

[ ] MFA / CA reviewed

[ ] Admin roles reviewed

[ ] Permissions reviewed

[ ] M365 Apps ready

[ ] Sensitive data understood

[ ] DLP strategy defined

[ ] Sensitivity labels defined

[ ] Extensions governed

[ ] Monitoring defined
```

---

# 42. Pregunta final 1

> Tenemos Copilot licenses. ¿Estamos listos?

Respuesta:

```text
Not necessarily.
```

Licensing es solamente una parte.

---

# 43. Pregunta final 2

> Copilot muestra un documento que un usuario podía abrir previamente. ¿Cuál es el primer lugar que debemos investigar?

Respuesta:

```text
Permissions / sharing
```

---

# 44. Pregunta final 3

> ¿Qué control usarías para exigir MFA según determinadas condiciones?

Respuesta:

```text
Conditional Access
```

---

# 45. Pregunta final 4

> ¿Qué principio usamos para asignar roles administrativos?

Respuesta:

```text
Least Privilege
```

---

# 46. Pregunta final 5

> ¿Qué herramienta puede controlar la actividad cuando detecta información sensible?

Respuesta:

```text
Microsoft Purview DLP
```

---

# 47. Pregunta final 6

> ¿Qué utilizamos para clasificar y proteger documentos?

Respuesta:

```text
Sensitivity Labels
```

---

# 48. Pregunta final 7

> ¿Qué ocurre cuando agregamos un agente o connector?

Respuesta:

```text
We extend both capability
and governance surface.
```

---

# 49. Mapa de los laboratorios

```text
LAB 01
Tenant readiness
      ↓

LAB 02
Identity + Security + Roles
      ↓

LAB 03
DLP
      ↓

LAB 04
Sensitivity Labels
```

---

# 50. Mapa del curso

```text
Module 01
Readiness

Module 02
Secure Access

Module 03
Roles

Module 04
Apps

Module 05
DLP

Module 06
Sensitivity Labels

Module 07
Extensibility

Module 08
Review
```

---

# 51. Mensaje central del curso

Microsoft 365 Copilot readiness no es un producto aislado.

Es la combinación de:

```text
Microsoft Entra

Microsoft 365

Microsoft Purview

Permissions

Security

Compliance

Governance
```

---

# 52. Frase de cierre

> Una implementación segura de Microsoft 365 Copilot comienza antes de activar Copilot: comienza con identidad, permisos, protección de datos y gobierno.

---

# 53. Resultado final

Al finalizar MS-4002, el alumno debería poder analizar una organización y responder:

```text
Who has access?

Why do they have access?

What data exists?

How is it protected?

What can applications and agents access?

Who governs the environment?
```

---

# Fin del curso

```text
IDENTITY
   +
ACCESS
   +
PERMISSIONS
   +
DATA PROTECTION
   +
GOVERNANCE
        =
MICROSOFT 365 COPILOT READINESS
```
