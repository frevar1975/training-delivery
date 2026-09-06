# MS-4002 - Lab 02
## Administrar identidades, acceso seguro y roles

**Modalidad:** Standalone  
**Entorno:** Tenant Microsoft 365 de práctica  
**Duración estimada:** 90-120 minutos

---

# Objetivos

Al finalizar este laboratorio podrás:

- revisar las licencias disponibles en Microsoft 365;
- preparar usuarios de prueba;
- agregar usuarios al grupo piloto;
- explorar Microsoft Entra ID;
- configurar una política de Conditional Access de forma controlada;
- comprender la relación entre Conditional Access y MFA;
- revisar Smart Lockout y Password Protection;
- asignar un rol administrativo directamente;
- crear un grupo asignable a roles;
- asignar roles mediante el grupo;
- utilizar Microsoft Graph PowerShell para administrar roles;
- validar permisos utilizando una segunda sesión del navegador.

---

# IMPORTANTE - Entorno de laboratorio

Este ejercicio modifica configuraciones de identidad y seguridad.

Utiliza exclusivamente un tenant destinado a capacitación o pruebas.

NO utilices un tenant de producción.

Durante este laboratorio NO aplicaremos políticas de Conditional Access indiscriminadamente a todos los usuarios.

Trabajaremos con cuentas y grupos de prueba para reducir el riesgo de bloquear el acceso administrativo.

---

# Arquitectura del laboratorio

No utilizaremos máquinas virtuales proporcionadas por un proveedor.

Utilizaremos:

PC del alumno
    |
    +-- Navegador principal
    |
    +-- Ventana InPrivate / segundo perfil
    |
    +-- PowerShell
    |
    +-- Microsoft 365 Admin Center
    |
    +-- Microsoft Entra Admin Center

La segunda sesión del navegador permitirá probar configuraciones utilizando otra identidad.

---

# PARTE 1 - Preparar usuarios y licencias

## Task 1 - Revisar las licencias disponibles

Accede a:

https://admin.microsoft.com

Inicia sesión con la cuenta administrativa de tu tenant de práctica.

Navega a:

Billing
>
Licenses

Revisa las suscripciones disponibles.

Identifica:

- nombre de la licencia;
- cantidad total;
- licencias asignadas;
- licencias disponibles.

No asignes ni retires licencias todavía.

> NOTA
> Las licencias disponibles dependerán del tenant utilizado para la capacitación.

---

# Task 2 - Preparar usuarios de laboratorio

Para este laboratorio utilizaremos varias identidades.

Puedes utilizar usuarios de prueba existentes o crear nuevos usuarios.

Se recomienda disponer de al menos:

LAB-Admin

LAB-Pilot

LAB-User1

LAB-User2

LAB-Helpdesk

Los nombres son orientativos.

Si tu tenant ya dispone de usuarios adecuados, puedes reutilizarlos.

---

## Crear un usuario

Desde Microsoft 365 admin center:

Users
>
Active users
>
Add a user

Ejemplo:

First name:

Lab

Last name:

User1

Display name:

LAB-User1

Username:

lab-user1

Selecciona el dominio de tu tenant.

Ejemplo:

lab-user1@contosolab.onmicrosoft.com

---

## Contraseña

Permite que Microsoft genere una contraseña temporal.

Configura:

Require this user to change their password when they first sign in

según las instrucciones del instructor.

No guardes contraseñas dentro del repositorio Git.

---

## Licencias

Si el tenant dispone de licencias suficientes, asigna la licencia indicada por el instructor.

Si no existen licencias disponibles, continúa con las tareas que no dependan de esa licencia.

---

# Task 3 - Agregar un usuario al grupo piloto

Desde:

Teams & groups
>
Active teams & groups

Abre:

M365 Copilot Pilot

Agrega:

LAB-Pilot

como miembro.

Confirma que el usuario aparece dentro del grupo.

---

# PARTE 2 - Microsoft Entra ID

## Task 4 - Abrir Microsoft Entra

Desde Microsoft 365 admin center:

Show all
>
Admin centers
>
Identity

También puedes acceder al Microsoft Entra admin center directamente.

Identifica las áreas:

Identity

Users

Groups

Roles & admins

Protection

No realices cambios todavía.

---

# PARTE 3 - Conditional Access y MFA

## Objetivo

Crearemos una política de laboratorio destinada únicamente a usuarios de prueba.

No aplicaremos inicialmente la política a toda la organización.

---

# Task 5 - Crear un grupo para probar Conditional Access

En Microsoft Entra admin center navega a:

Identity
>
Groups
>
All groups
>
New group

Configura:

Group type:

Security

Group name:

CA-MFA-Lab

Membership type:

Assigned

Agrega como miembro:

LAB-User1

Selecciona:

Create

---

# Task 6 - Crear una política de Conditional Access

Navega a:

Protection
>
Conditional Access
>
Policies

Selecciona:

New policy

Nombre:

LAB - Require MFA

---

## Users

En:

Assignments
>
Users or workload identities

Selecciona:

Select users and groups

Incluye únicamente:

CA-MFA-Lab

IMPORTANTE:

No selecciones All users para este laboratorio.

---

## Target resources

En:

Target resources

Selecciona los recursos indicados por el instructor.

Para un laboratorio controlado puede utilizarse:

All resources

La población afectada continúa limitada al grupo:

CA-MFA-Lab

---

## Conditions

Mantén las condiciones predeterminadas salvo indicación del instructor.

---

## Grant

Selecciona:

Grant access

y configura el requisito de autenticación multifactor disponible en el tenant.

Revisa la configuración antes de continuar.

---

## Enable policy

Durante la primera revisión utiliza:

Report-only

Selecciona:

Create

---

# Task 7 - Revisar la política

Abre:

LAB - Require MFA

Comprueba:

Users:

CA-MFA-Lab

Target resources:

según configuración del laboratorio

Grant:

requisito de MFA

State:

Report-only

---

# Task 8 - Probar con una segunda sesión

No cierres tu sesión administrativa.

Abre:

Microsoft Edge InPrivate

o utiliza un segundo perfil del navegador.

Inicia sesión como:

LAB-User1

Esta segunda sesión sustituye al segundo equipo que podría existir en un laboratorio hospedado.

---

## Qué observar

Como la política se encuentra inicialmente en:

Report-only

el objetivo es revisar su comportamiento sin bloquear inmediatamente al usuario.

El instructor indicará cómo revisar los resultados de inicio de sesión.

---

# Task 9 - Revisar Sign-in logs

Regresa a la sesión administrativa.

En Microsoft Entra navega a:

Identity
>
Monitoring & health
>
Sign-in logs

Busca el inicio de sesión realizado por:

LAB-User1

Abre el evento.

Revisa la información relacionada con:

Conditional Access

y el resultado de la política:

LAB - Require MFA

---

# Task 10 - Activación controlada

Solo si el instructor lo indica y el tenant es exclusivamente de laboratorio:

regresa a:

Protection
>
Conditional Access
>
Policies
>
LAB - Require MFA

Cambia:

Report-only

a:

On

Guarda la política.

---

# Task 11 - Probar MFA

Abre nuevamente una ventana InPrivate.

Inicia sesión como:

LAB-User1

Observa el comportamiento.

Dependiendo de la configuración previa del usuario, Microsoft Entra puede solicitar información adicional para completar MFA.

Sigue las instrucciones del instructor.

---

# Task 12 - Excluir al usuario de la prueba

Después de completar la demostración, el instructor puede indicar:

- volver la política a Report-only;
- quitar LAB-User1 del grupo;
- deshabilitar la política.

El objetivo es dejar el tenant en un estado conocido para los siguientes ejercicios.

---

# PARTE 4 - Smart Lockout y Password Protection

## Task 13 - Abrir Password Protection

En Microsoft Entra admin center navega a:

Protection
>
Authentication methods
>
Password protection

Revisa las opciones disponibles.

Identifica:

Lockout threshold

Lockout duration

Custom banned password list

---

# IMPORTANTE

En este laboratorio Standalone NO modificaremos automáticamente el umbral de bloqueo a valores agresivos.

Tampoco intentaremos bloquear deliberadamente una cuenta administrativa.

El objetivo es comprender la configuración.

---

# Task 14 - Revisar Smart Lockout

Identifica el valor configurado actualmente para:

Lockout threshold

y:

Lockout duration

Anota los valores observados.

No cambies la configuración salvo indicación expresa del instructor.

---

# Task 15 - Revisar Banned Password Protection

Si la funcionalidad está disponible en el tenant, identifica:

Custom banned password list

Revisa cómo una organización puede agregar términos que no desea permitir en contraseñas.

Ejemplos conceptuales:

- nombre de la empresa;
- nombre de un producto;
- nombre de un proyecto interno.

No agregues contraseñas reales.

---

# PARTE 5 - Administrar roles

## Task 16 - Revisar los roles administrativos

En Microsoft Entra admin center navega a:

Identity
>
Roles & admins
>
Roles & admins

Busca algunos roles como:

Global Administrator

User Administrator

Helpdesk Administrator

Billing Administrator

Revisa la descripción de cada uno.

---

# Task 17 - Asignar un rol directamente

Selecciona un usuario de prueba:

LAB-User2

Asigna el rol indicado por el instructor.

Para reproducir el concepto del laboratorio original puede utilizarse:

Billing Administrator

Confirma la asignación.

---

# Principio importante

No todos los administradores necesitan Global Administrator.

Debemos asignar solamente los privilegios necesarios para realizar una función.

---

# PARTE 6 - Grupo asignable a roles

## Task 18 - Crear el grupo

En Microsoft Entra admin center navega a:

Identity
>
Groups
>
All groups
>
New group

Configura:

Group type:

Security

Group name:

User Management Role Group

Busca la opción que permite asignar roles de Microsoft Entra al grupo.

Actívala si está disponible y si tu tenant cumple los requisitos.

Membership type:

Assigned

Agrega:

LAB-Helpdesk

como miembro.

Selecciona:

Create

---

# Task 19 - Asignar roles al grupo

Abre:

User Management Role Group

Revisa las opciones relacionadas con roles asignados.

Asigna los roles indicados por el instructor.

Como referencia para este laboratorio pueden utilizarse:

User Administrator

Helpdesk Administrator

El instructor puede reducir la cantidad de roles para mantener el ejercicio controlado.

---

# Task 20 - Verificar permisos heredados

Abre:

LAB-Helpdesk

Revisa sus roles asignados.

Identifica cuáles obtiene mediante:

User Management Role Group

El objetivo es comprender:

Usuario
    |
    v
Grupo asignable a roles
    |
    v
Rol administrativo
    |
    v
Permisos

---

# PARTE 7 - Microsoft Graph PowerShell

## Task 21 - Conectar a Microsoft Graph

Abre PowerShell.

Ejecuta:

```powershell
Connect-MgGraph -Scopes "User.Read.All","RoleManagement.ReadWrite.Directory"