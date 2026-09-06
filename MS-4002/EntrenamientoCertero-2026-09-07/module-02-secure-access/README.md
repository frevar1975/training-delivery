# Module 02 - Secure User Access

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Comprender cómo proteger el acceso de los usuarios a Microsoft 365 antes de ampliar el uso de Microsoft 365 Copilot.

El flujo principal será:

```text
User
  |
  v
Identity
  |
  v
Authentication
  |
  v
Conditional Access
  |
  v
Microsoft 365
  |
  v
Copilot
```

La pregunta principal del módulo es:

```text
¿Cómo sabemos que la persona
que intenta acceder realmente
debería poder hacerlo?
```

---

# 2. Punto de partida

Microsoft 365 Copilot trabaja dentro del contexto del usuario.

Por eso debemos proteger primero:

```text
IDENTITY
```

Antes de preocuparnos por Copilot debemos revisar:

- usuarios;
- autenticación;
- MFA;
- políticas de acceso;
- protección de contraseñas;
- intentos de autenticación.

---

# 3. Analogía

Imagina un edificio corporativo.

Tener un empleado registrado en Recursos Humanos no significa que pueda entrar libremente a cualquier lugar.

Tenemos varias capas:

```text
Empleado
   |
   v
Credencial
   |
   v
Control de entrada
   |
   v
Validación adicional
   |
   v
Acceso
```

En Microsoft 365 podemos relacionarlo con:

```text
User
   |
   v
Password
   |
   v
MFA
   |
   v
Conditional Access
   |
   v
Microsoft 365
```

---

# 4. Microsoft Entra ID

Microsoft Entra ID proporciona la plataforma de identidad y acceso utilizada por Microsoft 365.

Conceptualmente:

```text
Microsoft Entra ID
        |
        +---- Users
        |
        +---- Groups
        |
        +---- Authentication
        |
        +---- Conditional Access
        |
        +---- Roles
```

Durante este módulo nos concentramos principalmente en:

```text
Authentication
+
Secure Access
```

---

# 5. Identidad vs autenticación vs autorización

Es importante diferenciar estos conceptos.

## Identity

```text
¿Quién eres?
```

Ejemplo:

```text
LAB-User1
```

## Authentication

```text
¿Puedes demostrar que eres LAB-User1?
```

Ejemplos:

```text
Password
MFA
```

## Authorization

```text
¿Qué puedes hacer después de autenticarte?
```

Ejemplos:

```text
Read SharePoint
Access Teams
Administer users
```

---

# 6. Analogía

En un aeropuerto:

```text
Pasaporte
   =
Identity

Control del pasaporte
   =
Authentication

Boarding pass
   =
Authorization
```

No son lo mismo.

---

# 7. Por qué importa para Copilot

Supongamos que un atacante obtiene:

```text
username + password
```

Si puede iniciar sesión como el usuario, potencialmente podrá acceder a los recursos Microsoft 365 disponibles para esa identidad.

Por eso:

```text
Protect Identity
      |
      v
Protect Microsoft 365
      |
      v
Protect Copilot access
```

---

# 8. Multi-Factor Authentication

MFA agrega otro factor de autenticación.

En lugar de depender únicamente de:

```text
Something you know
```

podemos incorporar:

```text
Something you have
```

o:

```text
Something you are
```

---

# 9. Ejemplo

Sin MFA:

```text
Username
   +
Password
   =
Access
```

Con MFA:

```text
Username
   +
Password
   +
Additional verification
   =
Access
```

---

# 10. Analogía de MFA

Una caja fuerte puede requerir:

```text
Llave
+
Código
```

Robar solamente la llave ya no es suficiente.

MFA aplica un principio similar a la autenticación.

---

# 11. MFA no responde todas las preguntas

MFA puede ayudar a comprobar la identidad, pero todavía podemos necesitar evaluar:

```text
¿Desde dónde se conecta?

¿Qué aplicación utiliza?

¿Qué recurso intenta abrir?

¿Qué riesgo existe?

¿Qué condiciones deben cumplirse?
```

Aquí entra:

```text
Conditional Access
```

---

# 12. Conditional Access

Conditional Access permite evaluar señales y aplicar controles antes de conceder acceso.

Modelo conceptual:

```text
SIGNALS
   |
   v
CONDITIONS
   |
   v
DECISION
   |
   v
ACCESS CONTROL
```

---

# 13. Explicación simple

Conditional Access funciona como:

```text
IF
    determinadas condiciones
THEN
    aplicar determinado control
```

Ejemplo:

```text
IF
User belongs to pilot group

THEN
Require MFA
```

---

# 14. Analogía

En un edificio:

```text
Empleado llega
      |
      v
Seguridad revisa:
      |
      +---- quién es
      +---- dónde quiere entrar
      +---- horario
      +---- credencial
      |
      v
Permitir / Denegar / Verificación adicional
```

Conditional Access aplica un concepto parecido al acceso digital.

---

# 15. Componentes conceptuales

Una política puede considerar elementos como:

```text
Assignments
     |
     +---- Users
     +---- Groups
     +---- Resources
     |
Conditions
     |
     +---- Device
     +---- Location
     +---- Risk
     +---- Client
     |
Access Controls
     |
     +---- Block
     +---- Require MFA
     +---- Other controls
```

Las opciones exactas dependen de las capacidades disponibles en el tenant.

---

# 16. Ejemplo de política

Para el laboratorio utilizaremos conceptualmente:

```text
LAB - Require MFA
```

Aplicada únicamente a:

```text
CA-MFA-Lab
```

Resultado:

```text
LAB-User1
     |
     v
CA-MFA-Lab
     |
     v
Conditional Access
     |
     v
Require MFA
```

---

# 17. Por qué usamos un grupo de laboratorio

No queremos crear inicialmente:

```text
All Users
    |
    v
Require MFA
```

durante una clase.

En su lugar:

```text
Test User
    |
    v
Test Group
    |
    v
Test Policy
```

Esto reduce el riesgo.

---

# 18. Regla para demos de Conditional Access

Durante una clase:

```text
SMALL SCOPE
+
TEST USERS
+
REPORT-ONLY FIRST
```

Evitar realizar cambios amplios en un tenant compartido.

---

# 19. Report-only

Report-only permite evaluar qué habría ocurrido si la política estuviera activa, sin aplicar inmediatamente el control.

Conceptualmente:

```text
Sign-in
   |
   v
Conditional Access
   |
   v
Evaluate Policy
   |
   v
Report Result
```

sin necesariamente aplicar el bloqueo/control al usuario.

---

# 20. Analogía de Report-only

Antes de instalar una nueva barrera de seguridad en la entrada de una empresa podemos observar:

```text
¿A quién habría detenido?

¿A quién habría permitido entrar?
```

sin cerrar todavía la puerta.

Ese es el valor conceptual de:

```text
Report-only
```

---

# 21. DEMO INSTRUCTOR - Microsoft Entra

Abrir:

```text
Microsoft Entra admin center
```

Mostrar:

```text
Identity
   |
   +---- Users
   +---- Groups
   +---- Protection
```

No modificar todavía configuraciones globales.

---

# 22. DEMO INSTRUCTOR - Users

Mostrar:

```text
Identity > Users
```

Seleccionar un usuario de laboratorio.

Explicar que desde la identidad podemos revisar información relacionada con:

- cuenta;
- grupos;
- roles;
- autenticación;
- actividad.

---

# 23. DEMO INSTRUCTOR - Groups

Mostrar:

```text
Identity > Groups
```

Explicar la diferencia conceptual entre:

```text
Users
```

y:

```text
Groups
```

Los grupos permiten administrar controles sobre conjuntos de identidades.

---

# 24. Ejemplo de administración por grupos

En lugar de:

```text
Policy -> Freddy
Policy -> Ana
Policy -> Pedro
Policy -> María
```

podemos utilizar:

```text
Users
   |
   v
CA-MFA-Lab
   |
   v
Policy
```

Esto facilita la administración.

---

# 25. DEMO INSTRUCTOR - Conditional Access

Mostrar el área de:

```text
Conditional Access
```

Identificar:

```text
Policies
```

Abrir una política existente solamente si es seguro hacerlo.

Mostrar conceptualmente:

```text
Assignments
Conditions
Target resources
Access controls
```

---

# 26. No activar una política global durante la explicación

Evitar utilizar durante una demo:

```text
All users
+
All resources
+
Block access
```

Una configuración incorrecta puede afectar incluso cuentas administrativas.

---

# 27. Break-glass / Emergency Access

Explicar conceptualmente que una organización debe considerar cuentas de acceso de emergencia dentro de su estrategia de identidad.

No crear ni modificar una cuenta de emergencia durante esta demo.

El objetivo es que el alumno entienda que:

```text
Conditional Access
```

requiere planificación antes de una implementación amplia.

---

# 28. Sign-in Logs

Una parte fundamental de la validación es revisar:

```text
Sign-in logs
```

Conceptualmente:

```text
User
   |
   v
Sign-in
   |
   v
Conditional Access evaluation
   |
   v
Logs
```

Los logs ayudan a comprender qué ocurrió durante un intento de acceso.

---

# 29. DEMO INSTRUCTOR - Sign-in Logs

Mostrar:

```text
Microsoft Entra
>
Sign-in logs
```

Seleccionar un inicio de sesión de laboratorio si existe.

Mostrar campos relevantes disponibles en el portal.

Especialmente:

```text
Conditional Access
```

cuando corresponda.

---

# 30. Caso práctico

Usuario:

```text
LAB-User1
```

Política:

```text
LAB - Require MFA
```

Estado:

```text
Report-only
```

El usuario inicia sesión.

Preguntar:

```text
¿Cómo sabemos qué habría hecho la política?
```

Respuesta:

```text
Sign-in logs
```

---

# 31. Smart Lockout

Smart Lockout ayuda a proteger las cuentas frente a intentos repetidos de autenticación incorrectos.

Conceptualmente:

```text
Repeated failed attempts
        |
        v
Smart Lockout
        |
        v
Account protection
```

---

# 32. Analogía

Imagina un cajero automático.

Si alguien introduce un PIN incorrecto muchas veces:

```text
Intento
Intento
Intento
Intento
```

el sistema no debería permitir intentos ilimitados.

Smart Lockout aplica un principio de protección frente a intentos de autenticación sospechosos o repetitivos.

---

# 33. DEMO INSTRUCTOR - Smart Lockout

Mostrar dónde se administra la configuración correspondiente si el tenant y los permisos lo permiten.

Durante la clase:

```text
REVISAR
```

no necesariamente:

```text
MODIFICAR
```

No utilizar valores agresivos simplemente para provocar un bloqueo.

---

# 34. Password Protection

Microsoft Entra Password Protection ayuda a impedir el uso de contraseñas débiles o conocidas como inseguras.

Conceptualmente:

```text
User chooses password
        |
        v
Password Protection
        |
        +---- Allowed
        |
        +---- Rejected
```

---

# 35. Analogía

No basta con exigir:

```text
8 caracteres
1 mayúscula
1 número
```

si el usuario termina utilizando algo predecible.

La protección moderna de contraseñas busca reducir el uso de contraseñas débiles o demasiado comunes.

---

# 36. DEMO INSTRUCTOR - Password Protection

Mostrar la configuración disponible.

Explicar:

```text
Global banned password list
```

y, cuando corresponda:

```text
Custom banned password list
```

No modificar la configuración global del tenant durante la explicación salvo que sea un entorno exclusivamente de laboratorio.

---

# 37. Ejemplo empresarial

Empresa:

```text
Contoso
```

Tiene 2.000 usuarios.

Problemas:

```text
Password-only authentication
No Conditional Access
Legacy accounts
Weak password practices
```

La empresa quiere desplegar Copilot.

Orden lógico:

```text
Review identities
      |
      v
Strengthen authentication
      |
      v
Implement access controls
      |
      v
Validate
      |
      v
Expand Copilot
```

---

# 38. Relación con Lab 02

Este módulo prepara la primera parte de:

```text
Standalone Lab 02
Identities, Security and Roles
```

El alumno podrá practicar:

```text
Users
  |
  v
Groups
  |
  v
Conditional Access
  |
  v
MFA
  |
  v
Sign-in validation
```

El mismo laboratorio continuará posteriormente con roles y permisos.

---

# 39. Qué dejamos para Module 03

No profundizar todavía en:

```text
Billing Administrator
User Administrator
Helpdesk Administrator
Role-assignable groups
Microsoft Graph role assignment
```

Eso pertenece a:

```text
Module 03 - Roles and Permissions
```

---

# 40. Mini comprobación

Preguntar:

> ¿Qué diferencia existe entre MFA y Conditional Access?

Respuesta conceptual:

```text
MFA
=
Método/control adicional de autenticación

Conditional Access
=
Motor de políticas que evalúa condiciones
y decide qué controles aplicar
```

---

# 41. Segunda comprobación

Preguntar:

> ¿Por qué comenzamos una política de laboratorio en Report-only?

Respuesta:

```text
Para evaluar su impacto antes
de aplicar el control.
```

---

# 42. Mensaje clave

El alumno debe recordar:

> Antes de proteger Copilot debemos proteger la identidad que accede a Microsoft 365.

Modelo:

```text
Secure Identity
      |
      v
Secure Access
      |
      v
Secure Microsoft 365
      |
      v
Safer Copilot adoption
```

---

# 43. Transición

Cerrar con:

```text
Ya sabemos QUIÉN entra
y CÓMO protegemos el acceso.

Ahora debemos decidir:

¿QUÉ PUEDE HACER después de entrar?
```

Siguiente:

```text
Module 03
Roles and Permissions
```