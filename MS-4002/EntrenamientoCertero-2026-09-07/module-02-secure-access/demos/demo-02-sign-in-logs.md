# DEMO 02 - Sign-in Logs y Report-only

## MS-4002 - Module 02: Secure User Access

---

## Duración

10 a 15 minutos

## Tipo

DEMO INSTRUCTOR

## Portal

https://entra.microsoft.com

---

## Objetivo

Mostrar cómo validar el resultado de una política de Conditional Access utilizando los Sign-in Logs de Microsoft Entra.

Al finalizar la demo, el alumno debe comprender cómo relacionar:

```text
User sign-in
        ↓
Sign-in log
        ↓
Conditional Access
        ↓
Policy evaluation
```

---

## Escenario

En la demo anterior creamos:

```text
LAB - Require MFA
```

con estado:

```text
Report-only
```

y dirigido al grupo:

```text
CA-MFA-Lab
```

El usuario de prueba es:

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>
```

Ahora queremos comprobar si la política fue evaluada.

---

# 1. Generar un inicio de sesión

Abrir una ventana:

```text
Microsoft Edge
→ New InPrivate window
```

o utilizar un segundo perfil de navegador.

---

## Iniciar sesión con

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>
```

Acceder a un recurso Microsoft 365 disponible en el tenant.

Por ejemplo:

```text
https://www.microsoft365.com
```

o cualquier aplicación Microsoft 365 disponible para el laboratorio.

---

## Qué explicar

La intención no es bloquear al usuario.

Queremos generar un evento que podamos analizar.

Conceptualmente:

```text
Carlos
   ↓
Sign-in
   ↓
Microsoft Entra
   ↓
Conditional Access evaluation
   ↓
Sign-in Log
```

---

# 2. Volver a Microsoft Entra

Abrir:

```text
https://entra.microsoft.com
```

con la cuenta administrativa.

---

# 3. Abrir Sign-in Logs

Ir a:

```text
Monitoring & health
→ Sign-in logs
```

La ubicación puede variar ligeramente según la experiencia actual del portal.

---

# 4. Buscar el usuario

Filtrar por usuario.

Buscar:

```text
Carlos Mendoza - Test User 1
```

o:

```text
lab-user1@<TU-DOMINIO>
```

---

## Qué observar

Localizar el inicio de sesión realizado hace unos minutos.

Revisar columnas como:

```text
Date
User
Application
Status
IP address
Conditional Access
```

---

# 5. Abrir el evento

Seleccionar el inicio de sesión correspondiente.

Se abrirá el detalle del evento.

---

## Qué explicar

Un Sign-in Log nos ayuda a responder preguntas como:

```text
¿Quién inició sesión?

¿Cuándo?

¿A qué aplicación?

¿Desde qué dirección IP?

¿El acceso fue exitoso?

¿Qué políticas se evaluaron?

¿Se solicitó MFA?
```

---

# 6. Revisar información básica

Dentro del evento revisar secciones equivalentes a:

```text
Basic info
Location
Device info
Authentication details
Conditional Access
```

No es necesario revisar absolutamente todos los campos.

---

# 7. Revisar Status

Mostrar el estado del inicio de sesión.

Puede aparecer como:

```text
Success
```

o un resultado diferente dependiendo de la prueba.

---

## Qué explicar

Un inicio de sesión exitoso no significa que Conditional Access no haya sido evaluado.

La política está en:

```text
Report-only
```

Por eso puede evaluarse sin bloquear el acceso.

---

# 8. Abrir Conditional Access

Dentro del evento buscar la sección:

```text
Conditional Access
```

o la pestaña equivalente.

---

## Buscar la política

Identificar:

```text
LAB - Require MFA
```

---

# 9. Revisar el resultado

La experiencia del portal puede mostrar estados equivalentes a:

```text
Report-only: Success

Report-only: Failure

Not applied

Success

Failure
```

El valor exacto dependerá del evento y de la configuración del tenant.

---

## Qué explicar

Lo importante es entender:

```text
Was the policy evaluated?
```

y:

```text
What would have happened
if the policy were enabled?
```

---

# 10. Interpretar Report-only

Explicar:

```text
Policy state:
Report-only
```

significa que Microsoft Entra evalúa la política pero no aplica el control como una política activa.

Conceptualmente:

```text
Real sign-in
      ↓
Evaluate policy
      ↓
Calculate result
      ↓
Record result
      ↓
Do not enforce
```

---

# 11. Comparar con Laura

Si hay tiempo, realizar una segunda prueba con:

```text
Laura Rojas - Test User 2
lab-user2@<TU-DOMINIO>
```

Laura inicialmente NO debe pertenecer a:

```text
CA-MFA-Lab
```

---

## Resultado conceptual esperado

Carlos:

```text
Carlos
  ↓
CA-MFA-Lab
  ↓
LAB - Require MFA
  ↓
Policy evaluated
```

Laura:

```text
Laura
  ↓
Not member of CA-MFA-Lab
  ↓
Policy not applicable
```

---

# 12. Mostrar el valor de los grupos

Explicar por qué utilizamos:

```text
CA-MFA-Lab
```

en vez de seleccionar usuarios directamente.

Flujo:

```text
User
   ↓
Group
   ↓
Policy
```

Esto facilita:

```text
Pilot
Testing
Administration
Scaling
```

---

# 13. Revisar Authentication Details

Abrir:

```text
Authentication Details
```

o la sección equivalente.

---

## Qué observar

Dependiendo del inicio de sesión se puede ver información relacionada con:

```text
Authentication requirement
Authentication method
MFA
Primary authentication
Additional verification
```

---

## Qué explicar

No todos los eventos mostrarán exactamente la misma información.

Depende de:

```text
Tenant configuration
Authentication flow
Existing session
MFA registration
Conditional Access
```

---

# 14. Ejemplo de sesión existente

Explicar este punto porque puede ocurrir durante una demo:

```text
El usuario ya inició sesión anteriormente
        ↓
Existe una sesión válida
        ↓
El comportamiento puede ser diferente
```

Por eso usamos:

```text
InPrivate
```

o un segundo perfil de navegador.

---

# 15. Analogía

Usar un control de seguridad de un edificio.

```text
Conditional Access
=
regla de seguridad
```

Mientras que:

```text
Sign-in Logs
=
registro del guardia
```

El registro permite revisar:

```text
Quién entró
A qué hora
Qué regla se evaluó
Qué ocurrió
```

---

# 16. Relación con troubleshooting

Plantear este caso:

```text
Usuario:
"No puedo iniciar sesión"
```

No empezamos cambiando configuraciones al azar.

Primero revisamos:

```text
Sign-in Logs
```

Luego podemos investigar:

```text
Authentication
Conditional Access
MFA
Device
Location
Policy
```

---

# 17. Pregunta para la clase

> Creamos una política y el usuario dice que no funciona. ¿Qué revisarías primero?

Respuesta esperada:

```text
Sign-in Logs
```

y específicamente:

```text
Conditional Access evaluation
```

---

# 18. De Report-only a producción

Mostrar el flujo recomendado:

```text
Create policy
      ↓
Report-only
      ↓
Generate sign-ins
      ↓
Review Sign-in Logs
      ↓
Validate scope
      ↓
Correct configuration if needed
      ↓
Enable progressively
```

---

## Qué explicar

No debemos pasar directamente de:

```text
idea
```

a:

```text
production enforcement
```

sin observar el comportamiento.

---

# 19. Relación con Microsoft 365 Copilot

Copilot utiliza la identidad y permisos del usuario.

Por eso necesitamos poder observar:

```text
User
  ↓
Authentication
  ↓
Conditional Access
  ↓
Microsoft 365 access
  ↓
Copilot
```

Si existen problemas de acceso, los Sign-in Logs son una de las principales fuentes de diagnóstico.

---

# 20. Qué NO hacer en esta demo

No:

```text
activar la política para All users

bloquear usuarios reales

modificar políticas productivas

eliminar políticas existentes

cambiar MFA de administradores

forzar configuraciones solo para obtener
un resultado visual específico
```

---

# 21. Resultado esperado

El alumno debe poder:

```text
abrir Sign-in Logs

buscar un usuario

abrir un evento

identificar Conditional Access

localizar LAB - Require MFA

entender Report-only
```

---

# 22. Plan B - No aparece el evento

Si el inicio de sesión todavía no aparece:

```text
1. Esperar unos minutos

2. Actualizar Sign-in Logs

3. Confirmar el usuario utilizado

4. Realizar un nuevo inicio de sesión InPrivate

5. Continuar con capturas o explicación conceptual
   y volver a revisar más tarde
```

No crear nuevas políticas por no ver inmediatamente el resultado.

---

# 23. Plan B - Conditional Access no muestra la política

Revisar:

```text
¿Carlos pertenece a CA-MFA-Lab?

¿La política está creada?

¿Está en Report-only?

¿El recurso del inicio de sesión
entra dentro del alcance?

¿Estamos mirando el evento correcto?
```

---

# 24. Mensaje clave

> Configurar una política es solo la mitad del trabajo. También debemos comprobar cómo fue evaluada y entender su impacto antes de activarla.

---

# 25. Cierre de Module 02 para Clase 1

Hasta este punto vimos:

```text
Identity
   ↓
Authentication
   ↓
MFA
   ↓
Conditional Access
   ↓
Sign-in Logs
```

---

# 26. Cierre de la Clase 1

Conectar todo lo visto:

```text
Microsoft 365 Admin Center
        ↓
Tenant readiness
        ↓
Microsoft Entra
        ↓
Identity
        ↓
Conditional Access
        ↓
MFA
        ↓
Sign-in Logs
```

La próxima clase continuará con:

```text
Roles
Least Privilege
Microsoft 365 Apps
Data Protection
```