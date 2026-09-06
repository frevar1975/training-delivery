# MS-4002 - Lab 02
## Guía del instructor - Identidades, acceso seguro y roles

**Modalidad:** Standalone  
**Curso:** MS-4002 - Prepare security and compliance to support Microsoft 365 Copilot  
**Duración sugerida:** 90-120 minutos

---

# 1. Propósito del laboratorio

Este laboratorio adapta las prácticas de identidad, acceso seguro y administración de roles del entorno XtremeLabs a un escenario sin laboratorio hospedado.

El alumno utilizará:

- su propia PC;
- un navegador principal;
- una ventana InPrivate o segundo perfil;
- PowerShell local;
- un tenant Microsoft 365 de práctica.

No se requiere:

- LON-CL1;
- LON-CL2;
- LON-DC1;
- usuarios precargados por XtremeLabs;
- credenciales proporcionadas por un proveedor de laboratorio.

---

# 2. Objetivos didácticos

Al finalizar el laboratorio el alumno debería comprender y poder demostrar:

- cómo revisar licencias y usuarios;
- cómo trabajar con un grupo piloto;
- cómo acceder a Microsoft Entra;
- cómo funciona Conditional Access;
- cómo se relaciona Conditional Access con MFA;
- qué es Smart Lockout;
- qué es Password Protection;
- cómo funcionan los roles administrativos;
- cómo usar grupos asignables a roles;
- cómo validar permisos delegados;
- cómo utilizar Microsoft Graph PowerShell para consultar y asignar roles.

---

# 3. Clasificación de actividades

Durante este laboratorio utilizaremos tres tipos de actividad.

## ALUMNO

El alumno ejecuta directamente la tarea.

## DEMO INSTRUCTOR

El instructor demuestra la configuración y explica el concepto.

## OPCIONAL

Se documenta y puede realizarse si hay tiempo, licencias y un tenant adecuado.

---

# 4. Preparación previa del instructor

Antes de la clase valida:

- acceso al tenant de práctica;
- existencia de al menos una cuenta administrativa;
- disponibilidad de usuarios de prueba;
- disponibilidad de licencias;
- acceso a Microsoft Entra admin center;
- disponibilidad de Conditional Access;
- Microsoft Graph PowerShell instalado.

Idealmente disponer de:

- LAB-Admin
- LAB-Pilot
- LAB-User1
- LAB-User2
- LAB-Helpdesk

También debe existir:

**M365 Copilot Pilot**

creado durante el Lab 01.

---

# 5. Seguridad del laboratorio

> IMPORTANTE
>
> No realizar estas prácticas en un tenant de producción.
>
> No aplicar políticas de Conditional Access a todos los usuarios durante una clase.
>
> No utilizar Global Administrator innecesariamente.
>
> No provocar bloqueos deliberados de cuentas administrativas.
>
> No modificar Smart Lockout con valores agresivos salvo que el tenant esté dedicado completamente a pruebas.

---

# 6. PARTE 1 - Licencias y usuarios

## Tipo

**ALUMNO**

## Tiempo sugerido

10-15 minutos

## Mostrar

Microsoft 365 admin center:

**Billing > Licenses**

y:

**Users > Active users**

---

## Explicación

Las licencias determinan qué servicios y capacidades están disponibles para cada usuario.

No todos los tenants de capacitación tienen exactamente las mismas suscripciones.

Por eso el laboratorio Standalone debe comenzar revisando qué está realmente disponible.

---

## Analogía

"Antes de entregar acceso a una aplicación debemos verificar qué licencias tenemos disponibles."

La licencia es similar a una entrada que habilita determinados servicios.

---

## Resultado esperado

El alumno identifica:

- licencias existentes;
- licencias disponibles;
- usuarios disponibles.

---

# 7. PARTE 2 - Grupo piloto

## Tipo

**ALUMNO**

## Tiempo sugerido

5 minutos

Agregar:

**LAB-Pilot**

al grupo:

**M365 Copilot Pilot**

---

## Explicación

El grupo piloto representa a los usuarios que inicialmente participan en una implementación controlada.

Más adelante puede utilizarse para:

- asignación;
- prueba;
- control;
- exclusiones temporales;
- adopción gradual.

---

# 8. PARTE 3 - Microsoft Entra

## Tipo

**DEMO INSTRUCTOR + ALUMNO**

## Tiempo sugerido

5 minutos

Mostrar Microsoft Entra admin center.

Áreas principales:

- Identity
- Users
- Groups
- Roles & admins
- Protection
- Monitoring & health

---

## Explicación

Microsoft 365 admin center ofrece administración general.

Microsoft Entra se especializa en:

- identidades;
- autenticación;
- acceso;
- roles;
- seguridad de identidad.

---

# 9. PARTE 4 - Conditional Access

## Tipo

**ALUMNO CONTROLADO**

## Tiempo sugerido

20 minutos

Crear el grupo:

**CA-MFA-Lab**

Agregar:

**LAB-User1**

Crear la política:

**LAB - Require MFA**

---

## Configuración recomendada para clase

### Usuarios

Seleccionar:

**CA-MFA-Lab**

No utilizar:

**All users**

### Recursos

Seleccionar según disponibilidad del tenant.

### Grant

Configurar el requisito de autenticación multifactor disponible en el tenant.

### Estado inicial

**Report-only**

---

# 10. Qué explicar sobre Conditional Access

Conditional Access puede entenderse como:

```text
IF
    condición
THEN
    acción
```

Ejemplo:

```text
SI un usuario determinado intenta acceder

ENTONCES requerir MFA.
```

---

## Analogía

"Un guardia de seguridad puede aplicar reglas diferentes dependiendo de quién entra, desde dónde entra y a qué área quiere acceder."

Conditional Access evalúa contexto y decide qué controles aplicar.

---

# 11. Por qué utilizamos Report-only

Report-only permite evaluar una política sin aplicarla inmediatamente.

Esto reduce el riesgo de:

- bloquear usuarios;
- interrumpir la clase;
- perder acceso administrativo.

Explicar que es una práctica útil antes de activar políticas amplias.

---

# 12. DEMO - Segunda sesión del navegador

## Tipo

**ALUMNO**

En lugar de utilizar otra VM:

- abrir Edge InPrivate;

o:

- utilizar un segundo perfil del navegador.

Iniciar sesión como:

**LAB-User1**

---

## Explicación

La segunda sesión representa otro usuario.

Esto sustituye la necesidad de utilizar **LON-CL2** del entorno XtremeLabs.

```text
XtremeLabs

LON-CL1
    |
    +---- LON-CL2


Standalone

Navegador principal
    |
    +---- Edge InPrivate / segundo perfil
```

---

# 13. PARTE 5 - Sign-in logs

## Tipo

**DEMO INSTRUCTOR + ALUMNO**

## Tiempo sugerido

10 minutos

Mostrar:

**Microsoft Entra > Identity > Monitoring & health > Sign-in logs**

Buscar:

**LAB-User1**

Abrir el evento.

Mostrar la información relacionada con:

**Conditional Access**

---

## Explicación

Los Sign-in logs permiten investigar:

- quién inició sesión;
- cuándo;
- desde dónde;
- resultado de autenticación;
- políticas aplicadas;
- controles requeridos.

---

# 14. Activación de la política

## Tipo

**DEMO INSTRUCTOR**

Solo activar la política si:

- el tenant es completamente de laboratorio;
- la cuenta administrativa no está incluida;
- la población está limitada a CA-MFA-Lab;
- existe una forma segura de recuperar acceso.

Si no se cumplen estas condiciones:

**mantener Report-only.**

---

# 15. PARTE 6 - Smart Lockout

## Tipo

**DEMO INSTRUCTOR**

## Tiempo sugerido

10 minutos

Mostrar:

**Protection > Authentication methods > Password protection**

Identificar:

- Lockout threshold
- Lockout duration
- Custom banned password list

---

# 16. Adaptación respecto a XtremeLabs

El laboratorio hospedado utiliza configuraciones específicas para demostrar Smart Lockout y puede provocar intencionalmente el bloqueo de un usuario de prueba.

En nuestra versión Standalone no recomendamos realizar este procedimiento por defecto.

El objetivo es comprender el mecanismo sin arriesgar el acceso al tenant.

Tampoco necesitamos reproducir la parte de Active Directory local utilizando LON-DC1 si el alumno solamente dispone de Microsoft Entra ID.

---

# 17. Qué explicar sobre Smart Lockout

Smart Lockout ayuda a proteger cuentas frente a intentos repetidos de autenticación.

No debe explicarse simplemente como:

```text
"Después de X intentos, bloquear."
```

Microsoft Entra utiliza mecanismos de protección para responder a intentos de autenticación potencialmente maliciosos.

---

# 18. Password Protection

## Tipo

**DEMO INSTRUCTOR**

Mostrar:

**Custom banned password list**

Explicar que una organización puede impedir contraseñas relacionadas con:

- marca;
- empresa;
- productos;
- nombres internos;
- términos fácilmente predecibles.

No utilizar contraseñas reales como ejemplo.

---

# 19. PARTE 7 - Roles administrativos

## Tipo

**ALUMNO**

## Tiempo sugerido

15 minutos

Mostrar:

**Identity > Roles & admins**

Buscar algunos roles:

- Global Administrator
- User Administrator
- Helpdesk Administrator
- Billing Administrator

Revisar la descripción de cada uno.

---

# 20. Principio de mínimo privilegio

Explicar:

> "No damos Global Administrator simplemente porque sea más fácil."

La regla es:

**dar únicamente los permisos necesarios para realizar una función.**

---

## Analogía

"En un hotel no todos los empleados necesitan una llave maestra."

Recepción necesita ciertos accesos.

Mantenimiento necesita otros.

Administración necesita otros.

---

# 21. Asignación directa de rol

## Tipo

**ALUMNO**

Seleccionar:

**LAB-User2**

Asignar:

**Billing Administrator**

o el rol que defina el instructor.

---

## Resultado esperado

El usuario debe aparecer con el rol asignado.

Explicar que esta es la forma más sencilla:

```text
Usuario
    |
    v
Rol
    |
    v
Permisos
```

---

# 22. PARTE 8 - Grupo asignable a roles

## Tipo

**ALUMNO / DEMO SEGÚN LICENCIAMIENTO**

## Tiempo sugerido

15 minutos

Crear:

**User Management Role Group**

Tipo:

**Security**

Activar la opción que permite asignar roles de Microsoft Entra al grupo, si está disponible.

Membership:

**Assigned**

Agregar:

**LAB-Helpdesk**

---

# 23. Qué explicar

En lugar de asignar roles uno por uno:

```text
Usuario 1 ----> Rol
Usuario 2 ----> Rol
Usuario 3 ----> Rol
```

podemos utilizar:

```text
Usuario 1 --+
            |
Usuario 2 --+--> Grupo --> Rol --> Permisos
            |
Usuario 3 --+
```

Esto simplifica la administración.

Agregar un usuario al grupo puede otorgarle los roles asociados al grupo.

---

# 24. Roles sugeridos

Para el laboratorio podemos utilizar:

- User Administrator
- Helpdesk Administrator

No es necesario asignar una gran cantidad de roles.

El objetivo es demostrar el patrón.

---

# 25. PARTE 9 - Validación de permisos

## Tipo

**ALUMNO**

Abrir:

**Edge InPrivate**

Iniciar sesión como:

**LAB-Helpdesk**

---

## Mostrar

Qué opciones administrativas aparecen.

Comparar con la sesión de:

**LAB-Admin**

---

## Explicación

La interfaz y las operaciones disponibles dependen de los privilegios del usuario.

Dos usuarios pueden acceder al mismo portal, pero no necesariamente tienen las mismas capacidades.

---

# 26. Prueba segura

Seleccionar únicamente un usuario de laboratorio sin privilegios elevados.

Por ejemplo:

**LAB-Pilot**

Revisar qué acciones puede realizar LAB-Helpdesk.

No probar operaciones sobre:

- Global Administrators;
- cuentas reales;
- cuentas del instructor;
- usuarios fuera del laboratorio.

---

# 27. PARTE 10 - Microsoft Graph PowerShell

## Tipo

**DEMO INSTRUCTOR + ALUMNO**

## Tiempo sugerido

20 minutos

Conectar:

```powershell
Connect-MgGraph -Scopes "User.Read.All","RoleManagement.ReadWrite.Directory"
```

Completar la autenticación utilizando la cuenta administrativa del tenant de laboratorio.

---

# 28. Validar contexto

Ejecutar:

```powershell
Get-MgContext
```

Mostrar:

- Account
- TenantId
- Scopes

---

## Explicación

Antes de ejecutar tareas administrativas mediante PowerShell siempre debemos saber:

- quién somos;
- a qué tenant estamos conectados;
- qué permisos tiene la sesión.

Podemos representarlo así:

```text
PowerShell
    |
    v
Microsoft Graph
    |
    +---- Account
    |
    +---- TenantId
    |
    +---- Scopes
```

---

# 29. Consultar roles

Ejecutar:

```powershell
Get-MgRoleManagementDirectoryRoleDefinition |
Select-Object Id, DisplayName |
Sort-Object DisplayName
```

Buscar un rol específico:

```powershell
Get-MgRoleManagementDirectoryRoleDefinition |
Where-Object DisplayName -eq "Service Support Administrator" |
Select-Object Id, DisplayName
```

---

## Resultado esperado

Debe obtenerse información similar a:

```text
Id                                   DisplayName
--                                   -----------
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx Service Support Administrator
```

El identificador real dependerá del tenant y de Microsoft Entra.

---

# 30. Consultar usuario

Ejemplo:

```powershell
Get-MgUser -Filter "displayName eq 'LAB-User2'" |
Select-Object Id, DisplayName, UserPrincipalName
```

Resultado conceptual:

```text
Id                                   DisplayName UserPrincipalName
--                                   ----------- -----------------
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx LAB-User2   lab-user2@tenant.onmicrosoft.com
```

---

# 31. Qué explicar sobre los IDs

Microsoft Graph trabaja frecuentemente con identificadores únicos.

No debemos asumir que:

**DisplayName**

es suficiente para realizar operaciones.

Por eso primero consultamos:

```text
RoleDefinitionId
```

y:

```text
UserId
```

Luego podemos realizar la asignación.

---

# 32. Asignar rol mediante Microsoft Graph

## Tipo

**OPCIONAL / DEMO INSTRUCTOR**

Solo realizar si:

- el instructor valida el rol;
- el usuario es de laboratorio;
- el tenant es de pruebas.

Utilizar los identificadores obtenidos anteriormente.

```powershell
New-MgRoleManagementDirectoryRoleAssignment `
    -RoleDefinitionId "<ROLE-ID>" `
    -PrincipalId "<USER-ID>" `
    -DirectoryScopeId "/"
```

Sustituir:

```text
<ROLE-ID>
```

por el identificador real del rol.

Sustituir:

```text
<USER-ID>
```

por el identificador real del usuario.

---

# 33. Explicación: Portal vs Microsoft Graph

Portal y Graph son dos formas diferentes de administrar el mismo directorio.

## Portal

```text
Administrador
    |
    v
Microsoft Entra Admin Center
    |
    v
Microsoft Entra ID
```

## PowerShell

```text
Administrador
    |
    v
Microsoft Graph PowerShell
    |
    v
Microsoft Graph
    |
    v
Microsoft Entra ID
```

Ambos administran el mismo tenant.

---

# 34. Errores frecuentes

## Get-MgContext no muestra información

Esto normalmente significa que todavía no existe una sesión activa de Microsoft Graph.

Ejecutar:

```powershell
Connect-MgGraph
```

y posteriormente:

```powershell
Get-MgContext
```

---

## El alumno no puede crear Conditional Access

Posibles causas:

- licencia no disponible;
- permisos insuficientes;
- características no disponibles en el tenant.

### Plan B

**DEMO INSTRUCTOR**

El instructor realiza la configuración y los alumnos observan el resultado.

---

## No aparece la opción de grupo asignable a roles

Puede depender de:

- permisos;
- licencia;
- configuración del tenant.

### Plan B

Mostrar el concepto y continuar.

---

## El rol no aparece inmediatamente

Utilizar:

**Refresh**

Esperar algunos minutos.

---

## Microsoft Graph solicita consentimiento

Revisar los scopes solicitados.

No aceptar permisos adicionales que no sean necesarios para el ejercicio.

---

# 35. Limpieza recomendada

Al finalizar, revisar la política:

**LAB - Require MFA**

Dejarla en:

**Report-only**

o:

**Disabled**

según lo que se necesite para el resto del curso.

No eliminar necesariamente:

- M365 Copilot Pilot
- LAB-Pilot
- LAB-User1
- LAB-User2
- LAB-Helpdesk
- User Management Role Group

porque pueden reutilizarse en laboratorios posteriores.

---

# 36. Qué hace el alumno y qué hace el instructor

## ALUMNO

- revisar licencias;
- utilizar usuarios de prueba;
- agregar un usuario al grupo piloto;
- crear CA-MFA-Lab;
- crear la política en Report-only;
- probar una segunda sesión;
- revisar Sign-in logs;
- revisar roles;
- asignar un rol directo;
- crear un grupo asignable a roles si está disponible;
- consultar usuarios y roles mediante Graph.

## DEMO INSTRUCTOR

- explicar Microsoft Entra;
- activar Conditional Access si corresponde;
- demostrar MFA;
- mostrar Smart Lockout;
- mostrar Password Protection;
- explicar Sign-in logs;
- realizar troubleshooting.

## OPCIONAL

- activar MFA realmente para el usuario de prueba;
- modificar Smart Lockout;
- asignar un rol mediante Graph;
- realizar pruebas avanzadas de delegación administrativa.

---

# 37. Distribución sugerida del tiempo

| Actividad | Tiempo |
|---|---:|
| Licencias y usuarios | 15 min |
| Microsoft Entra | 5 min |
| Conditional Access | 20 min |
| InPrivate + Sign-in logs | 15 min |
| Smart Lockout | 10 min |
| Roles administrativos | 15 min |
| Grupo asignable a roles | 15 min |
| Microsoft Graph | 20 min |
| Preguntas / troubleshooting | 10 min |

**Total aproximado:** 125 minutos

Si la sesión es más corta, reducir:

- Smart Lockout a DEMO;
- asignación de roles mediante Graph a DEMO/OPCIONAL;
- pruebas avanzadas de delegación a OPCIONAL.

---

# 38. Mapeo XtremeLabs -> Standalone

| XtremeLabs | Standalone |
|---|---|
| LON-CL1 | PC del alumno |
| LON-CL2 | Edge InPrivate / segundo perfil |
| LON-DC1 | Se elimina para el escenario cloud-only |
| MOD Administrator | Administrador del tenant de práctica |
| Usuarios Adatum precargados | LAB-User1, LAB-User2, LAB-Helpdesk, etc. |
| Credenciales de XtremeLabs | Credenciales del tenant de práctica |
| Tenant preparado | Tenant Microsoft 365 de práctica |
| VMs preparadas | Navegador + PowerShell local |

---

# 39. Resultado final

Al finalizar el laboratorio los alumnos deberían comprender el flujo:

```text
Identidad
    |
    v
Grupo
    |
    v
Política
    |
    v
Autenticación
    |
    v
Rol
    |
    v
Permisos
```

y cómo Microsoft Entra protege el acceso antes de implementar controles posteriores de Microsoft Purview.

---

# 40. Conexión con el siguiente laboratorio

El siguiente paso será proteger la información.

**Lab 03 - Microsoft Purview Data Loss Prevention**

El enfoque cambia de:

```text
¿Quién puede entrar?
```

a:

```text
¿Qué puede hacer el usuario con la información?
```