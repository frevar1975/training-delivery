# DEMO 03 - Microsoft Entra Smart Lockout

## MS-4002 - Module 02: Secure User Access

---

## Duración

5 a 10 minutos

## Tipo

DEMO INSTRUCTOR

## Portal

https://entra.microsoft.com

---

## Objetivo

Mostrar cómo Microsoft Entra Smart Lockout ayuda a proteger las cuentas frente a intentos repetidos de autenticación incorrectos.

Este demo corresponde a la tarea del laboratorio oficial:

```text
Implementación de bloqueo inteligente de Microsoft Entra
```

Al finalizar, el alumno debe comprender:

```text
Failed authentication attempts
        ↓
Microsoft Entra
        ↓
Smart Lockout
        ↓
Temporary account protection
```

---

# 1. Escenario

Contoso está preparando el acceso seguro antes de implementar Microsoft 365 Copilot.

Ya configuramos:

```text
MFA
Conditional Access
```

Pero debemos considerar otro escenario:

```text
¿Qué ocurre si alguien intenta
autenticarse repetidamente
con una contraseña incorrecta?
```

Aquí entra:

```text
Microsoft Entra Smart Lockout
```

---

# 2. Qué problema intenta resolver

Plantear el siguiente escenario:

```text
Attacker
   ↓
Password attempt
   ↓
Password attempt
   ↓
Password attempt
   ↓
Password attempt
```

Sin controles adecuados, los intentos repetitivos pueden formar parte de ataques contra credenciales.

Smart Lockout ayuda a proteger las cuentas frente a este comportamiento.

---

# 3. Entrar a Microsoft Entra

Abrir:

```text
https://entra.microsoft.com
```

Iniciar sesión con la cuenta administrativa del tenant de práctica.

---

# 4. Buscar Password Protection

En Microsoft Entra, localizar la configuración relacionada con:

```text
Authentication methods
Password protection
```

La ubicación exacta puede variar según la experiencia actual del portal.

Si el menú del tenant es diferente, utilizar la búsqueda del portal para localizar:

```text
Password protection
```

---

# 5. Mostrar Smart Lockout

Dentro de Password Protection, identificar las opciones relacionadas con Smart Lockout.

Dependiendo del tenant pueden mostrarse parámetros equivalentes a:

```text
Lockout threshold

Lockout duration
```

---

# 6. Explicar Lockout Threshold

Explicar:

```text
Lockout threshold
```

representa el umbral utilizado por el mecanismo de bloqueo inteligente ante intentos de autenticación incorrectos.

Conceptualmente:

```text
Failed attempt
     ↓
Failed attempt
     ↓
Failed attempt
     ↓
Threshold reached
     ↓
Smart Lockout
```

---

# 7. Explicar Lockout Duration

Mostrar:

```text
Lockout duration
```

Explicar que representa el período asociado al bloqueo cuando se alcanza el comportamiento definido por el servicio.

No es necesario modificar el valor durante la demo.

---

# 8. IMPORTANTE - No demostrarlo bloqueando una cuenta

No realizar una prueba como:

```text
escribir intencionalmente
muchas contraseñas incorrectas
```

sobre:

```text
Global Administrator
```

ni sobre ninguna cuenta necesaria para administrar el laboratorio.

---

## Qué explicar

No necesitamos provocar un bloqueo real para demostrar el concepto.

Podemos mostrar:

```text
Configuration
        +
Concept
        +
Expected behavior
```

sin poner en riesgo el tenant.

---

# 9. No utilizar valores agresivos

Durante esta demo:

```text
NO cambiar el threshold a un valor extremadamente bajo

NO reducir valores solamente para provocar un bloqueo

NO probar con la cuenta administrativa

NO modificar una configuración productiva
```

---

# 10. Analogía

Usar el ejemplo de una tarjeta bancaria.

```text
PIN incorrecto
     ↓
PIN incorrecto
     ↓
PIN incorrecto
     ↓
Temporary protection
```

La idea no es eliminar la cuenta.

La idea es dificultar intentos repetitivos contra las credenciales.

---

# 11. Diferencia con MFA

Explicar:

```text
MFA
=
demostrar la identidad
utilizando un factor adicional
```

Mientras que:

```text
Smart Lockout
=
proteger frente a patrones
de autenticación incorrectos repetidos
```

---

# 12. Diferencia con Conditional Access

Explicar:

```text
Conditional Access
=
decide bajo qué condiciones
se permite o controla el acceso
```

Mientras que:

```text
Smart Lockout
=
protege el proceso de autenticación
frente a intentos repetidos
```

---

# 13. Relacionar los tres controles

Mostrar:

```text
                 Secure Access
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
         MFA     Conditional    Smart
                   Access      Lockout
```

Explicar:

```text
MFA
→ verifica mejor la identidad

Conditional Access
→ decide cuándo aplicar controles

Smart Lockout
→ ayuda a proteger frente a intentos
  repetidos de autenticación incorrecta
```

---

# 14. Relación con el laboratorio oficial

Mostrar que este demo corresponde a:

```text
Ejercicio 1
Administrar el acceso seguro de los usuarios

Tarea 5
Implementación de bloqueo inteligente
de Microsoft Entra
```

La adaptación Standalone prioriza:

```text
revisar
comprender
interpretar
```

la configuración.

No necesitamos provocar un bloqueo real para completar el objetivo didáctico.

---

# 15. Pregunta para la clase

> ¿Por qué no configuramos un threshold extremadamente bajo para ver el bloqueo en vivo?

Respuesta esperada:

```text
Porque podríamos afectar usuarios
o administradores del tenant
innecesariamente.
```

---

# 16. Qué NO hacer

No:

```text
probar contraseñas incorrectas repetidamente

bloquear intencionalmente LAB-Admin

bloquear Global Administrator

usar valores agresivos

modificar configuración productiva

cambiar parámetros únicamente
para obtener una captura
```

---

# 17. Resultado esperado

El alumno debe poder explicar:

```text
¿Qué es Smart Lockout?

¿Qué problema intenta reducir?

¿Qué representa el threshold?

¿Qué representa la duración?

¿En qué se diferencia de MFA?

¿En qué se diferencia de Conditional Access?
```

---

# 18. Mapa final de acceso seguro

```text
User
  |
  v
Authentication
  |
  +---- Password Protection
  |          |
  |          v
  |     Smart Lockout
  |
  +---- MFA
  |
  v
Conditional Access
  |
  v
Microsoft 365
  |
  v
Microsoft 365 Copilot
```

---

# 19. Mensaje clave

> Smart Lockout forma parte de la protección de identidad de Microsoft Entra y ayuda a responder ante intentos repetidos de autenticación incorrecta sin que tengamos que provocar bloqueos artificiales durante el laboratorio.

---

# 20. Cierre

Con este demo quedan cubiertas las cinco tareas del ejercicio de acceso seguro:

```text
1. Usuario de laboratorio
        ✓

2. Grupo M365 Copilot Pilot
        ✓

3. Conditional Access + MFA
        ✓

4. Usuario incluido vs excluido
        ✓

5. Smart Lockout
        ✓
```

Siguiente bloque del curso:

```text
Roles
Permissions
Least Privilege
```