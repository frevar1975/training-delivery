# Module 04 - Microsoft 365 Apps

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Comprender por qué Microsoft 365 Apps forma parte de la preparación para Microsoft 365 Copilot y qué debe revisar un administrador antes del despliegue.

Hasta ahora vimos:

```text
Identity
   |
   v
Secure Access
   |
   v
Roles & Permissions
```

Ahora incorporamos:

```text
Microsoft 365 Apps
```

---

# 2. Punto de partida

Los usuarios interactúan con Microsoft 365 y Copilot a través de distintas aplicaciones y experiencias.

Ejemplos:

```text
Word
Excel
PowerPoint
Outlook
Teams
Microsoft 365
```

Por eso no basta con preparar únicamente:

```text
Tenant + Users + Licenses
```

También debemos preparar el entorno de aplicaciones.

---

# 3. Analogía

Una empresa compra un nuevo sistema, pero las computadoras de los usuarios tienen versiones diferentes del software.

```text
PC 1 -> versión actual
PC 2 -> versión antigua
PC 3 -> configuración diferente
PC 4 -> actualización pendiente
```

Aunque el servicio esté disponible en la nube, la experiencia del usuario puede variar.

La administración de Microsoft 365 Apps busca reducir estas diferencias.

---

# 4. Microsoft 365 Apps for enterprise

Microsoft 365 Apps for enterprise proporciona las aplicaciones de productividad utilizadas por los usuarios.

Entre ellas:

```text
Word
Excel
PowerPoint
Outlook
```

Estas aplicaciones se conectan con servicios Microsoft 365 como:

```text
Exchange Online
SharePoint Online
OneDrive
Microsoft Teams
```

---

# 5. Aplicaciones y servicios

Es importante diferenciar:

```text
APPLICATION
```

de:

```text
SERVICE
```

Ejemplo:

```text
Word
   |
   v
Application

OneDrive / SharePoint
   |
   v
Cloud services
```

La experiencia Microsoft 365 combina ambos.

---

# 6. Relación con Copilot

Conceptualmente:

```text
User
  |
  v
Microsoft 365 App
  |
  v
Microsoft 365 Services
  |
  v
User context + permissions
  |
  v
Copilot experience
```

Por ello las aplicaciones deben formar parte de la planificación del despliegue.

---

# 7. Qué debe revisar el administrador

Antes de un despliegue amplio debemos considerar:

```text
Licensing
    |
    v
Applications
    |
    v
Versions / Updates
    |
    v
Configuration
    |
    v
Pilot
    |
    v
Deployment
```

---

# 8. Actualizaciones

Las aplicaciones Microsoft 365 evolucionan continuamente.

Una organización necesita una estrategia para administrar:

```text
Updates
```

y evitar escenarios donde cada equipo se encuentre en un estado diferente.

---

# 9. Analogía de actualizaciones

Imagina una flota de vehículos.

Si cada vehículo utiliza:

```text
motor diferente
repuestos diferentes
mantenimiento diferente
```

administrar la flota se vuelve más complejo.

Una estrategia de actualización busca mantener un entorno administrable y predecible.

---

# 10. Update Channels

Microsoft 365 Apps puede utilizar diferentes estrategias o canales de actualización.

El punto didáctico no es memorizar todos los nombres.

El alumno debe comprender:

```text
Update strategy
      |
      v
Feature availability
      +
Change velocity
      +
Testing
      +
Support
```

---

# 11. Pilot users

Las actualizaciones también pueden probarse inicialmente con un grupo reducido.

Conceptualmente:

```text
New capability
      |
      v
Pilot users
      |
      v
Validate
      |
      v
Broader deployment
```

Este patrón ya apareció en Module 01.

---

# 12. El patrón Pilot

Podemos reutilizar:

```text
M365 Copilot Pilot
```

como concepto organizativo.

La idea general es:

```text
Small group
   |
   v
Test
   |
   v
Collect feedback
   |
   v
Fix issues
   |
   v
Expand
```

---

# 13. DEMO INSTRUCTOR - Microsoft 365 Admin Center

Abrir:

```text
Microsoft 365 Admin Center
```

Mostrar las áreas relacionadas con:

```text
Users
Licensing
Settings
Admin centers
```

El objetivo es conectar:

```text
User
+
License
+
Services
+
Apps
```

---

# 14. DEMO INSTRUCTOR - Usuario y licencias

Seleccionar un usuario LAB.

Mostrar la sección de:

```text
Licenses and apps
```

o su equivalente actual en el portal.

Explicar que asignar una licencia puede habilitar diferentes servicios para el usuario.

No modificar licencias productivas.

---

# 15. Ejemplo

Usuario:

```text
LAB-User1
```

Antes de utilizarlo en un piloto debemos revisar:

```text
Account
+
License
+
Required services
+
Applications
+
Access
```

---

# 16. DEMO INSTRUCTOR - Microsoft 365 Apps Admin Center

Si el tenant dispone de acceso, mostrar el centro administrativo utilizado para administrar Microsoft 365 Apps.

No es necesario realizar un despliegue completo.

Mostrar conceptualmente áreas relacionadas con:

```text
Inventory
Servicing
Customization
Configuration
```

según las opciones disponibles en el tenant.

---

# 17. Inventario

Una organización necesita conocer su entorno.

Preguntas:

```text
¿Qué aplicaciones tenemos?

¿Qué versiones?

¿Qué dispositivos?

¿Qué canales?

¿Qué estado de actualización?
```

Sin inventario es difícil planificar un despliegue controlado.

---

# 18. Analogía del inventario

Antes de renovar una flota empresarial primero preguntamos:

```text
¿Cuántos vehículos existen?

¿Qué modelos?

¿Qué antigüedad?

¿Qué estado tienen?
```

Lo mismo ocurre con las aplicaciones.

Primero:

```text
Understand current state
```

Después:

```text
Plan target state
```

---

# 19. Caso práctico

Contoso quiere habilitar nuevas experiencias Microsoft 365 para:

```text
2,000 users
```

Pero descubre:

```text
Different Office versions
Different update strategies
Old devices
Different configurations
```

No debería comenzar simplemente con:

```text
Deploy to everyone
```

Primero:

```text
Inventory
   |
   v
Pilot
   |
   v
Validate
   |
   v
Standardize
   |
   v
Deploy
```

---

# 20. Aplicaciones web como alternativa para laboratorios

En nuestro entorno Standalone utilizamos principalmente:

```text
Browser
+
Microsoft 365 web apps
```

Esto reduce la dependencia de:

```text
Office desktop installation
```

durante los laboratorios.

Ejemplo:

```text
Word for the Web
```

será utilizado para probar Sensitivity Labels.

---

# 21. Ventaja para la clase

Utilizando aplicaciones web:

```text
Alumno
   |
   v
Browser
   |
   v
Microsoft 365
```

evitamos depender de que todos tengan exactamente la misma instalación local de Office.

---

# 22. Limitación

La experiencia puede no ser idéntica entre:

```text
Web
Desktop
Mobile
```

Algunas funcionalidades pueden aparecer o comportarse de forma diferente.

Por eso durante la clase debemos distinguir:

```text
Concept
```

de:

```text
Exact UI
```

---

# 23. Seguridad y aplicaciones

Preparar aplicaciones también implica considerar controles como:

```text
Authentication
Access
Updates
Policies
Information Protection
```

Las aplicaciones son uno de los puntos desde los cuales los usuarios interactúan con la información corporativa.

---

# 24. Relación con Sensitivity Labels

Posteriormente veremos:

```text
Word
  |
  v
Document
  |
  v
Sensitivity
  |
  v
PII
```

Por eso necesitamos que las aplicaciones puedan trabajar correctamente con las capacidades de protección de información utilizadas por la organización.

---

# 25. Relación con DLP

También veremos:

```text
Outlook / Teams / SharePoint / OneDrive
                |
                v
               DLP
```

Las políticas de seguridad y cumplimiento interactúan con los servicios y experiencias que utilizan los usuarios.

---

# 26. Qué NO vamos a hacer en este módulo

No necesitamos realizar:

```text
mass deployment
```

ni:

```text
tenant-wide Office configuration
```

ni:

```text
production update channel changes
```

durante la clase.

El objetivo es comprender el papel de Microsoft 365 Apps dentro de la preparación.

---

# 27. Pregunta de comprobación

Preguntar:

> Si todos los usuarios tienen licencia de Microsoft 365 pero utilizan aplicaciones y configuraciones diferentes, ¿podemos asumir que todos tendrán exactamente la misma experiencia?

Respuesta:

```text
No
```

Debemos considerar:

```text
Applications
Versions
Updates
Configuration
```

---

# 28. Caso de decisión

Tenemos dos opciones:

```text
A)
Deploy immediately to 2,000 users

B)
Pilot with selected users,
validate apps and experience,
then expand
```

¿Cuál sigue el enfoque que venimos utilizando durante el curso?

```text
B
```

---

# 29. Mensaje clave

El alumno debe recordar:

> Preparar Microsoft 365 Copilot también implica preparar las aplicaciones y experiencias desde las cuales trabajarán los usuarios.

Modelo:

```text
Identity
+
Access
+
Apps
+
Information
=
Copilot Readiness
```

---

# 30. Transición al siguiente módulo

Hasta ahora hemos preparado:

```text
WHO
 |
 v
Identity

HOW
 |
 v
Secure Access

WHAT THEY CAN ADMINISTER
 |
 v
Roles

WHERE THEY WORK
 |
 v
Microsoft 365 Apps
```

Ahora comenzamos con:

```text
WHAT HAPPENS TO THE DATA?
```

Siguiente módulo:

```text
Module 05
Data Loss Prevention
```

Aquí entraremos en Microsoft Purview y veremos:

```text
Sensitive Information
      |
      v
DLP
      |
      +---- Detect
      +---- Notify
      +---- Block
      +---- Override
      +---- Monitor
```