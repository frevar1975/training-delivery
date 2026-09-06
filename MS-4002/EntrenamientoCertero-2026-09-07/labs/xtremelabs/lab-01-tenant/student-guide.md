# MS-4002 - Lab 01
## Inicializar el tenant de Microsoft 365

**Modalidad:** XtremeLabs  
**Entorno:** Laboratorio hospedado  
**Duración estimada:** 30-45 minutos

---

## Objetivos

Al finalizar este laboratorio podrás:

- Acceder al Microsoft 365 admin center.
- Identificar el tenant asignado al laboratorio.
- Crear el grupo piloto de Microsoft 365.
- Explorar las opciones de personalización del tenant.
- Instalar Microsoft Graph PowerShell.
- Verificar los módulos necesarios.

---

# Requisitos

Antes de comenzar confirma que tienes disponibles:

- acceso al entorno XtremeLabs;
- la máquina virtual cliente asignada;
- credenciales del tenant;
- cuenta administrativa;
- acceso a Internet desde la VM.

Las credenciales y nombres exactos pueden variar según la instancia del laboratorio.

No publiques ni compartas contraseñas del entorno.

---

# Task 1 - Acceder al Microsoft 365 Admin Center

## Paso 1 - Iniciar la máquina virtual

Desde XtremeLabs inicia la máquina virtual cliente proporcionada para el laboratorio.

En el entorno oficial normalmente se utiliza:

LON-CL1

Espera hasta que el escritorio esté disponible.

---

## Paso 2 - Abrir Microsoft Edge

En la máquina virtual abre Microsoft Edge.

Accede a:

https://admin.microsoft.com

---

## Paso 3 - Iniciar sesión

Utiliza la cuenta administrativa proporcionada por XtremeLabs.

En muchos entornos del laboratorio esta cuenta aparece como:

MOD Administrator

El nombre de usuario tendrá un dominio similar a:

xxxxxZZZZZZ.onmicrosoft.com

El prefijo exacto será diferente en cada instancia.

---

## Paso 4 - Validar el acceso

Confirma que puedes visualizar:

Microsoft 365 admin center

Expande:

Show all

Identifica:

- Users
- Teams & groups
- Billing
- Settings
- Admin centers

---

# Task 2 - Crear el grupo piloto

## Paso 1 - Abrir grupos

En Microsoft 365 admin center selecciona:

Teams & groups
>
Active teams & groups

Selecciona:

Teams & Microsoft 365 groups

---

## Paso 2 - Crear el grupo

Selecciona:

Add a Microsoft 365 group

Configura:

Name:

M365 pilot project

Description:

Pilot group used during the MS-4002 lab

Privacy:

Private

---

## Paso 3 - Asignar propietario

Selecciona como propietario la cuenta administrativa del laboratorio.

Por ejemplo:

MOD Administrator

---

## Paso 4 - Agregar miembros

Agrega los usuarios de laboratorio indicados por el instructor.

El entorno oficial puede incluir múltiples usuarios precargados.

No es necesario utilizar todos si el instructor ha definido un subconjunto para la clase.

---

## Paso 5 - Crear el grupo

Revisa la configuración y selecciona:

Create group

Espera hasta que aparezca:

M365 pilot project

Utiliza Refresh si es necesario.

---

# Task 3 - Explorar Custom Themes

## Paso 1 - Abrir configuración

Navega a:

Settings
>
Org settings
>
Organization profile
>
Custom themes

---

## Paso 2 - Crear el tema

Si la opción está disponible selecciona:

Add theme

Utiliza:

Name:

M365 pilot project theme

Asocia el tema al grupo:

M365 pilot project

Si está disponible activa:

Show the user's display name

---

## Paso 3 - Guardar

Selecciona:

Save

> NOTA
> En algunos entornos del laboratorio esta configuración puede tardar o puede presentar errores.
> Si no puedes guardar el tema, informa al instructor y continúa con el siguiente ejercicio.

---

# Task 4 - Instalar Microsoft Graph PowerShell

## Paso 1 - Abrir PowerShell

En LON-CL1 abre PowerShell.

---

## Paso 2 - Instalar Microsoft Graph

Ejecuta:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
