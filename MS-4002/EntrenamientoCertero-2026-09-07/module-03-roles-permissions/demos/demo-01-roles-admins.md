# DEMO 01 - Roles administrativos y Least Privilege

## MS-4002 - Module 03: Roles and Permissions

---

## Duración

15 a 20 minutos

## Tipo

DEMO INSTRUCTOR

## Portales

```text
Microsoft Entra Admin Center
https://entra.microsoft.com

Microsoft 365 Admin Center
https://admin.microsoft.com
```

---

## Objetivo

Mostrar cómo Microsoft 365 y Microsoft Entra utilizan roles administrativos para delegar tareas sin entregar permisos innecesarios.

Al finalizar la demo, el alumno debe comprender:

```text
User
   ↓
Role Assignment
   ↓
Administrative Permission
   ↓
Specific Task
```

---

## Escenario

Contoso necesita que una persona del equipo de soporte pueda realizar tareas operativas.

El usuario será:

```text
Diego Perez - Helpdesk
lab-helpdesk@<TU-DOMINIO>
```

Diego necesita realizar tareas de soporte.

No necesita administrar todo el tenant.

Por lo tanto, NO queremos asignarle:

```text
Global Administrator
```

Nuestro objetivo es demostrar:

```text
Least Privilege
```

---

# 1. Introducir el problema

Plantear a los alumnos:

```text
Diego trabaja en Helpdesk.

Necesita ayudar a usuarios.

¿Le damos Global Administrator?
```

Respuesta esperada:

```text
No.
```

---

## Qué explicar

Un administrador debería recibir únicamente los permisos necesarios para realizar su función.

Esto se conoce como:

```text
Principle of Least Privilege
```

---

# 2. Analogía

Usar el ejemplo de un hotel.

```text
Global Administrator
=
Master Key

Helpdesk Administrator
=
Llave para determinadas habitaciones o tareas
```

No entregamos:

```text
Master Key
```

a cada empleado.

---

# 3. Entrar a Microsoft Entra

Abrir:

```text
https://entra.microsoft.com
```

Iniciar sesión con la cuenta administrativa del tenant de práctica.

---

# 4. Ir a Roles and administrators

Navegar a:

```text
Entra ID
→ Roles & admins
```

o utilizar la búsqueda del portal para:

```text
Roles and administrators
```

---

## Qué explicar

Desde aquí podemos ver los roles administrativos disponibles en Microsoft Entra.

Ejemplos:

```text
Global Administrator

User Administrator

Helpdesk Administrator

Password Administrator

Billing Administrator
```

Los roles disponibles y algunas capacidades pueden depender del tenant y de las licencias.

---

# 5. Buscar Global Administrator

Buscar:

```text
Global Administrator
```

Abrir el rol.

---

## Qué mostrar

Mostrar que se trata de un rol altamente privilegiado.

No agregar ningún usuario.

---

## Qué explicar

Global Administrator tiene un alcance muy amplio.

Por eso no debe convertirse en:

```text
"el rol que usamos cuando algo no funciona"
```

---

# 6. Buscar Helpdesk Administrator

Volver a:

```text
Roles & admins
```

Buscar:

```text
Helpdesk Administrator
```

Abrir el rol.

---

## Qué explicar

Un rol especializado permite delegar tareas administrativas sin entregar control total del tenant.

La idea es:

```text
Business task
      ↓
Required permission
      ↓
Least privileged role
```

---

# 7. Verificar el usuario de laboratorio

Ir a:

```text
Entra ID
→ Users
→ All users
```

Buscar:

```text
Diego Perez - Helpdesk
```

o:

```text
lab-helpdesk@<TU-DOMINIO>
```

---

## Resultado esperado

Debe existir:

```text
Display name:
Diego Perez - Helpdesk

Username:
lab-helpdesk@<TU-DOMINIO>
```

---

# 8. Revisar roles asignados al usuario

Abrir el usuario:

```text
Diego Perez - Helpdesk
```

Buscar la sección:

```text
Assigned roles
```

La ubicación exacta puede variar según la experiencia del portal.

Microsoft Entra permite revisar los roles asignados directamente o mediante grupos. :contentReference[oaicite:1]{index=1}

---

# 9. Mostrar que Diego inicialmente no tiene privilegios administrativos

Idealmente:

```text
Diego
   ↓
Standard User
```

Explicar:

```text
Authentication
≠
Administrative authorization
```

Que Diego pueda iniciar sesión no significa que pueda administrar el tenant.

---

# 10. Asignar un rol administrativo de laboratorio

Para la demo utilizaremos:

```text
Helpdesk Administrator
```

Volver a:

```text
Entra ID
→ Roles & admins
→ Helpdesk Administrator
```

Seleccionar la opción equivalente a:

```text
Add assignments
```

---

# 11. Seleccionar el usuario

Buscar:

```text
Diego Perez - Helpdesk
```

o:

```text
lab-helpdesk@<TU-DOMINIO>
```

Seleccionarlo.

---

# 12. Revisar antes de confirmar

Mostrar:

```text
User:
Diego Perez - Helpdesk

Role:
Helpdesk Administrator
```

---

## Qué explicar

Antes de confirmar una asignación debemos responder:

```text
¿Quién recibe el permiso?

¿Qué rol recibe?

¿Por qué lo necesita?

¿Cuál es el alcance?
```

---

# 13. Confirmar la asignación

Completar la asignación utilizando la opción disponible en el portal.

El nombre del botón puede variar:

```text
Assign
Add
Save
```

---

# 14. Validar la asignación

Volver al usuario:

```text
Entra ID
→ Users
→ Diego Perez - Helpdesk
→ Assigned roles
```

Confirmar que aparece:

```text
Helpdesk Administrator
```

---

# 15. Mapa conceptual

Mostrar:

```text
Diego Perez
    |
    v
Helpdesk Administrator
    |
    v
Limited administrative capabilities
```

Comparar con:

```text
Diego Perez
    |
    v
Global Administrator
    |
    v
Excessive privileges
```

---

# 16. Mostrar alternativa desde Microsoft 365 Admin Center

Abrir:

```text
https://admin.microsoft.com
```

Ir a:

```text
Users
→ Active users
```

Seleccionar:

```text
Diego Perez - Helpdesk
```

Buscar:

```text
Manage roles
```

o la sección equivalente.

---

## Qué explicar

Microsoft 365 Admin Center también permite asignar roles administrativos desde el usuario o desde:

```text
Roles
→ Role assignments
```

Microsoft documenta ambos métodos: desde el usuario y desde la lista de roles. :contentReference[oaicite:2]{index=2}

---

# 17. Mostrar Roles > Role assignments

En Microsoft 365 Admin Center ir a:

```text
Roles
→ Role assignments
```

Mostrar las categorías disponibles.

Dependiendo del tenant pueden aparecer áreas como:

```text
Microsoft Entra ID
Exchange
Intune
Billing
```

---

# 18. Explicar que no todos los roles son iguales

Ejemplos conceptuales:

```text
User Administrator
→ administración de usuarios

Helpdesk Administrator
→ determinadas tareas de soporte

Billing Administrator
→ tareas relacionadas con facturación

Global Administrator
→ administración de alto privilegio
```

---

# 19. Pregunta para la clase

> Un usuario necesita resetear determinadas credenciales o ayudar con tareas de soporte. ¿Le asignamos Global Administrator?

Respuesta esperada:

```text
No.
```

Primero buscamos:

```text
el rol menos privilegiado
que permita realizar la tarea
```

---

# 20. Roles directos vs roles mediante grupos

Explicar que una asignación puede ser:

```text
User
  ↓
Role
```

o conceptualmente:

```text
User
  ↓
Role-assignable group
  ↓
Role
```

Microsoft Entra permite asignar roles tanto a usuarios como a grupos, según las capacidades y requisitos del tenant. :contentReference[oaicite:3]{index=3}

---

# 21. Introducir Role-Assignable Groups

Explicar:

En organizaciones mayores podemos administrar privilegios mediante grupos diseñados para recibir roles.

Ejemplo:

```text
Diego
  ↓
User Management Role Group
  ↓
User Administrator
```

Esto permite administrar membresías en lugar de realizar muchas asignaciones individuales.

---

## Importante

No crear todavía un grupo role-assignable si el tenant no cumple los requisitos o si no es necesario para esta demo.

Se puede mostrar conceptualmente o realizarlo dentro del laboratorio correspondiente.

---

# 22. Validar con un segundo navegador

Abrir:

```text
Edge
→ New InPrivate window
```

Iniciar sesión como:

```text
Diego Perez - Helpdesk
lab-helpdesk@<TU-DOMINIO>
```

---

# 23. Mostrar una tarea permitida

Dependiendo de la experiencia y permisos disponibles en el tenant:

```text
abrir Microsoft 365 Admin Center
```

o:

```text
Microsoft Entra Admin Center
```

Mostrar que Diego ahora tiene acceso a determinadas tareas administrativas.

---

# 24. Mostrar el límite del rol

Intentar navegar a una sección que no corresponda al alcance del rol.

No ejecutar cambios.

Solo mostrar conceptualmente que:

```text
Administrative role
≠
Full tenant control
```

---

## Qué explicar

Una buena demo de Least Privilege debe mostrar dos cosas:

```text
1. Lo que el usuario SÍ puede hacer

2. Lo que el usuario NO puede hacer
```

---

# 25. Ejemplo real

Plantear:

```text
Empresa con 2,000 empleados
```

Equipo:

```text
Global Admins
Security Admins
Helpdesk
Billing
User Management
```

Una mala práctica sería:

```text
todos = Global Administrator
```

Una mejor práctica:

```text
persona
  ↓
función laboral
  ↓
rol necesario
```

---

# 26. Relación con Zero Trust

Explicar:

Least Privilege forma parte de un enfoque de seguridad basado en:

```text
Verify explicitly

Use least privilege access

Assume breach
```

Para roles administrativos, Microsoft recomienda asignaciones Just-In-Time y Just-Enough-Access cuando las capacidades correspondientes están disponibles. :contentReference[oaicite:4]{index=4}

---

# 27. Relación con Microsoft 365 Copilot

Copilot no elimina la necesidad de administrar permisos.

Al contrario:

```text
Copilot
   ↓
Microsoft 365 data
   ↓
User identity
   ↓
Permissions
```

Y la administración de Copilot también requiere controlar quién puede:

```text
configure
manage
deploy
govern
```

servicios y políticas.

---

# 28. Diferenciar permisos administrativos de permisos sobre contenido

Explicar claramente:

```text
Admin Role
```

no es lo mismo que:

```text
Permission to a SharePoint file
```

Ejemplo:

```text
Helpdesk Administrator
```

puede tener determinadas capacidades administrativas.

Eso no significa automáticamente que pueda abrir:

```text
Salaries.xlsx
```

en SharePoint.

---

# 29. Pregunta importante

> ¿Ser administrador significa automáticamente tener acceso a todos los documentos de Microsoft 365?

Respuesta esperada:

```text
No necesariamente.
```

Diferenciar:

```text
Administrative authorization
```

de:

```text
Content permissions
```

---

# 30. Qué NO hacer en esta demo

No:

```text
asignar Global Administrator a Diego

eliminar roles existentes

modificar cuentas administrativas reales

cambiar permisos de producción

asignar roles a todos los usuarios

realizar cambios que no puedan revertirse
```

---

# 31. Resultado esperado

Al finalizar debe existir una demostración de:

```text
Diego Perez - Helpdesk
        ↓
Helpdesk Administrator
        ↓
Limited administrative capabilities
```

El alumno debe comprender:

```text
Role
Least Privilege
Direct assignment
Role-based administration
Administrative scope
```

---

# 32. Opcional - Cleanup

Si el tenant es compartido y queremos dejarlo como estaba:

```text
Entra ID
→ Users
→ Diego Perez - Helpdesk
→ Assigned roles
```

Quitar:

```text
Helpdesk Administrator
```

solo si la asignación fue creada exclusivamente para la demo y ya no será utilizada en el laboratorio.

---

# 33. Mensaje clave

> No debemos asignar el rol más poderoso para resolver una tarea pequeña. Primero identificamos la responsabilidad y después asignamos el rol mínimo necesario.

---

# 34. Transición

Siguiente demo:

```text
DEMO 02
Microsoft Graph PowerShell
```

Ahí veremos cómo consultar y administrar:

```text
Users
Roles
Role definitions
Role assignments
```

desde PowerShell.