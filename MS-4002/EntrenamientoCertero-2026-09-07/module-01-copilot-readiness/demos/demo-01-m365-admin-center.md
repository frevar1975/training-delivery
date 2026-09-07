# DEMO 01 - Microsoft 365 Admin Center

## MS-4002 - Module 01: Copilot Readiness

---

## Duración

10 minutos

## Tipo

DEMO INSTRUCTOR

## Portal

https://admin.microsoft.com

---

## Objetivo

Mostrar a los alumnos dónde revisar la información básica del tenant antes de comenzar una implementación de Microsoft 365 Copilot.

Al finalizar la demo, el alumno debe poder identificar:

```text
Tenant
Users
Groups
Licenses
```

---

## Escenario

Contoso quiere comenzar un piloto de Microsoft 365 Copilot.

Antes de configurar políticas o asignar licencias debemos revisar:

```text
¿En qué tenant estamos?

¿Qué usuarios existen?

¿Qué grupos existen?

¿Qué licencias están disponibles?
```

---

# 1. Entrar al Microsoft 365 Admin Center

Abrir:

```text
https://admin.microsoft.com
```

Iniciar sesión con la cuenta administrativa del tenant de práctica.

---

## Qué explicar

Microsoft 365 Admin Center es uno de los principales puntos de administración del entorno Microsoft 365.

Desde aquí podemos revisar elementos como:

```text
Users
Groups
Licenses
Settings
Services
```

No es necesario memorizar todos los menús.

El objetivo de esta demo es aprender a orientarnos.

---

# 2. Identificar el tenant

Desde Home, identificar:

```text
Organization / Tenant
```

Si el tenant utiliza un dominio como:

```text
contosolab.onmicrosoft.com
```

mostrarlo a los alumnos.

---

## Pregunta para la clase

> ¿Por qué es importante confirmar en qué tenant estamos antes de realizar una configuración?

Respuesta esperada:

```text
Porque una configuración realizada
en el tenant equivocado puede afectar
usuarios reales o una organización diferente.
```

---

# 3. Revisar los usuarios

Ir a:

```text
Users
→ Active users
```

Mostrar la lista de usuarios existentes.

---

## Qué observar

Identificar:

```text
Display name
Username
Licenses
Sign-in status
```

No modificar ningún usuario todavía.

---

## Usuarios que utilizaremos durante el curso

Explicar que en los laboratorios utilizaremos usuarios de prueba como:

```text
Ana Torres - Copilot Pilot
lab-pilot@<TU-DOMINIO>

Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>

Laura Rojas - Test User 2
lab-user2@<TU-DOMINIO>

Diego Perez - Helpdesk
lab-helpdesk@<TU-DOMINIO>
```

Estos usuarios se crearán o reutilizarán durante los laboratorios.

---

# 4. Explicar por qué usamos usuarios de laboratorio

No debemos realizar las pruebas con:

```text
usuarios productivos
```

ni con:

```text
cuentas personales
```

Preferimos:

```text
Dedicated Lab Users
```

---

## Analogía

Es similar a probar una nueva configuración en:

```text
Test Environment
```

antes de aplicarla en:

```text
Production
```

---

# 5. Revisar los grupos

Ir a:

```text
Teams & groups
→ Active teams & groups
```

Mostrar los grupos existentes.

---

## Qué explicar

Los grupos permiten aplicar configuraciones de manera controlada.

Durante el curso utilizaremos:

```text
M365 Copilot Pilot
```

como grupo piloto.

Y posteriormente:

```text
CA-MFA-Lab
```

para limitar las pruebas de Conditional Access.

---

# 6. Ejemplo de grupo piloto

Mostrar conceptualmente:

```text
All Employees
     |
     X
     |
     v

M365 Copilot Pilot
     |
     v
Small controlled group
```

---

## Mensaje

No comenzamos una adopción de Copilot con:

```text
All Users
```

Preferimos:

```text
Pilot Group
```

---

# 7. Revisar las licencias

Ir a:

```text
Billing
→ Licenses
```

o al área equivalente disponible en el tenant.

---

## Qué mostrar

Identificar las licencias disponibles.

No asignar ni quitar licencias durante esta demo.

---

## Qué explicar

Las capacidades disponibles pueden depender de:

```text
Licensing
```

Por eso antes de diseñar un laboratorio debemos saber qué tiene disponible el tenant.

---

# 8. Pregunta para la clase

> Si una función no aparece en nuestro tenant, ¿significa necesariamente que Microsoft la eliminó?

Respuesta esperada:

```text
No.
```

Puede depender de:

```text
License
Permissions
Tenant configuration
Rollout
Portal experience
```

---

# 9. Volver a Home

Regresar a:

```text
Home
```

y resumir.

---

# 10. Resumen visual

```text
Microsoft 365 Admin Center

        |
        +---- Users
        |
        +---- Groups
        |
        +---- Licenses
        |
        +---- Settings
```

---

# 11. Conexión con Copilot Readiness

Explicar:

```text
Before Copilot
     |
     v
Understand the tenant
     |
     v
Understand users
     |
     v
Understand groups
     |
     v
Understand licensing
```

---

# 12. Mensaje clave

> Antes de implementar Microsoft 365 Copilot debemos comprender el entorno Microsoft 365 sobre el que vamos a trabajar.

---

# 13. Qué NO hacer en esta demo

No:

```text
crear usuarios todavía
asignar licencias
eliminar usuarios
cambiar configuración global
```

Esta demo es únicamente de orientación.

---

# 14. Resultado esperado

El alumno puede responder:

```text
¿Dónde veo los usuarios?

¿Dónde veo los grupos?

¿Dónde reviso las licencias?

¿En qué tenant estoy?
```

---

# 15. Transición

Siguiente demo:

```text
DEMO 02
Microsoft Entra Overview
```

Ahí veremos:

```text
Identity
Groups
Conditional Access
Roles
```