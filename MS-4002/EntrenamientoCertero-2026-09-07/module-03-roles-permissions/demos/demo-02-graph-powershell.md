# DEMO 02 - Microsoft Graph PowerShell

## MS-4002 - Module 03: Roles and Permissions

---

## Duración

15 a 20 minutos

## Tipo

DEMO INSTRUCTOR

## Herramienta

```text
PowerShell
Microsoft Graph PowerShell SDK
```

---

## Objetivo

Mostrar cómo utilizar Microsoft Graph PowerShell para consultar usuarios, roles administrativos y asignaciones de roles en Microsoft Entra.

Al finalizar la demo, el alumno debe comprender:

```text
PowerShell
    ↓
Microsoft Graph
    ↓
Microsoft Entra
    ↓
Users / Roles / Assignments
```

---

## Escenario

En la demo anterior administramos roles desde el portal.

Utilizamos:

```text
Diego Perez - Helpdesk
lab-helpdesk@<TU-DOMINIO>
```

y revisamos el principio:

```text
Least Privilege
```

Ahora queremos demostrar que las mismas tareas administrativas también pueden consultarse o automatizarse mediante Microsoft Graph PowerShell.

---

# 1. Abrir PowerShell

Abrir:

```text
Windows PowerShell
```

o:

```text
PowerShell 7
```

No es necesario ejecutar como administrador si Microsoft Graph ya está instalado para el usuario.

---

# 2. Verificar Microsoft Graph

Ejecutar:

```powershell
Get-InstalledModule Microsoft.Graph -ErrorAction SilentlyContinue
```

---

## Resultado esperado

Debería aparecer información similar a:

```text
Version    Name
-------    ----
2.x.x      Microsoft.Graph
```

La versión exacta puede variar.

---

# 3. Si Microsoft Graph no está instalado

Mostrar conceptualmente:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
```

No es necesario reinstalarlo si ya existe.

---

## Qué explicar

Microsoft Graph PowerShell SDK permite interactuar con servicios Microsoft mediante Microsoft Graph.

Conceptualmente:

```text
Administrator
      ↓
PowerShell
      ↓
Microsoft Graph SDK
      ↓
Microsoft Graph API
      ↓
Microsoft 365 / Entra
```

---

# 4. Verificar módulos relevantes

Ejecutar:

```powershell
Get-Module Microsoft.Graph.Users -ListAvailable
```

Luego:

```powershell
Get-Module Microsoft.Graph.Identity.DirectoryManagement -ListAvailable
```

---

## Qué explicar

Microsoft Graph PowerShell está organizado en módulos.

En esta demo nos interesan especialmente capacidades relacionadas con:

```text
Users

Directory Management

Role Management
```

---

# 5. Conectarse a Microsoft Graph

Ejecutar:

```powershell
Connect-MgGraph -Scopes "User.Read.All","RoleManagement.Read.Directory"
```

Se abrirá el proceso de autenticación.

Utilizar la cuenta administrativa del tenant de práctica.

---

## Qué explicar

Los scopes representan permisos solicitados por la sesión de Microsoft Graph.

En este caso:

```text
User.Read.All
```

permite consultar información de usuarios según los permisos concedidos.

Y:

```text
RoleManagement.Read.Directory
```

permite consultar información relacionada con administración de roles.

---

# 6. Verificar la conexión

Ejecutar:

```powershell
Get-MgContext
```

---

## Qué observar

Mostrar campos como:

```text
Account

TenantId

Scopes

AuthType
```

---

## Pregunta para la clase

> ¿Por qué debemos revisar Get-MgContext antes de ejecutar comandos administrativos?

Respuesta esperada:

```text
Para confirmar:

qué cuenta estamos utilizando

en qué tenant estamos

qué permisos tiene la sesión
```

---

# 7. Listar usuarios

Ejecutar:

```powershell
Get-MgUser -Top 10 |
    Select-Object DisplayName, UserPrincipalName
```

---

## Resultado esperado

Aparecerán usuarios del tenant.

Buscar visualmente nuestros usuarios de laboratorio.

Por ejemplo:

```text
Ana Torres - Copilot Pilot

Carlos Mendoza - Test User 1

Laura Rojas - Test User 2

Diego Perez - Helpdesk
```

---

# 8. Buscar específicamente a Diego

Primero identificar el dominio real del tenant.

Después utilizar:

```powershell
Get-MgUser -UserId "lab-helpdesk@<TU-DOMINIO>"
```

---

## Alternativa

Guardar el usuario en una variable:

```powershell
$Diego = Get-MgUser -UserId "lab-helpdesk@<TU-DOMINIO>"
```

Mostrar:

```powershell
$Diego |
    Select-Object Id, DisplayName, UserPrincipalName
```

---

## Qué explicar

La variable:

```text
$Diego
```

ahora representa el objeto de usuario recuperado desde Microsoft Graph.

---

# 9. Mostrar el Object ID

Ejecutar:

```powershell
$Diego.Id
```

---

## Qué explicar

Microsoft Graph normalmente trabaja internamente con identificadores de objetos.

Conceptualmente:

```text
Display Name
=
Diego Perez - Helpdesk

UPN
=
lab-helpdesk@<TU-DOMINIO>

Object ID
=
identificador único del objeto
```

---

# 10. Consultar definiciones de roles

Ejecutar:

```powershell
Get-MgRoleManagementDirectoryRoleDefinition |
    Select-Object DisplayName, Id
```

---

## Qué explicar

Esto consulta las definiciones de roles disponibles en Microsoft Entra.

La lista puede ser extensa.

---

# 11. Buscar Helpdesk Administrator

Ejecutar:

```powershell
$HelpdeskRole = Get-MgRoleManagementDirectoryRoleDefinition `
    -Filter "displayName eq 'Helpdesk Administrator'"
```

Mostrar:

```powershell
$HelpdeskRole |
    Select-Object DisplayName, Id
```

---

## Resultado esperado

Conceptualmente:

```text
DisplayName
-----------
Helpdesk Administrator
```

junto con su identificador.

---

# 12. Relacionar usuario y rol

Ahora tenemos:

```text
$Diego
```

y:

```text
$HelpdeskRole
```

Mostrar:

```text
$Diego.Id

$HelpdeskRole.Id
```

---

## Qué explicar

Conceptualmente una asignación relaciona:

```text
Principal
   +
Role Definition
   +
Scope
```

Es decir:

```text
Diego
   ↓
Helpdesk Administrator
   ↓
Directory scope
```

---

# 13. Consultar las asignaciones de Diego

Ejecutar:

```powershell
Get-MgRoleManagementDirectoryRoleAssignment `
    -Filter "principalId eq '$($Diego.Id)'"
```

---

## Mostrar de forma más clara

```powershell
Get-MgRoleManagementDirectoryRoleAssignment `
    -Filter "principalId eq '$($Diego.Id)'" |
    Select-Object PrincipalId, RoleDefinitionId, DirectoryScopeId
```

---

## Qué explicar

Aquí estamos consultando:

```text
qué roles tiene asignados Diego
```

pero Microsoft Graph devuelve principalmente identificadores.

---

# 14. Comparar Portal vs PowerShell

Mostrar:

```text
PORTAL

Users
→ Diego
→ Assigned roles
```

frente a:

```text
POWERSHELL

Get-MgUser
        ↓
Get-MgRoleManagementDirectoryRoleAssignment
```

---

## Mensaje

Ambos administran el mismo entorno.

La diferencia es la interfaz:

```text
Portal
=
visual / manual

PowerShell
=
scriptable / repeatable / automatable
```

---

# 15. Mostrar cómo sería una asignación por PowerShell

IMPORTANTE:

Esta parte puede mostrarse sin ejecutarla si el rol ya fue asignado desde el portal.

Para crear una asignación necesitaríamos una sesión con permisos adecuados, por ejemplo:

```powershell
Connect-MgGraph -Scopes `
    "User.Read.All", `
    "RoleManagement.ReadWrite.Directory"
```

---

## Comando de referencia

```powershell
New-MgRoleManagementDirectoryRoleAssignment `
    -PrincipalId $Diego.Id `
    -RoleDefinitionId $HelpdeskRole.Id `
    -DirectoryScopeId "/"
```

---

## NO ejecutar automáticamente

Antes de ejecutarlo verificar:

```text
¿Diego ya tiene el rol?

¿Estamos en el tenant correcto?

¿Tenemos autorización?

¿La asignación es necesaria?
```

---

# 16. Explicar DirectoryScopeId

En el ejemplo:

```powershell
-DirectoryScopeId "/"
```

representa un alcance de directorio.

No profundizar demasiado en scopes administrativos en esta demo.

El objetivo es entender que una asignación contiene:

```text
WHO

WHAT ROLE

WHERE
```

---

# 17. Mostrar el riesgo de automatizar sin validar

Plantear:

```powershell
New-MgRoleManagementDirectoryRoleAssignment
```

es rápido.

Pero también puede ser peligroso si:

```text
usamos el usuario incorrecto

usamos el rol incorrecto

estamos en el tenant incorrecto

automatizamos sin controles
```

---

# 18. Regla antes de ejecutar cambios

Mostrar:

```text
READ
 ↓
VALIDATE
 ↓
CHANGE
 ↓
VERIFY
```

---

## Ejemplo

Primero:

```powershell
Get-MgContext
```

Después:

```powershell
Get-MgUser
```

Después:

```powershell
Get-MgRoleManagementDirectoryRoleDefinition
```

Y solo entonces considerar:

```powershell
New-MgRoleManagementDirectoryRoleAssignment
```

---

# 19. Ejemplo de automatización real

Plantear una organización con:

```text
50 Helpdesk users
```

Administrarlos manualmente puede requerir muchas operaciones.

Con automatización podemos:

```text
read input
    ↓
validate users
    ↓
identify role
    ↓
perform assignment
    ↓
verify
    ↓
generate report
```

---

# 20. Portal vs PowerShell

Mostrar esta comparación:

```text
Portal
----------------
Excelente para aprender
Visual
Ideal para pocas operaciones


PowerShell
----------------
Repetible
Automatizable
Ideal para operaciones masivas
Útil para documentación
Útil para auditoría
```

---

# 21. Relación con Least Privilege

Explicar que Least Privilege también aplica a nuestras herramientas administrativas.

No deberíamos conectarnos solicitando:

```text
todos los permisos posibles
```

si solamente necesitamos consultar usuarios.

Preferimos solicitar los permisos necesarios para la tarea.

---

# 22. Relación con Microsoft 365 Copilot

La preparación de Copilot puede requerir revisar:

```text
Users
Groups
Roles
Permissions
Policies
```

Microsoft Graph permite automatizar parte de estas verificaciones.

Ejemplo conceptual:

```text
Tenant
  ↓
Microsoft Graph
  ↓
Read configuration
  ↓
Generate readiness information
```

---

# 23. Mostrar comandos utilizados

```powershell
Get-InstalledModule Microsoft.Graph

Connect-MgGraph

Get-MgContext

Get-MgUser

Get-MgRoleManagementDirectoryRoleDefinition

Get-MgRoleManagementDirectoryRoleAssignment
```

Y, cuando realmente corresponda:

```powershell
New-MgRoleManagementDirectoryRoleAssignment
```

---

# 24. Desconectarse

Al finalizar ejecutar:

```powershell
Disconnect-MgGraph
```

---

## Qué explicar

Esto cierra la sesión actual de Microsoft Graph PowerShell.

---

# 25. Resultado esperado

El alumno debe poder explicar:

```text
cómo conectarse a Microsoft Graph

cómo comprobar el tenant

cómo consultar usuarios

cómo consultar roles

cómo consultar asignaciones

por qué validar antes de modificar
```

---

# 26. Qué NO hacer

No:

```text
copiar comandos de Internet
y ejecutarlos sin entenderlos

asignar Global Administrator

solicitar permisos innecesarios

automatizar cambios sin validación

trabajar sin comprobar Get-MgContext
```

---

# 27. Plan B - No conecta Microsoft Graph

Revisar:

```text
Internet

Microsoft.Graph instalado

Cuenta utilizada

Consentimiento

Scopes solicitados

Permisos del usuario
```

Si la conexión no puede realizarse:

```text
mostrar los comandos

explicar el flujo

continuar con el portal
```

---

# 28. Plan B - Usuario no encontrado

Verificar:

```powershell
Get-MgUser -Top 20 |
    Select-Object DisplayName, UserPrincipalName
```

Confirmar el UPN real.

No asumir que:

```text
<TU-DOMINIO>
```

es literalmente el dominio.

Debe reemplazarse por el dominio real del tenant.

---

# 29. Plan B - El rol ya está asignado

Perfecto.

No volver a asignarlo.

Utilizar:

```powershell
Get-MgRoleManagementDirectoryRoleAssignment
```

para demostrar la consulta.

---

# 30. Mensaje clave

> El portal nos permite administrar visualmente. Microsoft Graph PowerShell nos permite consultar, repetir y automatizar esas operaciones, pero la automatización siempre debe ir acompañada de validación y Least Privilege.

---

# 31. Cierre de Module 03

Conectar:

```text
Identity
   ↓
Role
   ↓
Least Privilege
   ↓
Portal
   +
Microsoft Graph
```

---

# 32. Transición

Siguiente módulo:

```text
Module 04
Microsoft 365 Apps for enterprise
```

Ahí cambiaremos el foco desde:

```text
Who can administer?
```

hacia:

```text
What applications and services
are users actually using?
```