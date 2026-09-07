
# DEMO 01 - Crear una Sensitivity Label en Microsoft Purview

## MS-4002 - Module 06: Sensitivity Labels

---

## Duración

20 a 25 minutos

## Tipo

DEMO INSTRUCTOR - CONFIGURACIÓN GUIADA

## Portal

```text
Microsoft Purview
https://purview.microsoft.com
```

---

# Objetivo

Crear una etiqueta de confidencialidad para demostrar cómo Microsoft Purview permite clasificar y proteger información de Microsoft 365.

Crearemos:

```text
PII
```

La etiqueta tendrá:

```text
Classification
Content marking
Protection
```

y posteriormente será publicada en el Demo 02.

---

# Escenario

Contoso maneja documentos que pueden contener información personal.

La organización necesita que ciertos archivos sean identificados claramente como sensibles.

Nuestro objetivo será crear:

```text
PII
```

para clasificar documentos que contengan Personally Identifiable Information.

---

# 1. Introducir el concepto

Explicar:

Una Sensitivity Label permite aplicar una clasificación a contenido.

Ejemplos empresariales:

```text
Public

Internal

Confidential

Highly Confidential
```

Para el laboratorio utilizaremos:

```text
PII
```

---

# 2. Modelo mental

Mostrar:

```text
Document
   ↓
Sensitivity Label
   ↓
Classification
   ↓
Protection
```

Una etiqueta puede incluir:

```text
Visual marking

Encryption

Access restrictions

Auto-labeling

Content classification
```

dependiendo de la configuración y capacidades del tenant.

---

# 3. Diferenciar Label y Label Policy

Antes de entrar al portal explicar:

```text
CREATE LABEL
≠
PUBLISH LABEL
```

Primero:

```text
Create Label
```

Después:

```text
Publish Label
```

---

## Analogía

Crear una etiqueta es como fabricar un sello:

```text
CONFIDENTIAL
```

Publicarla es decidir:

```text
quién puede usar ese sello
```

---

# 4. Abrir Microsoft Purview

Abrir:

```text
https://purview.microsoft.com
```

Iniciar sesión con la cuenta administrativa del tenant de práctica.

---

# 5. Localizar Information Protection

Buscar:

```text
Solutions
```

y localizar:

```text
Information Protection
```

Después buscar:

```text
Sensitivity labels
```

La ubicación exacta del menú puede variar según la experiencia actual del portal.

Si es necesario utilizar la búsqueda:

```text
Sensitivity labels
```

---

# 6. Mostrar etiquetas existentes

Antes de crear una etiqueta mostrar la lista actual.

No modificar etiquetas existentes.

---

## Qué explicar

Una organización puede tener una jerarquía como:

```text
Public

Internal

Confidential

Highly Confidential
```

Nuestro laboratorio creará una etiqueta separada:

```text
PII
```

---

# 7. Crear nueva etiqueta

Seleccionar la opción equivalente a:

```text
Create a label
```

---

# 8. Información básica

Configurar:

```text
Name:
PII
```

Display name:

```text
PII
```

Description for users:

```text
Documents, files, and emails with PII
```

Description for admins:

```text
MS-4002 lab sensitivity label for Personally Identifiable Information.
```

---

# 9. Explicar nombre vs descripción

El nombre identifica la etiqueta.

La descripción ayuda al usuario a entender:

```text
cuándo debe utilizarla
```

---

# 10. Definir Scope

Cuando el asistente solicite el alcance, priorizar:

```text
Items
```

para trabajar con contenido como:

```text
Files

Emails
```

---

## Qué explicar

El alcance indica:

```text
sobre qué tipo de objetos
puede aplicarse la etiqueta
```

No todas las etiquetas tienen que aplicarse a todos los tipos de contenido.

---

# 11. Elegir elementos de protección

Si el asistente presenta opciones de configuración, seleccionar capacidades relacionadas con:

```text
Control access

Apply content marking
```

según la experiencia disponible.

---

# 12. Content Marking

Entrar a la configuración de:

```text
Content marking
```

---

## Objetivo

Aplicar marcas visuales al documento.

Usaremos:

```text
Header

Footer

Watermark
```

---

# 13. Configurar Header

Activar:

```text
Header
```

Texto:

```text
PII - CONFIDENTIAL
```

---

## Qué explicar

El encabezado permite identificar visualmente el documento.

---

# 14. Configurar Footer

Activar:

```text
Footer
```

Texto:

```text
Contains Personally Identifiable Information
```

---

# 15. Configurar Watermark

Activar:

```text
Watermark
```

Texto:

```text
CONFIDENTIAL - PII
```

---

# 16. Mostrar el resultado conceptual

```text
---------------------------------
PII - CONFIDENTIAL

Documento...

Documento...

CONFIDENTIAL - PII

Contains Personally Identifiable Information
---------------------------------
```

---

# 17. Qué explicar

Estas marcas ayudan a que el usuario vea claramente:

```text
este contenido está clasificado
```

Pero la marca visual por sí sola no representa toda la protección.

---

# 18. Control Access

Entrar a:

```text
Control access
```

si está disponible dentro del asistente.

---

# 19. Explicar Encryption

Una Sensitivity Label puede aplicar protección criptográfica.

Conceptualmente:

```text
Label
   ↓
Encryption
   ↓
Access Control
```

---

# 20. No crear restricciones agresivas

Para este laboratorio evitar configuraciones que puedan impedir al instructor o alumnos recuperar acceso al documento.

Si el tenant permite configurar permisos de forma segura, mantener un alcance controlado.

---

# 21. Escenario conceptual de protección

Explicar:

```text
PII document
   ↓
Only authorized users
   ↓
Can open / edit
```

---

# 22. Diferenciar Content Marking de Encryption

Mostrar:

```text
CONTENT MARKING
→ visible to the user
```

frente a:

```text
ENCRYPTION
→ technical access protection
```

---

# 23. Sensitive Information Types

Explicar que las etiquetas también pueden relacionarse con detección de información sensible.

Ejemplos:

```text
Credit Card Number

Passport Number

National ID

Social Security Number
```

---

# 24. Auto-labeling

Si aparece una opción relacionada con:

```text
Auto-labeling
```

mostrarla conceptualmente.

No es obligatorio configurarla en esta demo.

---

## Qué explicar

Auto-labeling puede permitir:

```text
Detect sensitive content
      ↓
Recommend or apply label
```

dependiendo de las capacidades disponibles.

---

# 25. Ejemplo de laboratorio

Podemos utilizar contenido ficticio como:

```text
111-11-1111
```

únicamente para pruebas controladas.

No usar PII real.

---

# 26. Revisar configuración

Antes de crear la etiqueta revisar:

```text
Name:
PII

Scope:
Items

Content marking:
Header
Footer
Watermark

Protection:
as configured
```

---

# 27. Crear la etiqueta

Seleccionar:

```text
Create label
```

o la opción equivalente.

---

# 28. Resultado esperado

Debe aparecer:

```text
PII
```

en la lista de Sensitivity Labels.

---

# 29. Importante: todavía NO está publicada

Explicar inmediatamente:

```text
Label created
≠
Users can use it
```

La etiqueta existe administrativamente.

Pero todavía debemos:

```text
Publish
```

---

# 30. Pregunta para la clase

> ¿Por qué un usuario podría no ver la etiqueta aunque ya la creamos?

Respuesta:

```text
Porque aún no fue publicada
```

o porque:

```text
la publicación todavía está propagándose
```

---

# 31. Modelo completo

Mostrar:

```text
CREATE
   ↓
PII Label
   ↓
PUBLISH
   ↓
Users
   ↓
Word / Excel / PowerPoint / Outlook
```

---

# 32. Relación con Microsoft 365 Apps

Conectar con Module 04:

```text
Microsoft 365 Apps
        ↓
User creates content
        ↓
Sensitivity Label
        ↓
Classification
        ↓
Protection
```

---

# 33. Relación con DLP

Conectar con Module 05:

```text
DLP
→ detects and controls activities
```

mientras:

```text
Sensitivity Label
→ classifies and protects content
```

---

# 34. Ejemplo comparativo

Archivo:

```text
Employees.xlsx
```

DLP puede detectar:

```text
Sensitive information
```

y aplicar:

```text
warning / block
```

Una Sensitivity Label puede marcarlo como:

```text
PII
```

y mantener esa clasificación asociada al documento.

---

# 35. Relación con Microsoft 365 Copilot

Explicar:

Copilot trabaja con contenido de Microsoft 365 respetando las capacidades de seguridad y cumplimiento configuradas en la organización.

Por eso:

```text
Identity

Permissions

DLP

Sensitivity Labels
```

forman parte de la preparación del entorno.

---

# 36. Propagación

Muy importante para la Clase 3:

```text
Label created
≠
Label immediately visible everywhere
```

La publicación y disponibilidad pueden requerir tiempo.

---

# 37. Estrategia de instructor

Antes de la clase es recomendable tener preparada una etiqueta adicional:

```text
LAB - Confidential
```

ya publicada.

Esto permite continuar el laboratorio si:

```text
PII
```

todavía no aparece para los alumnos.

---

# 38. Plan A

Si la nueva etiqueta aparece:

```text
usar PII
```

---

# 39. Plan B

Si todavía no aparece:

```text
usar LAB - Confidential
```

para demostrar:

```text
apply label
view marking
change label
remove label
```

---

# 40. No recrear la etiqueta por propagación

Si no aparece inmediatamente:

```text
NO crear PII2

NO crear PII-Test

NO crear varias copias
```

Primero revisar:

```text
Label exists

Publication policy

Users included

Propagation time
```

---

# 41. Qué NO hacer

No:

```text
usar información personal real

publicar globalmente sin necesidad

configurar cifrado que pueda bloquear al instructor

modificar etiquetas de producción

crear múltiples etiquetas duplicadas

asumir que la publicación es inmediata
```

---

# 42. Resultado pedagógico

El alumno debe poder explicar:

```text
What is a sensitivity label?

What is scope?

What is content marking?

What is encryption?

What is auto-labeling?

What is the difference between create and publish?
```

---

# 43. Resultado técnico

Al finalizar este demo tendremos:

```text
Sensitivity Label:
PII
```

configurada y lista para ser publicada.

---

# 44. Mensaje clave

> Una Sensitivity Label convierte la clasificación de información en una política visible y, cuando corresponde, en protección técnica aplicada directamente al contenido.

---

# 45. Transición

Siguiente demo:

```text
DEMO 02
Publish and Test Sensitivity Label
```

Ahí haremos:

```text
Publish PII
      ↓
Assign users
      ↓
Wait / validate
      ↓
Open Word
      ↓
Apply label
      ↓
Observe protection
```
