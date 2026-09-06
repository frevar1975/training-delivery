# MS-4002 - Lab 01
## Preparar el tenant de Microsoft 365

**Modalidad:** Standalone  
**Entorno:** Tenant Microsoft 365 de práctica  
**Duración estimada:** 30-45 minutos

---

## Objetivos

Al finalizar este laboratorio podrás:

- Acceder al centro de administración de Microsoft 365.
- Validar que tienes acceso administrativo al tenant.
- Identificar el dominio del tenant que utilizarás durante el curso.
- Crear un grupo de Microsoft 365 para el proyecto piloto.
- Explorar las opciones de personalización de Microsoft 365.
- Instalar Microsoft Graph PowerShell.
- Validar la instalación de los módulos requeridos.

---

# Requisitos

Necesitas:

- Un equipo con Windows.
- Microsoft Edge o un navegador compatible.
- Acceso a Internet.
- Un tenant Microsoft 365 de práctica.
- Una cuenta con permisos administrativos.
- PowerShell.

> IMPORTANTE  
> No realices estos ejercicios en un tenant de producción.
> Utiliza exclusivamente un tenant destinado a capacitación o pruebas.

---

# Task 1 - Acceder al Microsoft 365 Admin Center

## Paso 1 - Abrir Microsoft 365

Abre Microsoft Edge.

Accede al portal de Microsoft 365:

https://portal.office.com

Inicia sesión utilizando la cuenta administrativa proporcionada para el laboratorio.

Ejemplo:

admin@contosolab.onmicrosoft.com

Tu dominio será diferente.

---

## Paso 2 - Identificar la cuenta utilizada

Una vez iniciada la sesión, observa el usuario que aparece en la esquina superior derecha.

Confirma que estás utilizando la cuenta administrativa destinada al laboratorio.

Anota:

- Usuario:
- Dominio del tenant:
- Nombre del tenant:

No anotes la contraseña en este documento.

---

## Paso 3 - Abrir el centro de administración

Desde Microsoft 365 selecciona:

Apps > Admin

También puedes acceder directamente a:

https://admin.microsoft.com

Debe abrirse el Microsoft 365 admin center.

---

## Paso 4 - Explorar el centro de administración

En el panel izquierdo selecciona:

Show all

Identifica las siguientes áreas:

- Users
- Teams & groups
- Billing
- Settings
- Admin centers

No realices cambios todavía.

### Punto de control

Antes de continuar debes poder:

- Acceder al Microsoft 365 admin center.
- Identificar tu tenant.
- Identificar tu cuenta administrativa.
- Visualizar las opciones administrativas.

---

# Task 2 - Crear el grupo del proyecto piloto

Durante el curso utilizaremos un grupo para representar a los usuarios que participan en el proyecto piloto de Microsoft 365 Copilot.

## Paso 1 - Abrir grupos

En Microsoft 365 admin center selecciona:

Teams & groups > Active teams & groups

Selecciona:

Teams & Microsoft 365 groups

---

## Paso 2 - Crear el grupo

Selecciona:

Add a Microsoft 365 group

Configura:

Name:

M365 Copilot Pilot

Description:

Users participating in the Microsoft 365 Copilot pilot project

Selecciona:

Next

---

## Paso 3 - Asignar propietario

Selecciona:

Assign owners

Agrega la cuenta administrativa que estás utilizando para el laboratorio.

Continúa con:

Next

---

## Paso 4 - Agregar miembros

Selecciona:

Add members

Agrega al menos dos usuarios de prueba disponibles en tu tenant.

Si todavía no existen usuarios de prueba suficientes, consulta con el instructor antes de continuar.

Selecciona:

Next

---

## Paso 5 - Configurar el grupo

Configura:

Group email address:

m365copilotpilot

Privacy:

Private

Si aparece la opción para crear un Team asociado al grupo, puedes dejarla desactivada para este laboratorio.

Selecciona:

Next

---

## Paso 6 - Crear el grupo

Revisa la configuración.

Selecciona:

Create group

Cuando termine:

Close

El grupo puede tardar algunos minutos en aparecer.

Utiliza:

Refresh

hasta visualizar:

M365 Copilot Pilot

### Punto de control

Debes tener un grupo:

M365 Copilot Pilot

con:

- un propietario;
- al menos dos usuarios de prueba;
- privacidad Private.

---

# Task 3 - Explorar la personalización de Microsoft 365

## Paso 1 - Abrir la configuración organizacional

En Microsoft 365 admin center selecciona:

Settings > Org settings

Selecciona:

Organization profile

Busca:

Custom themes

---

## Paso 2 - Explorar los temas

Abre:

Custom themes

Revisa las opciones disponibles para personalizar:

- nombre;
- grupos;
- logotipos;
- colores;
- nombre visible del usuario.

Si tu tenant permite crear un tema personalizado, selecciona:

Add theme

Nombre:

M365 Copilot Pilot Theme

Asocia:

M365 Copilot Pilot

Si está disponible, activa:

Show the user's display name

---

## Paso 3 - Explorar branding

Revisa las pestañas:

Logos

Colors

No es necesario cargar imágenes corporativas para completar el laboratorio.

Puedes conservar los valores predeterminados.

---

## Paso 4 - Guardar

Selecciona:

Save

> NOTA  
> La disponibilidad y el comportamiento de Custom themes pueden variar según el tenant.
> Si el tema no puede guardarse, continúa con el laboratorio.

---

# Task 4 - Instalar Microsoft Graph PowerShell

Microsoft Graph PowerShell permitirá realizar tareas administrativas desde PowerShell.

## Paso 1 - Abrir PowerShell

Abre PowerShell.

Para esta instalación utilizaremos el contexto del usuario actual.

---

## Paso 2 - Instalar Microsoft Graph

Ejecuta:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
