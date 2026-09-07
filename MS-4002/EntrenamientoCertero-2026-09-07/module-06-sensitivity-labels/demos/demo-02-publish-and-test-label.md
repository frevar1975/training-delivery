
# DEMO 02 - Publicar y probar una Sensitivity Label

## MS-4002 - Module 06: Sensitivity Labels

---

## Duración

20 a 25 minutos

## Tipo

DEMO INSTRUCTOR - CONFIGURACIÓN Y PRUEBA

## Portales

```text
Microsoft Purview
https://purview.microsoft.com

Microsoft 365
https://www.microsoft365.com
```

---

# Objetivo

Publicar la etiqueta creada anteriormente:

```text
PII
```

para usuarios controlados del laboratorio y comprobar su funcionamiento desde una aplicación de Microsoft 365.

Flujo:

```text
PII Label
   ↓
Label Policy
   ↓
Users
   ↓
Microsoft 365 Apps
   ↓
Apply Label
   ↓
Classification / Protection
```

---

# Escenario

Ya tenemos creada:

```text
PII
```

Pero crear una etiqueta no significa que los usuarios puedan utilizarla.

Ahora debemos publicar la etiqueta.

Utilizaremos:

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>

Laura Rojas - Test User 2
lab-user2@<TU-DOMINIO>
```

---

# 1. Recordar Create vs Publish

Antes de entrar al portal mostrar:

```text
CREATE LABEL
      ↓
Define classification

PUBLISH LABEL
      ↓
Make it available to users
```

Pregunta:

> Ya creamos PII. ¿Carlos puede verla automáticamente?

Respuesta:

```text
No necesariamente.
```

---

# 2. Abrir Microsoft Purview

Abrir:

```text
https://purview.microsoft.com
```

Ir a:

```text
Solutions
→ Information Protection
```

Localizar:

```text
Sensitivity labels
```

---

# 3. Verificar PII

Confirmar que existe:

```text
PII
```

No crear otra etiqueta si ya existe.

---

# 4. Ir a publicación de etiquetas

Localizar la experiencia correspondiente a:

```text
Publish labels
```

o:

```text
Label policies
```

La ubicación y denominación pueden variar según la experiencia actual del portal.

---

# 5. Crear una Label Policy

Seleccionar la opción equivalente a:

```text
Publish labels
```

o:

```text
Create policy
```

---

# 6. Seleccionar la etiqueta

Seleccionar:

```text
PII
```

---

## Qué explicar

Una política de publicación responde:

```text
WHAT LABEL?
   ↓
PII

WHO?
   ↓
Selected users

HOW?
   ↓
Label policy settings
```

---

# 7. Definir usuarios

Para el laboratorio preferimos un alcance pequeño.

Seleccionar:

```text
Carlos Mendoza - Test User 1

Laura Rojas - Test User 2
```

o las identidades equivalentes del tenant.

---

## Importante

Evitar:

```text
All users
```

en un tenant compartido salvo que sea un entorno dedicado exclusivamente al laboratorio.

---

# 8. Explicar el alcance

Mostrar:

```text
PII
 |
 v
PII Policy
 |
 +--> Carlos
 |
 +--> Laura
```

Otros usuarios:

```text
no necesariamente reciben la etiqueta
```

---

# 9. Configuración de la política

Revisar las opciones disponibles.

Dependiendo del tenant pueden existir configuraciones relacionadas con:

```text
Default label

Mandatory labeling

Justification for removing a label

Justification for lowering classification
```

---

# 10. Mandatory Labeling

Explicar conceptualmente:

```text
Mandatory labeling
```

puede obligar a que determinados elementos tengan una etiqueta.

Para este laboratorio no necesitamos imponerlo globalmente.

---

# 11. Default Label

Explicar:

```text
Default Label
```

puede aplicar automáticamente una clasificación inicial.

No establecer:

```text
PII
```

como etiqueta predeterminada global del tenant.

---

# 12. Justification

Si está disponible, habilitar la solicitud de justificación cuando un usuario:

```text
removes a label
```

o:

```text
lowers classification
```

---

## Ejemplo de justificación

Durante el laboratorio:

```text
Authorized MS-4002 lab test.
```

---

# 13. Nombre de la política

Utilizar:

```text
PII Policy
```

Descripción sugerida:

```text
MS-4002 lab policy for publishing the PII sensitivity label.
```

---

# 14. Revisar antes de crear

Confirmar:

```text
Label:
PII

Policy:
PII Policy

Users:
Carlos
Laura
```

---

# 15. Crear la política

Seleccionar:

```text
Create policy
```

o la opción equivalente.

---

# 16. Resultado esperado

Debe aparecer:

```text
PII Policy
```

entre las políticas de publicación.

---

# 17. Propagación

Detenerse aquí para explicar:

```text
Published
≠
Immediately visible
```

La política puede necesitar tiempo para estar disponible en las aplicaciones.

---

# 18. Estrategia para una clase de 2 horas

No podemos dedicar la sesión a esperar propagación.

Utilizaremos:

```text
PLAN A
PII appears
→ use PII

PLAN B
PII does not appear
→ use pre-published LAB - Confidential
```

---

# 19. Preparar navegador de Carlos

Abrir:

```text
Edge
→ New InPrivate window
```

Iniciar sesión como:

```text
Carlos Mendoza - Test User 1
lab-user1@<TU-DOMINIO>
```

---

# 20. Abrir Microsoft 365

Entrar a:

```text
https://www.microsoft365.com
```

Abrir:

```text
Word
```

Preferimos Word for the web para evitar depender de una instalación local específica.

---

# 21. Crear documento

Crear un documento en blanco.

Nombre sugerido:

```text
MS4002-PII-Test.docx
```

---

# 22. Agregar contenido ficticio

Escribir:

```text
MS-4002 authorized training document.

Employee:
John Doe

Test identifier:
111-11-1111

This information is fictitious and used only for training.
```

---

## Importante

No utilizar:

```text
PII real

datos de clientes

datos de empleados

documentos reales
```

---

# 23. Localizar Sensitivity

En Word buscar:

```text
Sensitivity
```

La ubicación puede variar según la experiencia de Microsoft 365.

---

# 24. Revisar etiquetas disponibles

Abrir:

```text
Sensitivity
```

Buscar:

```text
PII
```

---

# 25. PLAN A - PII aparece

Seleccionar:

```text
PII
```

---

# 26. Observar resultado

Según la configuración realizada, buscar:

```text
PII - CONFIDENTIAL
```

en el encabezado.

También:

```text
Contains Personally Identifiable Information
```

en el pie.

Y, cuando corresponda:

```text
CONFIDENTIAL - PII
```

como marca de agua.

---

# 27. Explicar persistencia

La clasificación está asociada al documento.

Conceptualmente:

```text
Document
   +
PII Label
```

No es simplemente texto escrito manualmente en el archivo.

---

# 28. Mostrar información de la etiqueta

Si Word permite consultar detalles, mostrar:

```text
Sensitivity
→ PII
```

Explicar qué significa la clasificación.

---

# 29. Probar cambio o eliminación

Solo si es seguro en el tenant:

Intentar cambiar o quitar:

```text
PII
```

---

# 30. Justificación

Si configuramos justificación, el sistema puede solicitar una razón.

Utilizar:

```text
Authorized MS-4002 lab test.
```

---

# 31. Explicar el evento

Mostrar:

```text
User
   ↓
Changes classification
   ↓
Justification required
   ↓
Governance
```

---

# 32. PLAN B - PII no aparece

No crear otra etiqueta.

No modificar inmediatamente la política.

Explicar:

```text
This is expected in environments
where policy propagation is still occurring.
```

---

# 33. Utilizar etiqueta preparada

Buscar:

```text
LAB - Confidential
```

si fue publicada previamente por el instructor.

Aplicarla al documento.

---

# 34. Qué demostrar con Plan B

Aunque no sea PII, podemos demostrar:

```text
Sensitivity menu

Apply label

Visual classification

Change label

Remove / downgrade behavior
```

El concepto pedagógico se mantiene.

---

# 35. Segundo usuario

Abrir otro perfil o ventana InPrivate.

Iniciar sesión como:

```text
Laura Rojas - Test User 2
lab-user2@<TU-DOMINIO>
```

---

# 36. Verificar disponibilidad

Abrir Word for the web y revisar:

```text
Sensitivity
```

Confirmar si Laura también recibió la etiqueta publicada.

---

# 37. Qué explicar

La política controla:

```text
who receives the label
```

No basta con que la etiqueta exista en Purview.

---

# 38. Relación con permisos

Recordar:

```text
Sensitivity Label
≠
SharePoint Permission
```

Una etiqueta puede proteger un documento.

Pero los permisos de SharePoint/OneDrive siguen siendo otra capa.

---

# 39. Ejemplo

```text
Carlos creates document
        ↓
Applies PII
        ↓
Saves in OneDrive
        ↓
Shares with Laura
```

En ese escenario intervienen:

```text
Identity

Sharing permissions

Sensitivity Label

Encryption

DLP
```

---

# 40. Relación con DLP

Comparar el laboratorio anterior:

```text
DLP

Detect:
192.168.0.1

Action:
Warn / Restrict
```

con:

```text
Sensitivity Label

Classify:
PII

Action:
Mark / Protect
```

---

# 41. DLP + Labels

Mostrar:

```text
Sensitive content
      |
      +------ DLP ------> Control activity
      |
      +------ Label ----> Classify / Protect
```

---

# 42. Relación con Copilot

Mostrar:

```text
User
  ↓
Identity
  ↓
Permissions
  ↓
Microsoft 365 content
  ↓
Sensitivity / DLP
  ↓
Copilot experience
```

---

# 43. Qué debe entender el alumno

La preparación de Copilot no consiste en:

```text
"activar Copilot"
```

primero debemos tener control sobre:

```text
Identity

Access

Permissions

Applications

Data

Classification

Protection
```

---

# 44. Si no aparece Sensitivity en Word

Revisar:

```text
User license

Published label policy

Included users

Application

Propagation
```

---

# 45. Si Carlos ve la etiqueta y Laura no

Revisar:

```text
PII Policy
→ Users / Groups
```

Confirmar que Laura está incluida.

También considerar propagación.

---

# 46. Si las marcas visuales no aparecen

Revisar la configuración de:

```text
PII
→ Content marking
```

No asumir inmediatamente que la publicación falló.

---

# 47. Si el documento queda restringido

No realizar cambios improvisados.

Revisar:

```text
PII
→ Encryption / Control access
```

y confirmar qué usuarios fueron autorizados.

---

# 48. No utilizar cuentas personales

Para la prueba utilizar:

```text
LAB-User1
LAB-User2
```

No necesitamos compartir documentos con cuentas personales externas.

---

# 49. Cleanup

Si el tenant es reutilizable para futuras clases, podemos conservar:

```text
PII

PII Policy
```

como material de laboratorio.

Si se trata de un tenant compartido que debe quedar limpio, documentar primero los objetos antes de eliminarlos.

---

# 50. Resultado esperado

Al finalizar:

```text
PII
   ↓
PII Policy
   ↓
Carlos + Laura
   ↓
Word
   ↓
Sensitivity
   ↓
PII
   ↓
Classification / Protection
```

---

# 51. Relación con Lab 04 Standalone

El laboratorio completo está en:

```text
labs
└── standalone
    └── lab-04-sensitivity-labels
        ├── student-guide.md
        └── instructor-guide.md
```

El demo sirve para:

```text
Instructor shows
```

El laboratorio sirve para:

```text
Student executes
```

---

# 52. Mensaje clave

> Crear una etiqueta define la clasificación. Publicarla determina quién puede utilizarla. Aplicarla convierte esa clasificación en parte del ciclo de vida del contenido.

---

# 53. Cierre de Module 06

Ya recorrimos:

```text
Create Label
    ↓
Configure Protection
    ↓
Publish Label
    ↓
Assign Users
    ↓
Apply in Microsoft 365
    ↓
Observe Classification
```

---

# 54. Transición

Siguiente módulo:

```text
Module 07
Microsoft 365 Copilot Extensibility
```

Pasamos de:

```text
How do we protect information?
```

a:

```text
What happens when we extend Copilot
with agents, apps and organizational data?
```
