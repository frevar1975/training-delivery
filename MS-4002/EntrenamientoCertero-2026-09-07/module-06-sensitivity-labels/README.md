# Module 06 - Sensitivity Labels

## MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

---

# 1. Objetivo del módulo

Comprender cómo Microsoft Purview Information Protection permite clasificar y proteger información mediante Sensitivity Labels.

En el módulo anterior respondimos:

```text
¿Qué ocurre cuando información sensible
es utilizada o compartida?
```

Ahora responderemos:

```text
¿Qué ES esta información
y cómo debería protegerse?
```

---

# 2. Punto de partida

Una organización puede tener diferentes niveles de información:

```text
Public
Internal
Confidential
Highly Confidential
```

No toda la información requiere el mismo nivel de protección.

Necesitamos una forma consistente de:

```text
Classify
   |
   v
Label
   |
   v
Protect
```

---

# 3. ¿Qué es una Sensitivity Label?

Una Sensitivity Label permite asociar una clasificación a información y aplicar determinados controles.

Modelo:

```text
Document
    |
    v
Sensitivity Label
    |
    +---- Classification
    +---- Content Marking
    +---- Protection
    +---- Encryption
```

---

# 4. Analogía

Imagina documentos físicos.

Algunos pueden llevar un sello:

```text
PUBLIC
```

otros:

```text
INTERNAL
```

y otros:

```text
CONFIDENTIAL
```

El sello comunica cómo debe tratarse el documento.

Una Sensitivity Label lleva este concepto al entorno digital y puede agregar controles adicionales.

---

# 5. Una etiqueta no es solamente un nombre

Una etiqueta:

```text
CONFIDENTIAL
```

puede representar mucho más que texto.

Puede asociar:

```text
Classification
+
Visual marking
+
Protection
+
Access controls
```

dependiendo de su configuración.

---

# 6. Ejemplo del curso

En el laboratorio crearemos:

```text
PII
```

PII representa:

```text
Personally Identifiable Information
```

La etiqueta permitirá demostrar clasificación y protección sobre documentos de laboratorio.

---

# 7. Importante para la clase

No utilizar:

```text
información personal real
```

para demostrar PII.

Utilizaremos únicamente:

```text
sample data
```

creada específicamente para el laboratorio.

---

# 8. Microsoft Purview Information Protection

Las Sensitivity Labels se administran dentro de las capacidades de Information Protection de Microsoft Purview.

Modelo:

```text
Microsoft Purview
       |
       v
Information Protection
       |
       v
Sensitivity Labels
```

---

# 9. DEMO INSTRUCTOR - Information Protection

Abrir Microsoft Purview.

Mostrar:

```text
Solutions
>
Information Protection
>
Sensitivity labels
```

Revisar las etiquetas existentes.

No modificar etiquetas productivas.

---

# 10. Label vs Label Policy

Esta diferencia es fundamental.

## Label

Define:

```text
WHAT
```

Ejemplo:

```text
PII
```

y qué protección puede aplicar.

## Label Policy

Define principalmente:

```text
WHO
```

recibe/publica la etiqueta y determinados comportamientos asociados.

---

# 11. Modelo

```text
PII
 |
 v
Sensitivity Label
 |
 v
Defines classification/protection
```

Después:

```text
PII Policy
 |
 v
Publishes PII
 |
 v
Selected users
```

---

# 12. Analogía

Imagina que Recursos Humanos crea una clasificación:

```text
CONFIDENTIAL
```

Eso equivale a crear:

```text
LABEL
```

Pero todavía debemos decidir:

```text
¿Quién puede utilizarla?
```

Eso se relaciona con:

```text
LABEL POLICY
```

---

# 13. Crear no significa publicar

Punto importante:

```text
Create Label
      !=
Publish Label
```

Una etiqueta puede existir administrativamente sin estar todavía disponible para los usuarios.

---

# 14. Scope

Al crear una etiqueta debemos determinar dónde puede utilizarse.

Conceptualmente:

```text
Sensitivity Label
       |
       +---- Files
       +---- Emails
       +---- Meetings
       +---- Groups / Sites
       +---- Other supported assets
```

Las opciones exactas dependen de las capacidades disponibles en el tenant.

---

# 15. Analogía de Scope

Una etiqueta puede diseñarse para:

```text
documentos
```

pero no necesariamente para:

```text
sitios
```

o viceversa.

El Scope determina el tipo de recurso al que está orientada.

---

# 16. Protection Settings

Una etiqueta puede incorporar diferentes acciones.

En nuestro laboratorio nos concentraremos principalmente en:

```text
Control access
```

y:

```text
Content marking
```

---

# 17. Content Marking

Content Marking permite agregar indicadores visuales.

Ejemplos:

```text
Header
Footer
Watermark
```

---

# 18. Ejemplo

Etiqueta:

```text
PII
```

Puede producir:

```text
Header:
PII - CONFIDENTIAL

Footer:
Contains Personally Identifiable Information

Watermark:
CONFIDENTIAL - PII
```

---

# 19. Analogía

Es similar a imprimir sobre cada página:

```text
CONFIDENTIAL
```

para que cualquier persona que vea el documento pueda reconocer su clasificación.

---

# 20. Importante

El watermark no es la etiqueta.

Es solamente:

```text
una acción de Content Marking
```

producida por la configuración de la etiqueta.

Modelo:

```text
Sensitivity Label
       |
       +---- Header
       +---- Footer
       +---- Watermark
       +---- Other protection
```

---

# 21. Control Access

Una etiqueta también puede controlar el acceso al contenido mediante las opciones de protección disponibles.

Conceptualmente:

```text
Document
   |
   v
PII
   |
   v
Control Access
   |
   v
Authorized identities
```

---

# 22. Encryption

Cuando corresponde, una etiqueta puede aplicar cifrado.

Modelo:

```text
Document
   |
   v
Sensitivity Label
   |
   v
Encryption
   |
   v
Authorized users
```

---

# 23. Analogía

Un documento físico puede tener:

```text
CONFIDENTIAL
```

escrito encima.

Eso es parecido a:

```text
Content Marking
```

Pero también puede guardarse dentro de:

```text
una caja cerrada
```

Eso se aproxima conceptualmente a:

```text
Encryption / Access Control
```

---

# 24. Clasificación vs protección

No confundir:

```text
Classification
```

con:

```text
Protection
```

Una etiqueta puede comunicar:

```text
qué tipo de información es
```

y además aplicar:

```text
cómo debe protegerse
```

---

# 25. Sensitive Information Types

Microsoft Purview también puede reconocer determinados tipos de información sensible.

Ejemplos conceptuales:

```text
Personal identifiers
Financial information
Government identifiers
Health information
```

---

# 26. Auto-labeling

En escenarios compatibles podemos relacionar detección de contenido con clasificación.

Modelo:

```text
Document
   |
   v
Sensitive Information Type
   |
   v
Detection
   |
   v
Sensitivity Label
```

---

# 27. Manual vs automático

Manual:

```text
User
 |
 v
Select PII
```

Automático:

```text
Content detected
      |
      v
Classification logic
      |
      v
PII
```

Las capacidades exactas dependen de configuración y licenciamiento.

---

# 28. DEMO INSTRUCTOR - Create a Label

Iniciar:

```text
Create a label
```

Mostrar las etapas del asistente:

```text
Basic details
    |
    v
Scope
    |
    v
Protection
    |
    v
Content marking
    |
    v
Review
```

No es necesario terminarla durante esta explicación.

La creación completa corresponde al:

```text
Lab 04
```

---

# 29. Etiqueta del laboratorio

Durante el Lab 04 utilizaremos:

```text
Name:
PII

Display name:
PII
```

Descripción:

```text
Documents, files, and emails with PII
```

---

# 30. Label Policy

Después de crear PII debemos publicarla.

Utilizaremos:

```text
PII Policy
```

Modelo:

```text
PII
 |
 v
PII Policy
 |
 v
LAB users
 |
 v
Microsoft 365 Apps
```

---

# 31. Alcance controlado

En un entorno de práctica preferimos:

```text
LAB-User1
LAB-User2
```

en lugar de publicar inmediatamente a:

```text
Entire organization
```

especialmente si el tenant es compartido.

---

# 32. Justification

Una Label Policy puede requerir que el usuario proporcione una justificación cuando intenta:

```text
Remove label
```

o:

```text
Lower classification
```

---

# 33. Ejemplo

Documento:

```text
PII
```

Usuario intenta:

```text
Remove PII
```

Resultado:

```text
Justification required
```

Ejemplo de laboratorio:

```text
Authorized MS-4002 lab test.
```

---

# 34. Analogía

Un documento está marcado:

```text
CONFIDENTIAL
```

El usuario quiere convertirlo en:

```text
PUBLIC
```

La organización responde:

```text
Puedes hacerlo,
pero debes explicar por qué.
```

---

# 35. Trazabilidad

La justificación agrega un elemento de:

```text
Accountability
```

El objetivo no es únicamente:

```text
BLOCK
```

sino también comprender las decisiones del usuario.

---

# 36. SharePoint y OneDrive

Las etiquetas pueden interactuar con archivos almacenados en servicios Microsoft 365 compatibles.

Conceptualmente:

```text
Word
 |
 v
PII
 |
 v
OneDrive / SharePoint
 |
 +---- Collaboration
 +---- Protection
 +---- Compliance
```

---

# 37. Office for the Web

En nuestros laboratorios Standalone utilizaremos principalmente:

```text
Word for the Web
```

Esto evita depender de una instalación específica de Office Desktop en cada PC.

---

# 38. Prueba

Documento de laboratorio:

```text
MS-4002 Sensitivity Label Test

This document contains sample personally
identifiable information for a training exercise.
```

Después:

```text
Sensitivity
    |
    v
PII
```

---

# 39. Resultado esperado

Dependiendo de la configuración:

```text
PII
 |
 +---- Sensitivity indicator
 +---- Header
 +---- Footer
 +---- Watermark
 +---- Protection
```

---

# 40. Propagación

Este punto es crítico para la clase.

Después de:

```text
Create label
```

y:

```text
Publish label
```

puede existir un tiempo de propagación antes de que la etiqueta aparezca en las aplicaciones.

---

# 41. Modelo

```text
Create PII
    |
    v
Publish PII
    |
    v
PII Policy
    |
    v
Propagation
    |
    v
Word / Outlook / Microsoft 365
```

No todos los pasos son instantáneos.

---

# 42. Regla para el laboratorio

Si PII no aparece inmediatamente:

```text
DO NOT recreate PII
```

y:

```text
DO NOT recreate PII Policy
```

Primero revisar:

```text
Label exists?
Policy exists?
User included?
Correct account?
Propagation completed?
```

---

# 43. Estrategia del instructor

Antes de la clase puede prepararse una etiqueta sencilla.

Ejemplo:

```text
LAB - Confidential
```

y publicarla con anticipación.

Así podemos trabajar:

```text
Students
   |
   v
Create PII

Instructor
   |
   v
Explains propagation

Testing
   |
   +---- PII if available
   |
   +---- LAB - Confidential if needed
```

---

# 44. Por qué hacemos esto

El objetivo de la clase es enseñar:

```text
cómo funciona
```

no esperar durante la sesión a que:

```text
la propagación termine
```

---

# 45. DEMO INSTRUCTOR - Word

Si existe una etiqueta previamente publicada:

abrir:

```text
Word for the Web
```

Crear un documento.

Mostrar:

```text
Sensitivity
```

Aplicar:

```text
LAB - Confidential
```

o:

```text
PII
```

si ya está disponible.

---

# 46. Mostrar Content Marking

Revisar:

```text
Header
Footer
Watermark
```

según la configuración de la etiqueta utilizada.

---

# 47. Mostrar Justification

Si la política está disponible:

intentar:

```text
Remove label
```

o:

```text
Lower classification
```

Mostrar la solicitud de:

```text
Justification
```

---

# 48. DLP vs Sensitivity Labels

Esta comparación es fundamental.

## Sensitivity Labels

Responden principalmente:

```text
¿Qué ES esta información?
```

y:

```text
¿Cómo debe clasificarse/protegerse?
```

## DLP

Responde principalmente:

```text
¿Qué está ocurriendo con
información sensible?
```

---

# 49. Comparación

| Sensitivity Labels | DLP |
|---|---|
| Clasificación | Actividad |
| Marcado | Policy Tips |
| Protección | Restricción |
| Encryption | Block |
| Control de acceso según configuración | Override según política |

---

# 50. Cómo trabajan juntas

Ejemplo:

```text
Document
   |
   v
PII Label
   |
   v
User shares information
   |
   v
DLP evaluates activity
   |
   +---- Allow
   +---- Notify
   +---- Block
```

No son tecnologías competidoras.

Son capas complementarias.

---

# 51. Analogía conjunta

Sensitivity Label:

```text
Etiqueta pegada en la caja:
CONFIDENTIAL
```

DLP:

```text
Guardia que controla
qué ocurre cuando alguien
intenta sacar la caja.
```

---

# 52. Relación con Copilot

Microsoft 365 Copilot opera dentro del contexto de Microsoft 365 y sus controles.

Una estrategia de preparación debe considerar:

```text
Permissions
+
Classification
+
Information Protection
+
DLP
+
Governance
```

---

# 53. Ejemplo empresarial

Una empresa tiene:

```text
HR documents
Financial documents
Customer information
Public marketing material
```

No deberíamos tratarlos todos como:

```text
same sensitivity
```

Podemos definir una taxonomía:

```text
Public
Internal
Confidential
Highly Confidential
```

y asociar controles adecuados.

---

# 54. Error frecuente

Crear demasiadas etiquetas puede hacer que el sistema resulte difícil de entender para los usuarios.

Ejemplo problemático:

```text
Confidential A
Confidential B
Confidential Internal
Confidential External
Confidential Restricted
Confidential Special
...
```

La clasificación debe ser comprensible y gobernable.

---

# 55. La tecnología no sustituye el diseño de clasificación

Antes de crear etiquetas debemos responder:

```text
¿Qué niveles de información necesita
realmente nuestra organización?
```

Después:

```text
¿Cómo los implementamos técnicamente?
```

---

# 56. Relación con Lab 04

Este módulo prepara directamente:

```text
Standalone Lab 04
Sensitivity Labels
```

El alumno realizará:

```text
Purview
   |
   v
Create PII
   |
   v
Configure Scope
   |
   v
Content Marking
   |
   v
Protection
   |
   v
Publish
   |
   v
PII Policy
   |
   v
Test
```

---

# 57. Qué ejecutará el alumno

Según las capacidades del tenant:

```text
Create label
Configure content marking
Review access control
Publish label
Configure justification
Open Word
Apply sensitivity label
Test downgrade/removal
```

---

# 58. Qué puede quedar como demo

Dependiendo de:

```text
Licensing
Tenant
Time
Propagation
```

pueden quedar como demo:

```text
Advanced encryption
Auto-labeling
PDF scenarios
External sharing
Advanced SharePoint scenarios
```

---

# 59. Pregunta de comprobación

Preguntar:

> ¿Crear PII significa que inmediatamente aparecerá en Word para todos los usuarios?

Respuesta:

```text
No
```

Debemos:

```text
Create
   |
   v
Publish
   |
   v
Propagate
```

---

# 60. Segunda comprobación

Preguntar:

> ¿Cuál es la diferencia entre un Watermark y una Sensitivity Label?

Respuesta:

```text
Watermark
=
una posible acción de marcado visual

Sensitivity Label
=
clasificación que puede incluir
marcado y otros controles
```

---

# 61. Tercera comprobación

Preguntar:

> ¿DLP y Sensitivity Labels hacen exactamente lo mismo?

Respuesta:

```text
No
```

Son controles complementarios.

---

# 62. Mensaje clave

El alumno debe recordar:

> DLP controla actividades relacionadas con información sensible; Sensitivity Labels ayudan a clasificar y proteger la propia información.

Modelo:

```text
INFORMATION
     |
     v
CLASSIFY
     |
     v
PROTECT
     |
     v
CONTROL USE
```

---

# 63. Transición

Hasta ahora hemos preparado:

```text
Identity
+
Secure Access
+
Roles
+
Apps
+
DLP
+
Sensitivity Labels
```

Ahora debemos considerar:

```text
¿Qué ocurre cuando extendemos
Microsoft 365 Copilot con
agentes y aplicaciones?
```

Siguiente:

```text
Module 07
Copilot Extensibility
```