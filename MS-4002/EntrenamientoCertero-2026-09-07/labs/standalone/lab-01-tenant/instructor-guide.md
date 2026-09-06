# MS-4002 - Lab 01
## Guía del instructor - Preparar el tenant de Microsoft 365

**Modalidad:** Standalone  
**Curso:** MS-4002 - Prepare security and compliance to support Microsoft 365 Copilot  
**Duración sugerida:** 35-45 minutos

---

# 1. Propósito del laboratorio

Este laboratorio prepara el entorno que se utilizará durante las prácticas posteriores del curso.

El objetivo no es profundizar todavía en Microsoft 365 Copilot, Microsoft Entra o Microsoft Purview.

El objetivo es comprobar que el alumno dispone de un entorno administrativo funcional.

Al finalizar debemos tener:

- acceso administrativo al tenant;
- dominio del tenant identificado;
- grupo piloto creado;
- usuarios de prueba disponibles;
- Microsoft Graph PowerShell instalado;
- módulos necesarios disponibles.

---

# 2. Antes de comenzar

## Validación del instructor

Antes de iniciar la práctica pregunta:

1. ¿Todos pueden iniciar sesión en su tenant?
2. ¿Todos tienen una cuenta administrativa?
3. ¿El tenant es de laboratorio y no de producción?
4. ¿Tienen usuarios de prueba disponibles?
5. ¿Tienen PowerShell disponible?

IMPORTANTE:

No realizar las prácticas en un tenant de producción.

---

# 3. Introducción para explicar en clase

## Concepto

Antes de implementar controles de seguridad y cumplimiento para Microsoft 365 Copilot necesitamos preparar y conocer el entorno.

Durante el curso trabajaremos principalmente con:

- Microsoft 365 admin center;
- Microsoft Entra;
- Microsoft Purview;
- Microsoft Graph PowerShell.

## Analogía

Puedes explicar:

"Antes de instalar sistemas de seguridad en un edificio necesitamos saber qué edificio estamos administrando, quién tiene las llaves y quiénes son las personas que pueden ingresar."

En este laboratorio:

Tenant = edificio

Administrador = persona con las llaves principales

Usuarios = personas que utilizan el edificio

Grupos = conjuntos de personas con características comunes

Microsoft Graph = interfaz que nos permite administrar Microsoft 365 mediante automatización

---

# 4. DEMO - Acceder al Microsoft 365 Admin Center

## Tiempo sugerido

5 minutos

## Instructor muestra

Abrir:

https://admin.microsoft.com

Iniciar sesión con una cuenta administrativa del tenant de práctica.

Mostrar:

Microsoft 365 admin center

Expandir:

Show all

Mostrar rápidamente:

Users

Teams & groups

Billing

Settings

Admin centers

---

# 5. Qué explicar

No debemos memorizar todos los portales.

Microsoft 365 utiliza diferentes centros de administración especializados.

Explicar la relación:

Microsoft 365 admin center
        |
        +-- Users
        |
        +-- Groups
        |
        +-- Microsoft Entra
        |
        +-- Microsoft Purview
        |
        +-- SharePoint
        |
        +-- Teams
        |
        +-- Exchange

Microsoft 365 admin center funciona como punto de entrada administrativo.

---

# 6. Punto de control

Pedir a los alumnos que identifiquen:

- cuenta administrativa;
- nombre del tenant;
- dominio del tenant.

Ejemplo:

admin@contosolab.onmicrosoft.com

Explicar:

onmicrosoft.com identifica el dominio inicial asociado al tenant.

---

# 7. DEMO - Grupo piloto de Microsoft 365 Copilot

## Tiempo sugerido

10 minutos

Mostrar:

Teams & groups
>
Active teams & groups
>
Teams & Microsoft 365 groups

Crear:

M365 Copilot Pilot

Descripción:

Users participating in the Microsoft 365 Copilot pilot project

Privacy:

Private

Agregar:

- administrador como propietario;
- al menos dos usuarios de prueba como miembros.

---

# 8. Qué explicar

## ¿Por qué utilizar un grupo piloto?

Una implementación empresarial de Copilot normalmente no debería comenzar tratando a toda la organización como una única población.

Un grupo piloto permite trabajar inicialmente con un conjunto controlado de usuarios.

Durante el curso este grupo representará a los usuarios que participan en nuestra implementación de prueba.

## Analogía

"Antes de desplegar una nueva aplicación a 10.000 empleados, podemos probarla con 20 usuarios."

El grupo nos proporciona una población controlada sobre la cual probar configuraciones.

---

# 9. Resultado esperado

Debe aparecer:

M365 Copilot Pilot

con:

Owner >= 1

Members >= 2

Privacy = Private

---

# 10. Problemas posibles

## El grupo no aparece inmediatamente

Usar:

Refresh

Esperar algunos segundos/minutos.

## El alumno no tiene usuarios

No detener todo el laboratorio.

Puede:

- utilizar usuarios de prueba existentes;
- continuar con el grupo y agregar usuarios posteriormente;
- solicitar al instructor usuarios de laboratorio.

---

# 11. DEMO - Custom themes

## Tiempo sugerido

5 minutos

Mostrar:

Settings
>
Org settings
>
Organization profile
>
Custom themes

Explicar las opciones disponibles.

Si el tenant permite realizar la configuración, crear:

M365 Copilot Pilot Theme

Asociarlo al grupo:

M365 Copilot Pilot

No dedicar demasiado tiempo a:

- logos;
- colores;
- branding.

El objetivo es mostrar que Microsoft 365 puede personalizar experiencias para grupos determinados.

---

# 12. Plan B - Custom themes

Esta funcionalidad puede comportarse de forma diferente dependiendo del tenant.

Si:

- no aparece;
- no permite guardar;
- muestra un error;
- tarda demasiado;

NO detener la clase.

Mostrar conceptualmente la configuración y continuar.

Custom themes no es requisito para completar los laboratorios posteriores.

---

# 13. DEMO - Microsoft Graph PowerShell

## Tiempo sugerido

10-15 minutos

Explicar primero:

El portal gráfico es útil para operaciones interactivas.

PowerShell es especialmente útil cuando necesitamos:

- automatizar;
- repetir operaciones;
- administrar muchos objetos;
- ejecutar configuraciones de forma consistente.

---

# 14. Instalar Microsoft Graph

Mostrar PowerShell.

Ejecutar:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser