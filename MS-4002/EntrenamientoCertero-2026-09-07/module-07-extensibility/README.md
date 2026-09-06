# Module 07 - Manage Microsoft 365 Copilot Extensibility

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Comprender por qué la extensibilidad de Microsoft 365 Copilot también debe formar parte de la estrategia de seguridad y gobierno de una organización.

Hasta ahora hemos preparado:

```text
Identity
+
Secure Access
+
Roles
+
Microsoft 365 Apps
+
DLP
+
Sensitivity Labels
```

Ahora agregamos:

```text
Copilot Extensibility
```

---

# 2. Punto de partida

Microsoft 365 Copilot no debe analizarse únicamente como una experiencia aislada.

Las organizaciones pueden ampliar sus experiencias mediante capacidades como:

```text
Agents
Apps
Connectors
Custom solutions
```

Esto crea nuevas posibilidades, pero también nuevas preguntas de gobierno.

---

# 3. Pregunta para iniciar

Preguntar:

> Si permitimos que cualquier usuario agregue cualquier agente o aplicación a nuestro entorno de Copilot, ¿seguimos teniendo control sobre el entorno?

La respuesta conduce al concepto:

```text
EXTENSIBILITY GOVERNANCE
```

---

# 4. Analogía

Imagina un teléfono corporativo.

El dispositivo inicialmente está administrado y protegido.

Pero después permitimos:

```text
cualquier aplicación
+
cualquier proveedor
+
cualquier permiso
```

El dispositivo sigue siendo corporativo, pero su superficie de riesgo aumentó.

Con Copilot debemos considerar algo parecido:

```text
Core environment
      |
      v
Extensions
      |
      v
Additional capabilities
      |
      v
Additional governance
```

---

# 5. ¿Qué significa extensibilidad?

Extensibilidad significa ampliar las capacidades disponibles para los usuarios.

Conceptualmente:

```text
Microsoft 365 Copilot
        |
        +---- Agents
        |
        +---- Apps
        |
        +---- Connectors
        |
        +---- Organizational data
```

Las capacidades concretas disponibles pueden variar según el tenant, licenciamiento y evolución del producto.

---

# 6. La pregunta de seguridad

Cada extensión puede llevarnos a preguntar:

```text
Who created it?

Who can use it?

What data can it access?

What actions can it perform?

What permissions does it require?

Who approved it?
```

Estas preguntas convierten la extensibilidad en un tema de gobierno.

---

# 7. Extensibilidad no elimina los controles existentes

Una extensión debe convivir con el modelo de seguridad de Microsoft 365.

Conceptualmente:

```text
User
  |
  v
Identity
  |
  v
Permissions
  |
  v
Copilot / Agent
  |
  v
Authorized resources
```

No debemos diseñar una extensión pensando que los controles de identidad y permisos dejan de ser importantes.

---

# 8. Analogía de permisos

Un empleado puede contratar a un asistente.

Pero el asistente no debería recibir automáticamente:

```text
acceso al departamento financiero
+
recursos humanos
+
contratos
+
sistemas administrativos
```

Debe recibir únicamente los accesos necesarios para su función.

El mismo principio aparece nuevamente:

```text
Least Privilege
```

---

# 9. Volvemos al Module 03

El principio de mínimo privilegio no aplica únicamente a administradores.

Es una filosofía de diseño:

```text
Need
 |
 v
Required Access
 |
 v
Nothing More
```

Cuando incorporamos extensiones debemos analizar también qué acceso necesitan.

---

# 10. Agents

Un agente puede proporcionar una experiencia especializada para un determinado escenario.

Ejemplos conceptuales:

```text
HR Agent
Support Agent
Sales Agent
Policy Agent
```

Cada agente puede tener:

```text
Purpose
+
Knowledge
+
Users
+
Permissions
+
Actions
```

---

# 11. Ejemplo real

Supongamos que creamos:

```text
HR Agent
```

Objetivo:

```text
Responder preguntas sobre
políticas de Recursos Humanos
```

Deberíamos preguntarnos:

```text
¿Qué fuentes utiliza?

¿Quién puede acceder?

¿Puede acceder a expedientes personales?

¿Solamente consulta políticas?

¿Puede ejecutar acciones?
```

---

# 12. Diferencia entre conocimiento y autorización

Que un agente conozca una fuente no significa que debamos ignorar:

```text
permissions
```

El diseño debe considerar tanto:

```text
WHAT information is connected
```

como:

```text
WHO should access it
```

---

# 13. Oversharing vuelve a aparecer

Recordar Module 01:

```text
Oversharing
```

Si una fuente tiene permisos demasiado amplios, extender experiencias sobre esa información puede hacer más evidente un problema que ya existía.

Por eso el ciclo vuelve a:

```text
Permissions
+
Governance
```

---

# 14. Aplicaciones

Las organizaciones también deben controlar las aplicaciones permitidas dentro de su ecosistema Microsoft 365.

Preguntas:

```text
Is the application approved?

Who published it?

What permissions does it request?

Who can install/use it?
```

---

# 15. Consentimiento y permisos

Una aplicación puede requerir permisos para acceder a recursos.

Conceptualmente:

```text
Application
     |
     v
Requests permission
     |
     v
Consent
     |
     v
Access
```

La organización debe gobernar este proceso.

---

# 16. Analogía

Cuando instalamos una aplicación en un teléfono y solicita:

```text
Contacts
Camera
Location
Files
Microphone
```

deberíamos preguntarnos:

```text
¿Por qué necesita estos permisos?
```

El mismo razonamiento aplica al ecosistema empresarial.

---

# 17. Admin Consent

Determinados permisos pueden requerir aprobación administrativa.

Conceptualmente:

```text
Application
     |
     v
Permission request
     |
     v
Administrator review
     |
     v
Approve / Reject
```

Esto proporciona un punto de control.

---

# 18. DEMO INSTRUCTOR - Microsoft 365 Admin Center

Mostrar las áreas disponibles relacionadas con:

```text
Apps
Settings
Integrated apps
```

según la interfaz actual del tenant.

El objetivo no es instalar una aplicación.

El objetivo es mostrar que existe administración centralizada.

---

# 19. Qué observar

Durante la demo identificar, cuando esté disponible:

```text
Application
Publisher
Users
Permissions
Status
```

Explicar:

> Una extensión no debe evaluarse únicamente por lo que hace, sino también por los permisos y datos que utiliza.

---

# 20. DEMO INSTRUCTOR - Microsoft Entra

Abrir Microsoft Entra.

Mostrar conceptualmente las áreas relacionadas con:

```text
Enterprise applications
```

y:

```text
App registrations
```

Explicar que las aplicaciones pueden formar parte del modelo de identidad y permisos del tenant.

---

# 21. Enterprise Application vs App Registration

No profundizar excesivamente.

Conceptualmente:

```text
App Registration
=
definición/identidad de una aplicación
```

mientras que:

```text
Enterprise Application
=
representación utilizada dentro del tenant
```

El objetivo del curso no es desarrollar aplicaciones, sino reconocer que también deben gobernarse.

---

# 22. Connected Data

Una extensión puede incorporar información procedente de diferentes fuentes.

Modelo conceptual:

```text
Copilot / Agent
       |
       v
Connected information
       |
       +---- Microsoft 365
       +---- Business systems
       +---- Organizational knowledge
```

Cuantas más fuentes incorporamos, mayor importancia adquieren:

```text
Permissions
Classification
Governance
```

---

# 23. Ejemplo empresarial

Contoso crea:

```text
Sales Agent
```

El agente necesita información de:

```text
Products
Customers
Contracts
Sales documentation
```

No deberíamos simplemente conectar:

```text
entire corporate repository
```

Debemos determinar qué información necesita realmente.

---

# 24. Principio

```text
More connected data
        !=
Better governance
```

Conectar más información no siempre significa crear una mejor solución.

La información debe ser:

```text
Relevant
Authorized
Governed
```

---

# 25. Extensibilidad y DLP

Las políticas de protección de información continúan formando parte del entorno.

Recordar:

```text
Module 05
DLP
```

La incorporación de nuevas experiencias no significa que debamos abandonar los controles sobre información sensible.

---

# 26. Extensibilidad y Sensitivity Labels

También continúa siendo importante:

```text
Module 06
Sensitivity Labels
```

La organización debe mantener una estrategia coherente de clasificación y protección de información.

---

# 27. Modelo completo de gobierno

```text
                COPILOT
                   |
        +----------+----------+
        |                     |
      Users               Extensions
        |                     |
     Identity               Agents
        |                     |
     Access                  Apps
        |                     |
 Permissions              Connectors
        |                     |
        +----------+----------+
                   |
                   v
                  DATA
                   |
        +----------+----------+
        |                     |
       DLP              Sensitivity
                             Labels
                   |
                   v
               GOVERNANCE
```

---

# 28. Ciclo de aprobación

Una organización puede establecer conceptualmente:

```text
Request
   |
   v
Security Review
   |
   v
Permission Review
   |
   v
Data Review
   |
   v
Approval
   |
   v
Pilot
   |
   v
Production
```

---

# 29. Analogía

Es el mismo patrón utilizado para introducir cualquier sistema empresarial.

No hacemos:

```text
Someone found an app
        |
        v
Deploy to everyone
```

Preferimos:

```text
Evaluate
   |
   v
Approve
   |
   v
Pilot
   |
   v
Monitor
   |
   v
Expand
```

---

# 30. DEMO INSTRUCTOR - Escenario de agente

No es necesario construir un agente completo.

Plantear:

```text
HR Agent
```

y preguntar a los alumnos:

```text
1. ¿Quién puede usarlo?
2. ¿Qué información necesita?
3. ¿Qué información NO necesita?
4. ¿Qué permisos necesita?
5. ¿Quién debería aprobarlo?
6. ¿Cómo lo probaríamos?
```

---

# 31. Ejercicio rápido

Escenario:

```text
Finance Agent
```

Objetivo:

```text
Ayudar a analizar políticas
y procedimientos financieros.
```

La organización dispone de:

```text
Finance Policies
Employee Salaries
Customer Contracts
Bank Information
Public Reports
```

Preguntar:

> ¿Conectaríamos todas estas fuentes automáticamente?

Respuesta esperada:

```text
No
```

Primero debemos definir:

```text
Purpose
+
Required Data
+
Permissions
+
Security
+
Governance
```

---

# 32. Shadow AI

Introducir conceptualmente el riesgo de que usuarios adopten herramientas o soluciones de IA fuera del gobierno definido por la organización.

El mensaje principal:

```text
AI adoption
without governance
=
organizational risk
```

La solución no es solamente bloquear.

También debemos ofrecer:

```text
Approved tools
+
Policies
+
Education
+
Governance
```

---

# 33. El patrón vuelve a repetirse

Desde Module 01 hemos utilizado:

```text
Pilot
   |
   v
Validate
   |
   v
Govern
   |
   v
Expand
```

Este mismo patrón debe utilizarse para extensibilidad.

---

# 34. Qué NO vamos a hacer

Este módulo no busca enseñar:

```text
cómo desarrollar un agente completo
```

ni:

```text
cómo programar una aplicación
```

ni:

```text
cómo desarrollar un connector
```

El objetivo de MS-4002 es comprender:

```text
Security
+
Compliance
+
Governance
```

alrededor de estas capacidades.

---

# 35. Pregunta de comprobación

Preguntar:

> Si una aplicación funciona técnicamente, ¿significa que automáticamente debería aprobarse para toda la organización?

Respuesta:

```text
No
```

Debemos revisar:

```text
Permissions
Data
Security
Publisher
Users
Governance
```

---

# 36. Segunda comprobación

Preguntar:

> ¿Qué principio visto anteriormente vuelve a ser fundamental cuando hablamos de extensibilidad?

Respuesta:

```text
Least Privilege
```

---

# 37. Tercera comprobación

Preguntar:

> ¿Por qué Oversharing también importa para agentes y experiencias de Copilot?

Respuesta conceptual:

```text
Porque una experiencia puede utilizar
información que ya está disponible
para el usuario según los permisos existentes.
```

Por eso debemos corregir los permisos y el gobierno de la información.

---

# 38. Mensaje clave

El alumno debe recordar:

> Extender Copilot también significa extender nuestra superficie de gobierno.

Modelo:

```text
EXTEND
   |
   v
REVIEW ACCESS
   |
   v
REVIEW DATA
   |
   v
REVIEW PERMISSIONS
   |
   v
GOVERN
```

---

# 39. Transición

Ya hemos recorrido:

```text
Identity
Access
Roles
Apps
DLP
Sensitivity Labels
Extensibility
```

Ahora debemos conectar todas las piezas.

Siguiente:

```text
Module 08
Review
```