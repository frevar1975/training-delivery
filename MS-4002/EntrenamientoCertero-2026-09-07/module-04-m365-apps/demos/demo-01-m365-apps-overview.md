# DEMO 01 - Microsoft 365 Apps Overview

## MS-4002 - Module 04: Microsoft 365 Apps for Enterprise

---

## Duración

10 a 15 minutos

## Tipo

DEMO INSTRUCTOR

## Portales

```text
Microsoft 365 Admin Center
https://admin.microsoft.com

Microsoft 365 Apps Admin Center
https://config.office.com
```

---

## Objetivo

Mostrar dónde revisar y administrar Microsoft 365 Apps dentro del entorno empresarial y explicar por qué las aplicaciones también forman parte de la preparación para Microsoft 365 Copilot.

Al finalizar la demo, el alumno debe comprender:

```text
License
   ↓
Microsoft 365 Apps
   ↓
Deployment
   ↓
Update strategy
   ↓
User experience
   ↓
Copilot readiness
```

---

## Escenario

Contoso está preparando un piloto de Microsoft 365 Copilot.

Ya revisamos:

```text
Identity
MFA
Conditional Access
Roles
Permissions
```

Ahora surge otra pregunta:

```text
¿Los usuarios tienen las aplicaciones
y versiones adecuadas para trabajar?
```

---

# 1. Introducir el problema

Plantear:

```text
Usuario tiene licencia
        ↓
Pero tiene aplicaciones desactualizadas
        ↓
Experiencia inconsistente
```

o:

```text
Usuario trabaja solo con Office local antiguo
        ↓
No recibe las mismas capacidades
        ↓
Problemas de compatibilidad
```

---

## Qué explicar

Preparar Microsoft 365 Copilot no consiste solamente en:

```text
tener usuarios
```

o:

```text
asignar una licencia
```

También debemos revisar:

```text
Applications
Versions
Updates
Deployment
Configuration
```

---

# 2. Abrir Microsoft 365 Admin Center

Abrir:

```text
https://admin.microsoft.com
```

Iniciar sesión con la cuenta administrativa del tenant de práctica.

---

# 3. Revisar licencias

Ir a:

```text
Billing
→ Licenses
```

Mostrar las licencias disponibles en el tenant.

No asignar ni retirar licencias durante esta demo.

---

## Qué explicar

Las licencias determinan qué servicios y aplicaciones puede utilizar un usuario.

Pero:

```text
License
≠
Application deployment
```

Tener una licencia no significa necesariamente que la aplicación esté instalada o actualizada.

---

# 4. Revisar un usuario de prueba

Ir a:

```text
Users
→ Active users
```

Seleccionar, por ejemplo:

```text
Ana Torres - Copilot Pilot
lab-pilot@<TU-DOMINIO>
```

Revisar la sección relacionada con:

```text
Licenses and apps
```

---

## Qué mostrar

Identificar conceptualmente:

```text
Assigned license
Enabled services
Available applications
```

No cambiar nada.

---

# 5. Explicar aplicación vs servicio cloud

Usar esta comparación:

```text
Word Desktop
=
Application

Exchange Online
=
Cloud Service

OneDrive
=
Cloud Service

SharePoint Online
=
Cloud Service

Teams
=
Application + Cloud Service
```

---

## Mensaje

Microsoft 365 es una combinación de:

```text
Local applications
        +
Cloud services
```

Copilot trabaja dentro de ese ecosistema.

---

# 6. Mostrar Microsoft 365 Apps Admin Center

Abrir:

```text
https://config.office.com
```

Si el tenant permite acceso, iniciar sesión con la cuenta administrativa.

---

## Qué explicar

Microsoft 365 Apps Admin Center permite administrar aspectos relacionados con las aplicaciones de Microsoft 365.

Dependiendo del tenant y las capacidades disponibles, pueden aparecer áreas relacionadas con:

```text
Inventory

Servicing

Health

Customization

Cloud Policy
```

---

# 7. Mostrar Inventory

Buscar la sección:

```text
Inventory
```

Si está disponible.

---

## Qué explicar

Inventory ayuda a responder preguntas como:

```text
¿Qué aplicaciones están instaladas?

¿Qué versiones existen?

¿Qué dispositivos tienen Office?

¿Qué build están utilizando?
```

---

# 8. Explicar por qué importa la versión

Plantear:

```text
100 usuarios
```

con:

```text
5 versiones diferentes de Office
```

El resultado puede ser:

```text
Support complexity
Compatibility issues
Inconsistent features
Difficult troubleshooting
```

---

# 9. Update Channels

Mostrar conceptualmente los canales de actualización.

No es necesario cambiar ningún canal durante la demo.

Explicar que una organización puede definir distintas estrategias de actualización.

Ejemplos conceptuales:

```text
Current Channel

Monthly Enterprise Channel

Semi-Annual Enterprise Channel
```

Los nombres y disponibilidad pueden variar con el tiempo.

---

## Qué explicar

El canal determina:

```text
cuándo recibe actualizaciones
una instalación de Microsoft 365 Apps
```

---

# 10. Analogía

Usar teléfonos móviles.

```text
Todos tienen el mismo modelo
```

pero algunos utilizan:

```text
Software version 1
Software version 2
Software version 3
```

La experiencia puede cambiar.

Lo mismo ocurre con aplicaciones empresariales.

---

# 11. Mostrar Health o Servicing

Si está disponible, mostrar:

```text
Health
```

o:

```text
Servicing
```

No realizar cambios.

---

## Qué explicar

Antes de un despliegue importante queremos conocer:

```text
Application health

Update status

Compatibility

Deployment state
```

---

# 12. Explicar estrategia de piloto

Relacionar con lo visto anteriormente:

```text
M365 Copilot Pilot
```

La misma lógica de piloto se puede aplicar a aplicaciones.

Conceptualmente:

```text
Small group
     ↓
Validate
     ↓
Collect feedback
     ↓
Expand deployment
```

---

# 13. Aplicaciones web como alternativa de laboratorio

Explicar:

En un entorno Standalone no siempre podremos instalar Microsoft 365 Apps en cada equipo.

Podemos utilizar:

```text
Word for the web

Excel for the web

PowerPoint for the web

Outlook on the web
```

para demostrar capacidades de Microsoft 365.

---

## Ventaja

Esto reduce dependencia de:

```text
specific local installation

specific Office version

lab VM image
```

---

# 14. Relación con Word, Excel, PowerPoint y Outlook

Mostrar conceptualmente:

```text
Microsoft 365 Apps
        |
        +---- Word
        |
        +---- Excel
        |
        +---- PowerPoint
        |
        +---- Outlook
        |
        +---- Teams
```

---

# 15. Relación con información corporativa

Las aplicaciones son donde los usuarios:

```text
create
edit
share
consume
```

información.

Por eso se conectan directamente con los siguientes módulos:

```text
DLP

Sensitivity Labels
```

---

# 16. Ejemplo práctico

Usuario crea en Word:

```text
EmployeeData.docx
```

Luego puede:

```text
Save in OneDrive

Share through SharePoint

Send through Outlook

Discuss through Teams
```

La protección de ese contenido no depende solo de Word.

Intervienen:

```text
Permissions

DLP

Sensitivity Labels

Sharing policies
```

---

# 17. Conexión con DLP

Explicar:

```text
Microsoft 365 App
      ↓
User creates content
      ↓
Content moves through M365
      ↓
DLP evaluates information
```

---

# 18. Conexión con Sensitivity Labels

Explicar:

```text
Document
   ↓
Sensitivity Label
   ↓
Classification
   ↓
Protection
```

Las etiquetas pueden aparecer dentro de las aplicaciones de Microsoft 365 cuando la configuración y licenciamiento lo permiten.

---

# 19. Relación con Microsoft 365 Copilot

Copilot puede integrarse en experiencias de Microsoft 365.

Por lo tanto, necesitamos pensar en:

```text
Identity

License

Application

Cloud data

Permissions

Security

Compliance
```

como un solo ecosistema.

---

# 20. Pregunta para la clase

> Si un usuario tiene licencia pero trabaja con una aplicación que no cumple los requisitos del entorno, ¿la preparación está completa?

Respuesta esperada:

```text
No.
```

También debemos revisar:

```text
application state
version
deployment
configuration
```

---

# 21. Diferencia entre instalar y administrar

Explicar:

```text
Install Office
```

es una tarea.

Pero:

```text
Manage Microsoft 365 Apps
```

incluye:

```text
Deployment

Updates

Configuration

Monitoring

Health

Policy
```

---

# 22. Escenario empresarial

Contoso tiene:

```text
2,000 users

1,500 managed Windows devices

300 remote workers

200 web-only users
```

No necesariamente utilizará la misma estrategia para todos.

Podría definir:

```text
Pilot group

Production group

Web users

Managed devices
```

---

# 23. Mostrar Cloud Policy si está disponible

Si aparece:

```text
Customization
→ Policy Management
```

o una opción equivalente de Cloud Policy, mostrarla.

No crear políticas durante esta demo.

---

## Qué explicar

La administración de aplicaciones también puede incluir políticas sobre el comportamiento de Office.

---

# 24. No convertir esta demo en un laboratorio de despliegue

No necesitamos:

```text
instalar Office

desinstalar Office

cambiar update channels

crear deployment packages

modificar políticas globales
```

El objetivo es comprender la arquitectura y dónde se administra.

---

# 25. Resultado esperado

El alumno debe poder explicar:

```text
dónde revisar licencias

dónde revisar aplicaciones

qué es Microsoft 365 Apps Admin Center

qué significa Inventory

por qué importan las versiones

qué relación existe con DLP y Labels
```

---

# 26. Qué NO hacer

No:

```text
cambiar canales de actualización

desinstalar aplicaciones

modificar configuraciones globales

asignar licencias de producción

crear políticas que afecten a todos los usuarios
```

---

# 27. Plan B - Apps Admin Center no muestra datos

Esto puede ocurrir en un tenant de laboratorio.

Explicar conceptualmente:

```text
Inventory requires managed application/device data
```

Si no existen dispositivos registrados:

```text
mostrar el portal
explicar las áreas
continuar con Microsoft 365 web apps
```

No detener la clase.

---

# 28. Plan B - No hay aplicaciones desktop

Utilizar:

```text
https://www.microsoft365.com
```

Mostrar:

```text
Word
Excel
PowerPoint
Outlook
OneDrive
```

desde la web.

---

# 29. Mensaje clave

> La preparación para Microsoft 365 Copilot incluye identidad, permisos y protección de datos, pero también una estrategia consistente para las aplicaciones desde las que los usuarios trabajan con esa información.

---

# 30. Cierre de Module 04

Mostrar:

```text
Identity
   ↓
Secure Access
   ↓
Roles
   ↓
Applications
   ↓
Data
```

---

# 31. Transición

Siguiente módulo:

```text
Module 05
Microsoft Purview Data Loss Prevention
```

Ahora pasaremos de:

```text
What applications are users using?
```

a:

```text
How do we protect sensitive information
while users work with those applications?
```