# Module 03 - Roles and Permissions

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Comprender cómo administrar privilegios administrativos en Microsoft 365 y Microsoft Entra aplicando el principio de mínimo privilegio.

En el módulo anterior respondimos:

```text
¿QUIÉN puede entrar?
```

Ahora responderemos:

```text
¿QUÉ puede hacer después de entrar?
```

Modelo:

```text
Identity
   |
   v
Authentication
   |
   v
Authorization
   |
   v
Roles & Permissions
```

---

# 2. Punto de partida

Autenticar correctamente a un usuario no significa que deba tener acceso administrativo ilimitado.

Ejemplo:

```text
User authenticated successfully
              |
              v
       What can they do?
              |
              v
           ROLES
```

---

# 3. Analogía

Imagina un hotel.

Una persona puede demostrar quién es en recepción.

Eso no significa que su tarjeta pueda abrir:

```text
todas las habitaciones
+
caja fuerte
+
oficinas
+
sala de servidores
```

La identidad responde:

```text
¿Quién eres?
```

Los permisos responden:

```text
¿A dónde puedes entrar
y qué puedes hacer?
```

---

# 4. Authorization

Authorization determina qué acciones puede realizar una identidad después de autenticarse.

Modelo:

```text
Authentication
      |
      v
User verified
      |
      v
Authorization
      |
      v
Allowed actions
```

---

# 5. Roles administrativos

Microsoft 365 y Microsoft Entra utilizan roles para delegar capacidades administrativas.

Ejemplos que veremos:

```text
Global Administrator

User Administrator

Billing Administrator

Helpdesk Administrator
```

Cada uno tiene diferentes responsabilidades.

---

# 6. El problema del Global Administrator

Una práctica incorrecta sería:

```text
Necesita administrar algo
        |
        v
Global Administrator
```

Esto concede muchos más privilegios de los necesarios.

---

# 7. Principio de mínimo privilegio

El principio fundamental es:

```text
Least Privilege
```

Es decir:

> Otorgar únicamente los permisos necesarios para realizar una tarea.

Modelo:

```text
TASK
 |
 v
Required permissions
 |
 v
Appropriate role
```

No:

```text
TASK
 |
 v
Global Administrator
```

---

# 8. Analogía del mínimo privilegio

Un técnico necesita reparar el aire acondicionado de una oficina.

No necesita:

```text
llave de todas las oficinas
+
acceso a la bóveda
+
acceso al datacenter
+
acceso a Recursos Humanos
```

Necesita solamente el acceso requerido para realizar su trabajo.

---

# 9. Ejemplo empresarial

Responsabilidad:

```text
Administrar facturación
```

Pregunta:

```text
¿Necesita Global Administrator?
```

No necesariamente.

Podemos evaluar un rol más específico:

```text
Billing Administrator
```

---

# 10. Ejemplo - User Administrator

Responsabilidad:

```text
Administrar usuarios
```

Podemos evaluar:

```text
User Administrator
```

en lugar de:

```text
Global Administrator
```

---

# 11. Ejemplo - Helpdesk Administrator

Responsabilidad:

```text
Soporte a usuarios
```

Podemos evaluar un rol como:

```text
Helpdesk Administrator
```

según las tareas requeridas.

---

# 12. Roles y responsabilidades

Conceptualmente:

```text
Billing
   |
   v
Billing Administrator


User Management
   |
   v
User Administrator


Helpdesk
   |
   v
Helpdesk Administrator
```

El objetivo es relacionar:

```text
JOB FUNCTION
     |
     v
ROLE
```

---

# 13. DEMO INSTRUCTOR - Microsoft Entra Roles

Abrir:

```text
Microsoft Entra admin center
```

Mostrar el área correspondiente a:

```text
Roles and administrators
```

Buscar algunos roles utilizados durante el curso.

Por ejemplo:

```text
Global Administrator
User Administrator
Billing Administrator
Helpdesk Administrator
```

---

# 14. Qué mostrar

Seleccionar un rol.

Revisar:

- descripción;
- permisos/capacidades;
- asignaciones;
- miembros.

No realizar todavía cambios innecesarios.

---

# 15. Pregunta para los alumnos

Mostrar:

```text
Global Administrator
```

y preguntar:

> ¿Por qué no utilizamos simplemente este rol para todos los administradores?

La discusión debería conducir a:

```text
Least Privilege
```

---

# 16. Asignación directa

Un rol puede asignarse directamente a una identidad.

Conceptualmente:

```text
LAB-Admin
    |
    v
Billing Administrator
```

Esto puede ser apropiado en determinados escenarios.

---

# 17. Problema de muchas asignaciones directas

Supongamos:

```text
50 Helpdesk users
```

Podríamos administrar:

```text
User 1 -> Role
User 2 -> Role
User 3 -> Role
...
User 50 -> Role
```

Pero esto puede complicar la administración.

---

# 18. Administración mediante grupos

Una alternativa es utilizar grupos apropiados para administrar determinadas asignaciones.

Modelo conceptual:

```text
Users
  |
  v
Role-Assignable Group
  |
  v
Directory Role
```

Ejemplo:

```text
Support Team
      |
      v
User Management Role Group
      |
      v
Role
```

---

# 19. Role-Assignable Groups

Microsoft Entra permite utilizar determinados grupos de seguridad para asignaciones de roles.

Conceptualmente:

```text
LAB-Helpdesk
      |
      v
User Management Role Group
      |
      v
Helpdesk Administrator
```

El administrador puede gestionar la pertenencia al grupo en lugar de administrar cada asignación individual por separado.

---

# 20. Analogía

En lugar de entregar individualmente una llave especial a 30 personas:

```text
Persona -> Llave
Persona -> Llave
Persona -> Llave
```

creamos una función:

```text
Equipo de soporte
       |
       v
Acceso correspondiente
```

La pertenencia al equipo determina quién obtiene ese acceso.

---

# 21. Precaución

Los grupos utilizados para asignación de roles son objetos sensibles.

No deben tratarse como grupos comunes sin considerar su impacto.

Agregar una identidad al grupo puede implicar:

```text
Group membership
       |
       v
Administrative privileges
```

---

# 22. DEMO INSTRUCTOR - Group

Mostrar un grupo de laboratorio como:

```text
User Management Role Group
```

Explicar la propiedad relacionada con la posibilidad de asignar roles al grupo cuando esté disponible.

No utilizar grupos productivos.

---

# 23. Administración delegada

El objetivo de los roles es permitir delegar administración.

Ejemplo:

```text
Global Admin
      |
      +---- User Admin
      |
      +---- Helpdesk Admin
      |
      +---- Billing Admin
```

No todos necesitan los mismos privilegios.

---

# 24. Analogía organizacional

En una empresa:

```text
CEO
 |
 +---- Finance
 |
 +---- HR
 |
 +---- IT
 |
 +---- Support
```

El CEO no realiza personalmente cada tarea.

Las responsabilidades se delegan.

La administración de Microsoft 365 sigue un principio parecido.

---

# 25. Validar permisos

Asignar un rol no es suficiente.

Debemos comprobar:

```text
¿Puede realizar la tarea esperada?
```

y también:

```text
¿Está impedido de realizar tareas
que no debería poder hacer?
```

---

# 26. Prueba de permisos

Modelo:

```text
Assign role
     |
     v
Sign in as test user
     |
     v
Attempt authorized task
     |
     v
Success
```

Después:

```text
Attempt unauthorized task
     |
     v
Denied
```

Esto demuestra realmente:

```text
Least Privilege
```

---

# 27. InPrivate / segundo perfil

En XtremeLabs puede existir una segunda máquina virtual para probar otra identidad.

En Standalone podemos utilizar:

```text
Browser session 1
      |
      v
Administrator

Browser InPrivate / Profile 2
      |
      v
LAB user
```

Esto permite validar permisos sin necesitar otra VM.

---

# 28. DEMO INSTRUCTOR - Validación

Mantener:

```text
Admin session
```

en el navegador principal.

Abrir:

```text
InPrivate
```

e iniciar sesión con un usuario LAB que tenga un rol limitado.

Mostrar que la interfaz y las capacidades disponibles pueden ser diferentes.

---

# 29. Microsoft Graph

No todas las tareas administrativas tienen que realizarse exclusivamente desde el portal.

Microsoft Graph proporciona acceso programático a recursos Microsoft 365 y Microsoft Entra.

Conceptualmente:

```text
Administrator
      |
      +---- Portal
      |
      +---- PowerShell
              |
              v
        Microsoft Graph
```

---

# 30. Microsoft Graph PowerShell

Microsoft Graph PowerShell permite trabajar con Microsoft Graph mediante PowerShell.

Ejemplos:

```powershell
Connect-MgGraph
Get-MgContext
Get-MgUser
```

Durante el laboratorio utilizaremos Graph también para trabajar con roles.

---

# 31. Conectarse a Microsoft Graph

Ejemplo:

```powershell
Connect-MgGraph -Scopes "User.Read.All","RoleManagement.ReadWrite.Directory"
```

Después:

```powershell
Get-MgContext
```

---

# 32. Qué explicar sobre Scopes

Cuando ejecutamos:

```text
Connect-MgGraph
```

podemos solicitar permisos necesarios para realizar determinadas operaciones.

Conceptualmente:

```text
PowerShell
    |
    v
Requested scopes
    |
    v
Microsoft Graph
    |
    v
Allowed operations
```

---

# 33. Mínimo privilegio también aplica aquí

No debemos solicitar permisos amplios simplemente porque:

```text
"quizás los necesitemos"
```

El mismo principio sigue aplicando:

```text
Required operation
       |
       v
Required permission
```

---

# 34. Consultar roles

Podemos explorar definiciones de roles mediante Graph.

Ejemplo:

```powershell
Get-MgRoleManagementDirectoryRoleDefinition
```

Podemos buscar un rol específico.

Ejemplo conceptual:

```powershell
Get-MgRoleManagementDirectoryRoleDefinition |
Where-Object DisplayName -eq "Service Support Administrator"
```

---

# 35. Consultar usuarios

Ejemplo:

```powershell
Get-MgUser
```

Esto permite recuperar identidades disponibles mediante Microsoft Graph.

---

# 36. Asignaciones mediante Graph

Microsoft Graph también permite administrar asignaciones de roles.

Durante el Lab 02 utilizaremos:

```powershell
New-MgRoleManagementDirectoryRoleAssignment
```

El objetivo didáctico no es memorizar el comando.

El objetivo es comprender:

```text
Portal
and
Automation
```

pueden administrar los mismos tipos de recursos.

---

# 37. Portal vs PowerShell

### Portal

Ventajas para aprendizaje:

```text
Visual
Easy to explore
Good for demos
```

### PowerShell

Ventajas:

```text
Repeatable
Automatable
Scalable
Scriptable
```

---

# 38. Analogía

Configurar manualmente un usuario es parecido a:

```text
hacer una tarea una vez
```

Automatizar con PowerShell es parecido a:

```text
crear un procedimiento repetible
```

Cuando administramos cientos o miles de objetos, la automatización cobra mayor importancia.

---

# 39. DEMO INSTRUCTOR - Graph

Abrir PowerShell.

Mostrar:

```powershell
Connect-MgGraph -Scopes "User.Read.All"
```

Después:

```powershell
Get-MgContext
```

y:

```powershell
Get-MgUser -Top 5 |
Select-Object DisplayName, UserPrincipalName
```

No realizar asignaciones administrativas durante esta demo inicial.

---

# 40. Qué mostrar en Get-MgContext

Explicar elementos como:

```text
Account
TenantId
Scopes
```

La idea es demostrar:

```text
¿Quién está conectado?

¿A qué tenant?

¿Con qué permisos?
```

---

# 41. Caso práctico

Empresa:

```text
Contoso
```

Tiene:

```text
10 Helpdesk technicians
3 User administrators
2 Billing administrators
2 Global administrators
```

Pregunta:

> ¿Deberíamos convertir a los 17 usuarios en Global Administrators?

Respuesta:

```text
No
```

Debemos diseñar las asignaciones según responsabilidades.

---

# 42. Riesgo de privilegios excesivos

Modelo:

```text
More privileges
      |
      v
Larger impact
      |
      v
Higher risk
```

Una identidad comprometida con privilegios elevados puede producir un impacto mayor.

---

# 43. Relación con Copilot

Los roles administrativos no significan automáticamente que Copilot vaya a mostrar todos los datos de la organización.

Sin embargo, la administración correcta de identidades, permisos y privilegios forma parte del gobierno general de Microsoft 365 sobre el que se implementa Copilot.

Debemos evitar mezclar:

```text
Administrative roles
```

con:

```text
Content permissions
```

Son conceptos relacionados con seguridad, pero no son exactamente lo mismo.

---

# 44. Distinción importante

### Administrative role

Determina:

```text
¿Qué puedo administrar?
```

### Content permission

Determina:

```text
¿Qué contenido puedo acceder?
```

Ejemplo:

```text
User Administrator
```

no significa necesariamente:

```text
Puede leer todos los documentos de SharePoint
```

---

# 45. Relación con Lab 02

Este módulo completa la preparación conceptual para:

```text
Standalone Lab 02
Identities, Security and Roles
```

En el laboratorio el alumno trabaja con:

```text
Direct Role Assignment
        |
        v
Role-Assignable Group
        |
        v
Delegated Permissions
        |
        v
Microsoft Graph PowerShell
```

---

# 46. Qué ejecutará el alumno

Durante el laboratorio podrá realizar, según el entorno:

```text
Assign limited role
       |
       v
Create role-assignable group
       |
       v
Add LAB user
       |
       v
Validate permissions
       |
       v
Use Microsoft Graph
```

---

# 47. Qué NO debemos hacer

Evitar:

```text
Global Administrator para todos
```

Evitar:

```text
probar roles con usuarios productivos
```

Evitar:

```text
modificar cuentas administrativas reales
```

Evitar:

```text
asignar permisos amplios sin necesidad
```

---

# 48. Pregunta de comprobación

Preguntar:

> Un usuario necesita administrar cuentas de usuario. ¿Cuál debería ser nuestra primera opción?

No buscar inicialmente:

```text
Global Administrator
```

Buscar:

```text
el rol con los privilegios necesarios
para realizar la tarea
```

---

# 49. Segunda comprobación

Preguntar:

> ¿Qué diferencia existe entre autenticación y autorización?

Respuesta:

```text
Authentication
=
Demostrar quién eres

Authorization
=
Determinar qué puedes hacer
```

---

# 50. Tercera comprobación

Preguntar:

> ¿Por qué utilizaríamos Microsoft Graph PowerShell si existe un portal?

Respuesta conceptual:

```text
Automation
Repeatability
Scale
Scripting
```

---

# 51. Mensaje clave

El alumno debe recordar:

> Poder iniciar sesión no significa tener permiso para administrarlo todo.

Modelo:

```text
Identity
   |
   v
Authentication
   |
   v
Authorization
   |
   v
Least Privilege
```

---

# 52. Conexión Module 02 + Module 03

Ahora tenemos:

```text
MODULE 02
Who can enter?
      |
      v
Secure Access

MODULE 03
What can they do?
      |
      v
Roles & Permissions
```

Juntos forman:

```text
IDENTITY SECURITY
```

---

# 53. Transición al siguiente módulo

Cerrar con:

```text
Ya protegimos el acceso.

Ya controlamos los privilegios.

Ahora necesitamos preparar
las aplicaciones desde las que
los usuarios trabajarán.
```

Siguiente:

```text
Module 04
Microsoft 365 Apps
```