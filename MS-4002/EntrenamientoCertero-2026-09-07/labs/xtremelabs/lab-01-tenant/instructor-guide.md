# MS-4002 - Lab 01
## Guía del instructor - Inicializar el tenant de Microsoft 365

**Modalidad:** XtremeLabs  
**Curso:** MS-4002 - Prepare security and compliance to support Microsoft 365 Copilot  
**Duración sugerida:** 30-45 minutos

---

# 1. Objetivo

Preparar el entorno XtremeLabs que se utilizará durante el resto del curso.

Al finalizar el alumno debe poder:

- iniciar la VM cliente;
- acceder al Microsoft 365 admin center;
- identificar el tenant asignado;
- crear el grupo piloto;
- revisar Custom themes;
- instalar Microsoft Graph PowerShell;
- validar los módulos requeridos.

---

# 2. Entorno esperado

El laboratorio oficial puede proporcionar:

- LON-CL1 como equipo cliente;
- tenant Microsoft 365 temporal;
- cuenta administrativa MOD Administrator;
- usuarios de prueba precargados;
- dominio con formato similar a xxxxxZZZZZZ.onmicrosoft.com.

Los nombres exactos pueden variar entre instancias.

---

# 3. Antes de comenzar

Pedir a los alumnos que validen:

[OK] XtremeLabs inició correctamente

[OK] LON-CL1 está disponible

[OK] Las credenciales están visibles en la plataforma

[OK] Hay conectividad a Internet

[OK] Microsoft Edge funciona

IMPORTANTE:

No utilizar las credenciales del laboratorio fuera del entorno asignado.

---

# 4. DEMO - Acceso al tenant

## Tiempo sugerido

5 minutos

Desde LON-CL1:

1. Abrir Microsoft Edge.
2. Acceder a:

https://admin.microsoft.com

3. Iniciar sesión con la cuenta administrativa proporcionada.
4. Mostrar el Microsoft 365 admin center.

Explicar que el tenant fue preparado previamente por el proveedor del laboratorio.

---

# 5. Qué explicar

En XtremeLabs no estamos construyendo todo el entorno desde cero.

El proveedor ya entrega:

Tenant
    |
    +-- Usuarios
    |
    +-- Licencias
    |
    +-- VMs
    |
    +-- Credenciales
    |
    +-- Configuración inicial

Esto permite concentrarse en la práctica del curso.

---

# 6. Analogía

"XtremeLabs es como entrar a un laboratorio donde las mesas, computadoras y materiales ya están preparados."

El alumno no necesita construir la infraestructura base.

Solo debe utilizarla correctamente.

---

# 7. DEMO - Grupo piloto

## Tiempo sugerido

10 minutos

Navegar a:

Teams & groups
>
Active teams & groups

Crear:

M365 pilot project

Configurar:

Privacy = Private

Owner = MOD Administrator

Agregar los usuarios de prueba indicados por el instructor.

---

# 8. Qué explicar

El laboratorio oficial puede incluir una cantidad mayor de usuarios precargados.

No es necesario utilizar todos para explicar el concepto.

Para una clase en vivo se puede trabajar con un subconjunto.

Ejemplo:

- 1 propietario;
- 2 o 3 miembros.

El objetivo es comprender el patrón de grupo piloto.

---

# 9. Resultado esperado

Debe existir:

M365 pilot project

con:

- propietario administrativo;
- usuarios miembros;
- privacidad Private.

---

# 10. DEMO - Custom themes

## Tiempo sugerido

5 minutos

Navegar a:

Settings
>
Org settings
>
Organization profile
>
Custom themes

Mostrar:

Add theme

Crear:

M365 pilot project theme

Si está disponible:

- asociar el grupo;
- activar Show the user's display name.

---

# 11. Problema conocido

Custom themes puede:

- tardar en guardar;
- mostrar errores;
- no comportarse igual en todas las instancias.

Si falla:

[INFO] Explicar el concepto.

[INFO] Mostrar la configuración.

[INFO] Continuar con el laboratorio.

No dedicar demasiado tiempo a solucionar esta parte.

---

# 12. DEMO - Microsoft Graph PowerShell

## Tiempo sugerido

10-15 minutos

Desde LON-CL1 abrir PowerShell.

Ejecutar:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser