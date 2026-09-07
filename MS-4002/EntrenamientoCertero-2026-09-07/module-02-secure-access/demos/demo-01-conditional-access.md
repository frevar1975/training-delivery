# DEMO 01 - Conditional Access y MFA

## MS-4002 - Module 02: Secure User Access

---

## Duración

15 a 20 minutos

## Tipo

DEMO INSTRUCTOR

## Portal

https://entra.microsoft.com

---

## Objetivo

Mostrar cómo Microsoft Entra Conditional Access permite controlar el acceso a Microsoft 365 y exigir MFA de forma segura y gradual.

Al finalizar la demo, el alumno debe comprender:

```text
User / Group
        ↓
Conditional Access
        ↓
Conditions
        ↓
Grant controls
        ↓
Require MFA
```

---

## Escenario

Contoso quiere reforzar el acceso de un pequeño grupo piloto antes de desplegar Microsoft 365 Copilot.

No queremos afectar a todos los usuarios.

Utilizaremos un grupo de laboratorio:

```text
CA-MFA-Lab
```

con un usuario de prueba:

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>
```

---

# 1. Entrar a Microsoft Entra

Abrir:

```text
https://entra.microsoft.com
```

Iniciar sesión con una cuenta administrativa del tenant de práctica.

---

# 2. Ir a Conditional Access

Navegar a:

```text
Protection
→ Conditional Access
→ Policies
```

La ubicación puede variar ligeramente según la experiencia actual del portal.

---

## Qué explicar

Conditional Access funciona como un motor de decisiones.

Conceptualmente:

```text
IF
algo ocurre

THEN
aplicar un control
```

Por ejemplo:

```text
IF
Carlos pertenece a CA-MFA-Lab

AND
accede a Microsoft 365

THEN
Require MFA
```

---

# 3. Recordar el principio de seguridad

Antes de crear una política explicar:

```text
NO comenzar con All users
```

Preferimos:

```text
Test group
        ↓
Report-only
        ↓
Validate
        ↓
Enable when safe
```

---

## Mensaje clave

> Una política correcta técnicamente puede convertirse en un problema operativo si se aplica demasiado ampliamente.

---

# 4. Verificar el grupo de laboratorio

Ir a:

```text
Identity
→ Groups
→ All groups
```

Buscar:

```text
CA-MFA-Lab
```

Abrir el grupo.

---

## Miembro esperado

Para esta demo debería existir:

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>
```

Como miembro del grupo.

---

## Si el grupo no existe todavía

No improvisar una política para toda la organización.

Crear el grupo durante el laboratorio o utilizar un grupo de prueba ya existente.

---

# 5. Crear una política

Volver a:

```text
Protection
→ Conditional Access
→ Policies
```

Seleccionar:

```text
New policy
```

---

# 6. Nombre de la política

Usar exactamente:

```text
LAB - Require MFA
```

---

## Qué explicar

Usamos nombres claros para distinguir:

```text
LAB
TEST
PILOT
PRODUCTION
```

Ejemplo:

```text
LAB - Require MFA
```

es mucho más claro que:

```text
Policy 1
```

---

# 7. Configurar Users

En:

```text
Assignments
→ Users or workload identities
```

seleccionar:

```text
Include
→ Select users and groups
```

Elegir:

```text
CA-MFA-Lab
```

---

## Verificar

Debe quedar:

```text
Included:
CA-MFA-Lab
```

No seleccionar:

```text
All users
```

---

# 8. Explicar exclusiones

Mostrar que Conditional Access permite configurar:

```text
Include
Exclude
```

Explicar que en entornos reales suele ser importante contemplar cuentas administrativas de emergencia según el diseño de seguridad de la organización.

No crear ni modificar cuentas de emergencia durante esta demo.

---

# 9. Configurar Target resources

Ir a:

```text
Target resources
```

Según la interfaz del tenant puede mostrarse como:

```text
Resources
Cloud apps
Target resources
```

---

## Para el laboratorio

Utilizar el alcance disponible que permita demostrar MFA de forma controlada.

Si el tenant ofrece:

```text
All resources
```

explicar que el alcance se limita por el grupo de prueba.

---

## Qué decir

En producción no deberíamos asumir que:

```text
All users
+
All resources
```

es siempre el punto de partida adecuado.

Primero diseñamos el alcance.

---

# 10. Conditions

Mostrar la sección:

```text
Conditions
```

No es necesario modificar condiciones para esta demo.

Explicar que podemos evaluar elementos como:

```text
Sign-in risk
User risk
Device platform
Locations
Client apps
Device state
```

según las capacidades disponibles.

---

# 11. Access controls

Ir a:

```text
Access controls
→ Grant
```

Seleccionar:

```text
Grant access
```

y marcar:

```text
Require multifactor authentication
```

o el control equivalente que muestre la experiencia actual del tenant.

---

## Resultado conceptual

```text
CA-MFA-Lab
       |
       v
Conditional Access
       |
       v
Grant access
       |
       v
Require MFA
```

---

# 12. No activar todavía

En el estado de la política seleccionar:

```text
Report-only
```

No:

```text
On
```

---

## Qué explicar

Report-only nos permite evaluar cómo se comportaría la política sin aplicarla realmente.

Flujo:

```text
Create
   ↓
Report-only
   ↓
Test
   ↓
Review logs
   ↓
Enable
```

---

# 13. Crear la política

Revisar:

```text
Name:
LAB - Require MFA

Users:
CA-MFA-Lab

Grant:
Require MFA

State:
Report-only
```

Seleccionar:

```text
Create
```

---

# 14. Verificar el resultado

La política debería aparecer en la lista:

```text
LAB - Require MFA
```

con estado:

```text
Report-only
```

---

# 15. Explicar qué ocurriría

Plantear:

```text
Carlos
lab-user1@<TU-DOMINIO>
        |
        v
Sign-in
        |
        v
CA-MFA-Lab
        |
        v
LAB - Require MFA
        |
        v
Policy evaluated
```

Como estamos en:

```text
Report-only
```

la política se evalúa pero no debería bloquear ni forzar el cambio de acceso por sí sola.

---

# 16. Usuario de comparación

Recordar que:

```text
Laura Rojas - Test User 2
lab-user2@<TU-DOMINIO>
```

no está inicialmente dentro de:

```text
CA-MFA-Lab
```

Esto permitirá comparar:

```text
Carlos
Policy applies
```

contra:

```text
Laura
Policy does not apply
```

---

# 17. Probar desde una ventana InPrivate

Abrir:

```text
Microsoft Edge
→ New InPrivate window
```

o utilizar otro perfil de navegador.

---

## Usuario

Intentar iniciar sesión con:

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>
```

Acceder, por ejemplo, al portal Microsoft 365 disponible para el laboratorio.

---

# 18. Qué observar

No buscamos provocar un bloqueo.

Buscamos generar un evento de inicio de sesión para después analizarlo.

Explicar:

```text
Authentication attempt
        ↓
Conditional Access evaluation
        ↓
Sign-in log
```

---

# 19. Analogía

Utilizar un aeropuerto:

```text
Usuario
=
pasajero

Password
=
ticket

MFA
=
segunda comprobación de identidad

Conditional Access
=
reglas de seguridad del aeropuerto
```

Ejemplo:

```text
Si viajas a determinada zona
se requiere un control adicional.
```

---

# 20. Diferencia entre MFA y Conditional Access

Explicar:

```text
MFA
=
método de autenticación adicional
```

Mientras que:

```text
Conditional Access
=
motor que decide
cuándo exigir ese método
```

---

## Ejemplo

```text
Conditional Access:
"Este usuario necesita MFA"

MFA:
"Así verificamos la identidad"
```

---

# 21. Relación con Microsoft 365 Copilot

Copilot accede a servicios Microsoft 365 usando la identidad del usuario.

Por eso:

```text
Secure Identity
      ↓
Secure Access
      ↓
Microsoft 365
      ↓
Copilot
```

No debemos pensar en Copilot como una capa independiente de identidad.

---

# 22. Errores frecuentes que explicar

Evitar:

```text
All users sin prueba
```

Evitar:

```text
activar la política directamente
sin validar
```

Evitar:

```text
probar con la cuenta
administrativa principal
```

Evitar:

```text
crear políticas duplicadas
si no vemos efecto inmediato
```

---

# 23. Resultado esperado

Al finalizar debe existir:

```text
Conditional Access Policy

Name:
LAB - Require MFA

Target:
CA-MFA-Lab

Control:
Require MFA

State:
Report-only
```

---

# 24. Qué NO hacer en esta demo

No:

```text
activar una política global
bloquear All users
probar bloqueo de la cuenta admin
modificar Smart Lockout
cambiar políticas productivas
deshabilitar mecanismos de recuperación
```

---

# 25. Mensaje clave

> Conditional Access permite aplicar controles de acceso basados en contexto. La forma segura de implementarlo es comenzar con un alcance pequeño, probar y validar antes de activar.

---

# 26. Transición

Siguiente demo:

```text
DEMO 02
Sign-in Logs y Report-only
```

Ahí utilizaremos el inicio de sesión de Carlos para comprobar:

```text
qué ocurrió
qué política se evaluó
qué resultado tuvo Conditional Access
```