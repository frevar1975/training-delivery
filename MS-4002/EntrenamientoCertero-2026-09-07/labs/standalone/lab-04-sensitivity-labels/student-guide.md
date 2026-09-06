# MS-4002 - Lab 04
## Implementar y probar etiquetas de confidencialidad con Microsoft Purview

**Modalidad:** Standalone  
**Entorno:** Tenant Microsoft 365 de práctica  
**Duración estimada:** 75-90 minutos

---

# 1. Objetivos

Al finalizar este laboratorio podrás:

- acceder a Information Protection en Microsoft Purview;
- comprender el propósito de las Sensitivity Labels;
- revisar la integración con SharePoint y OneDrive;
- crear una etiqueta de confidencialidad;
- configurar el ámbito de una etiqueta;
- configurar protección mediante cifrado;
- aplicar marcas visuales al contenido;
- configurar detección de información sensible;
- publicar una etiqueta;
- crear una política de publicación;
- comprender el tiempo de propagación;
- aplicar una etiqueta desde Word;
- comprobar marcas visuales;
- probar la eliminación de una etiqueta con justificación.

---

# 2. Escenario

La organización necesita clasificar y proteger documentos que contienen información de identificación personal.

Crearemos una etiqueta:

```text
PII
```

que representa:

```text
Personally Identifiable Information
```

El flujo conceptual será:

```text
Documento
    |
    v
Información sensible
    |
    v
Sensitivity Label
    |
    +---- Clasificación
    |
    +---- Marcado visual
    |
    +---- Protección
    |
    +---- Control de acceso
```

---

# 3. Diferencia entre DLP y Sensitivity Labels

En el laboratorio anterior utilizamos DLP.

DLP responde principalmente a:

```text
¿Qué está intentando hacer el usuario
con información sensible?
```

Sensitivity Labels responden principalmente a:

```text
¿Qué clasificación tiene esta información
y cómo debe protegerse?
```

Ambas capacidades pueden trabajar juntas.

---

# 4. Entorno Standalone

No utilizaremos:

- LON-CL1;
- LON-CL2;
- usuarios precargados de XtremeLabs;
- la etiqueta Project - Falcon como requisito;
- credenciales proporcionadas por un proveedor.

Utilizaremos:

```text
PC del alumno
    |
    +---- Microsoft Purview
    |
    +---- Microsoft 365
    |
    +---- Word para la Web
    |
    +---- SharePoint / OneDrive
```

---

# 5. Requisitos

Antes de comenzar confirma:

- acceso al tenant Microsoft 365 de práctica;
- acceso a Microsoft Purview;
- permisos para administrar Information Protection;
- acceso a Word para la Web;
- OneDrive disponible;
- una cuenta de prueba con licencia adecuada.

> IMPORTANTE
>
> No realizar este laboratorio en un tenant de producción.

---

# 6. Consideración sobre el cliente Microsoft Purview Information Protection

El laboratorio XtremeLabs incluye la instalación del cliente Microsoft Purview Information Protection en su VM.

En la modalidad Standalone:

**no instalaremos este cliente como requisito inicial del laboratorio.**

Trabajaremos principalmente con:

- Microsoft Purview;
- Word para la Web;
- SharePoint;
- OneDrive.

Si el instructor determina que el entorno necesita componentes adicionales para una funcionalidad concreta, esa instalación se realizará como actividad adicional.

---

# 7. PARTE 1 - Abrir Microsoft Purview

Accede al portal de Microsoft Purview utilizando la dirección indicada por el instructor.

Inicia sesión con la cuenta administrativa del tenant de práctica.

Selecciona:

**Solutions**

Luego:

**Information Protection**

Selecciona:

**Sensitivity labels**

---

# 8. Explorar Sensitivity Labels

Observa las etiquetas existentes.

Dependiendo del tenant puedes encontrar:

- etiquetas existentes;
- subetiquetas;
- ninguna etiqueta personalizada.

No es necesario que exista:

```text
Project - Falcon
```

Nuestra versión Standalone no depende de ella.

---

# 9. PARTE 2 - SharePoint y OneDrive

En:

**Information Protection > Sensitivity labels**

revisa si aparece un mensaje indicando que la organización todavía no ha habilitado el procesamiento de contenido con etiquetas de confidencialidad cifradas en Office para la Web, SharePoint y OneDrive.

Si aparece:

selecciona:

**Turn on now**

Si no aparece:

la característica probablemente ya está habilitada en el tenant.

---

# 10. Qué habilita esta configuración

Esta capacidad permite que SharePoint y OneDrive puedan trabajar con archivos compatibles que tengan etiquetas de confidencialidad.

Conceptualmente:

```text
Archivo
    |
    v
Sensitivity Label
    |
    v
SharePoint / OneDrive
    |
    +---- Procesamiento
    +---- Colaboración
    +---- DLP
    +---- Search
    +---- eDiscovery
```

---

# 11. Tiempo de propagación

Los cambios realizados a nivel del tenant pueden requerir tiempo para aplicarse.

No asumas que un cambio que acabas de realizar aparecerá inmediatamente en todas las aplicaciones.

---

# 12. PARTE 3 - Protección de PDF

En Microsoft Purview abre:

**Information Protection**

Busca:

**Auto-labeling policies**

Si aparece una opción o banner relacionado con:

```text
Protect PDFs with Auto-labeling
```

revisa la configuración.

Si el instructor confirma que el tenant es exclusivamente de laboratorio, habilita la característica según las opciones disponibles.

Si no aparece:

continúa con el laboratorio.

---

# 13. PARTE 4 - Crear la etiqueta

Regresa a:

**Information Protection > Sensitivity labels**

Selecciona:

**Create a label**

---

# 14. Información básica

Configura:

**Name**

```text
PII
```

**Display name**

```text
PII
```

**Description for users**

```text
Documents, files, and emails with PII
```

**Description for admins**

```text
Documents, files, and emails with PII
```

Selecciona un color para identificar visualmente la etiqueta.

Selecciona:

**Next**

---

# 15. Definir Scope

En el ámbito de la etiqueta, selecciona los tipos de elementos requeridos para el laboratorio.

El laboratorio original utiliza:

- Files & other data assets;
- Emails;
- Meetings.

Mantén:

**Items**

seleccionado.

Selecciona:

**Next**

---

# 16. PARTE 5 - Configurar protección

En:

**Choose protection settings**

selecciona:

**Control access**

y:

**Apply content marking**

Selecciona:

**Next**

---

# 17. Qué significa Control access

Control access permite asociar protección a los elementos etiquetados.

Conceptualmente:

```text
PII
 |
 v
Control access
 |
 v
Encryption
 |
 v
Authorized users
```

La protección puede mantenerse incluso cuando el archivo cambia de ubicación.

---

# 18. Configurar acceso

En la página de control de acceso, utiliza las opciones indicadas por el instructor.

El objetivo es configurar protección para el contenido etiquetado como:

```text
PII
```

Evita utilizar usuarios personales o externos reales durante el laboratorio.

Utiliza únicamente identidades de prueba del tenant.

---

# 19. PARTE 6 - Content marking

Configura marcas visuales para que el usuario pueda reconocer inmediatamente la clasificación del documento.

Activa las opciones de marcado que estén disponibles.

Puedes utilizar:

- Header;
- Footer;
- Watermark.

---

# 20. Header

Configura un encabezado similar a:

```text
PII - CONFIDENTIAL
```

---

# 21. Footer

Configura un pie de página similar a:

```text
Contains Personally Identifiable Information
```

---

# 22. Watermark

Configura:

```text
CONFIDENTIAL - PII
```

Si existe la opción de orientación:

selecciona una presentación diagonal.

---

# 23. Resultado conceptual

Cuando se aplique la etiqueta:

```text
Documento
    |
    v
PII
    |
    +---- Header
    |
    +---- Footer
    |
    +---- Watermark
    |
    +---- Protection
```

---

# 24. PARTE 7 - Auto-labeling

Si el asistente de creación de la etiqueta ofrece configuración de auto-labeling para archivos y correos, revisa esta sección.

El objetivo es que Microsoft 365 pueda identificar determinados tipos de información sensible.

---

# 25. Sensitive Info Types

Busca tipos relacionados con información de identificación personal.

El laboratorio original utiliza ejemplos como:

```text
U.S. Social Security Number
```

y referencias a información financiera sensible.

Selecciona los tipos indicados por el instructor si la funcionalidad está disponible.

---

# 26. Qué significa Auto-labeling

Conceptualmente:

```text
Documento
    |
    v
Contenido
    |
    v
Sensitive Info Type
    |
    v
Coincidencia
    |
    v
Sensitivity Label
```

Esto permite que la clasificación no dependa exclusivamente de que el usuario identifique manualmente el contenido.

---

# 27. Protección para Groups and Sites

Si aparece:

**Define protection settings for groups and sites**

no habilites opciones adicionales para este laboratorio salvo indicación del instructor.

Selecciona:

**Next**

---

# 28. Schematized data assets

Si aparece una sección relacionada con:

```text
Auto-labeling for schematized data assets
```

no la habilites para este ejercicio.

Selecciona:

**Next**

---

# 29. Crear etiqueta

En:

**Review your settings and finish**

revisa:

- Name;
- Scope;
- Protection;
- Content marking;
- Auto-labeling si se configuró.

Selecciona:

**Create label**

---

# 30. No publicar automáticamente todavía

Cuando el asistente pregunte por la creación de una política:

selecciona la opción equivalente a:

```text
Don't create a policy yet
```

Selecciona:

**Done**

---

# 31. Validar creación

Regresa a:

**Sensitivity labels**

Busca:

```text
PII
```

Si no aparece inmediatamente:

selecciona:

**Refresh**

---

# 32. PARTE 8 - Publicar la etiqueta

Selecciona:

```text
PII
```

Luego selecciona:

**Publish label**

Esto inicia el asistente para crear una política de publicación.

---

# 33. Elegir etiquetas

Verifica que aparezca:

```text
PII
```

Selecciona:

**Next**

---

# 34. Administrative Units

Para un tenant dedicado a capacitación puedes mantener la configuración indicada por el instructor.

Selecciona:

**Next**

---

# 35. Usuarios y grupos

Para nuestra modalidad Standalone es preferible limitar inicialmente la publicación a usuarios de laboratorio cuando el portal permita hacerlo.

Por ejemplo:

```text
LAB-User1
LAB-User2
```

Si el tenant está dedicado exclusivamente a capacitación, el instructor puede decidir publicarla a todos los usuarios.

---

# 36. Política de justificación

En:

**Policy settings**

activa:

```text
Users must provide a justification to remove a label or lower its classification
```

Esta configuración será importante para la prueba posterior.

---

# 37. Default labels

El laboratorio original configura PII como etiqueta predeterminada para varios tipos de contenido.

En Standalone, no estableceremos una etiqueta predeterminada global para todo el tenant salvo indicación del instructor.

Si el tenant es exclusivamente de laboratorio, el instructor puede decidir reproducir la configuración original.

---

# 38. Nombre de la política

Configura:

**Name**

```text
PII Policy
```

Descripción:

```text
Publishes the PII sensitivity label for the MS-4002 lab and requires justification when the label is removed or its classification is lowered.
```

---

# 39. Crear política

Revisa la configuración.

Selecciona:

**Submit**

Espera la confirmación.

Selecciona:

**Done**

---

# 40. PARTE 9 - Propagación

> IMPORTANTE
>
> Una etiqueta recién publicada y su política pueden tardar en aparecer en aplicaciones como Word y Outlook.

El laboratorio original advierte que este proceso puede tardar hasta:

```text
24 horas
```

Por este motivo:

**no dependemos de que PII aparezca inmediatamente durante la clase.**

---

# 41. Estrategia Standalone

Tenemos dos escenarios:

```text
PII disponible
     |
     v
Probar PII


PII no disponible
     |
     v
Continuar con explicación
     |
     v
Probar posteriormente
```

No recrees la etiqueta.

No recrees la política.

---

# 42. Recomendación para una clase real

El instructor puede preparar previamente una etiqueta de prueba publicada con suficiente anticipación.

Ejemplo:

```text
LAB - Confidential
```

Esto permite:

```text
Clase
 |
 +---- Crear PII
 |
 +---- Explicar publicación
 |
 +---- Probar LAB - Confidential
```

sin depender de la propagación de PII.

---

# 43. PARTE 10 - Probar la etiqueta

Esta sección solo se realiza si:

- PII ya aparece en Word;

o:

- el instructor dispone de una etiqueta de prueba prepublicada.

Abre:

**Microsoft 365**

Luego:

**Word**

Selecciona:

**Blank document**

---

# 44. Crear contenido de prueba

Escribe:

```text
MS-4002 Sensitivity Label Test

This document contains sample personally identifiable information for a training exercise.

Sample SSN: 111-11-1111
```

> IMPORTANTE
>
> El valor anterior es exclusivamente un dato de laboratorio.
>
> No utilizar información personal real.

---

# 45. Aplicar etiqueta

En Word busca:

**Sensitivity**

Selecciona:

```text
PII
```

o la etiqueta prepublicada indicada por el instructor.

---

# 46. Resultado esperado

Dependiendo de la configuración de la etiqueta deberías observar elementos como:

```text
Header
Footer
Watermark
Sensitivity indicator
```

---

# 47. Revisar marca visual

Comprueba si aparece:

```text
CONFIDENTIAL - PII
```

o la marca configurada por el instructor.

---

# 48. Reading View

Si Word para la Web no muestra el watermark exactamente como esperas durante la edición:

abre:

**View**

y utiliza una vista de lectura si está disponible.

La representación de la marca puede variar entre:

- Word para la Web;
- modo de lectura;
- aplicación Word de escritorio.

---

# 49. PARTE 11 - Probar justificación

Con la etiqueta aplicada:

abre nuevamente:

**Sensitivity**

Intenta:

- eliminar la etiqueta;

o:

- cambiar a una clasificación inferior, si existe.

---

# 50. Resultado esperado

La política debería solicitar una justificación.

Conceptualmente:

```text
PII
 |
 v
Remove / Downgrade
 |
 v
Justification Required
 |
 v
Reason
 |
 v
Continue
```

---

# 51. Introducir justificación

Selecciona la opción disponible para proporcionar una explicación.

Utiliza:

```text
Authorized MS-4002 lab test.
```

Confirma la operación.

---

# 52. Qué demuestra esta prueba

La clasificación puede modificarse, pero la organización puede exigir que el usuario explique por qué.

Esto proporciona:

- control;
- responsabilidad;
- trazabilidad.

---

# 53. PARTE 12 - Compartir el documento

Si el instructor lo indica, guarda el documento en:

**OneDrive**

o:

**SharePoint**

Utiliza únicamente usuarios de laboratorio.

No utilices una cuenta personal externa como requisito del ejercicio.

---

# 54. Probar acceso

Comparte el documento con:

```text
LAB-User2
```

según las opciones permitidas por la configuración de la etiqueta.

---

# 55. Qué observar

La etiqueta puede combinar:

```text
Clasificación
+
Marcado
+
Cifrado
+
Permisos
```

La capacidad exacta dependerá de cómo se haya configurado la etiqueta.

---

# 56. PARTE 13 - Revisar la etiqueta en Purview

Regresa a:

**Microsoft Purview > Information Protection > Sensitivity labels**

Selecciona:

```text
PII
```

Revisa su configuración.

---

# 57. Revisar política

Revisa:

```text
PII Policy
```

Confirma:

- etiqueta publicada;
- usuarios/grupos;
- policy settings;
- requisito de justificación.

---

# 58. Troubleshooting - PII no aparece en Word

Esta es una situación esperable inmediatamente después de publicar una etiqueta.

No recrees la etiqueta.

No recrees la política.

Revisa:

1. que PII exista;
2. que PII esté publicada;
3. que el usuario esté incluido;
4. que la política esté activa;
5. que Word esté conectado con el usuario correcto;
6. que haya transcurrido suficiente tiempo.

---

# 59. No aparece Sensitivity en Word

Posibles causas:

- configuración del tenant;
- licencia;
- política todavía no propagada;
- usuario fuera de alcance;
- sesión de Office desactualizada.

Cierra sesión y vuelve a iniciar sesión solamente si el instructor lo indica.

---

# 60. No aparece el watermark

Revisa:

- configuración de Content marking;
- etiqueta aplicada;
- vista utilizada en Word.

Prueba:

**Reading View**

si está disponible.

---

# 61. No solicita justificación

Revisa:

```text
PII Policy
```

y confirma:

```text
Users must provide a justification to remove a label or lower its classification
```

También confirma que la política se haya propagado.

---

# 62. SharePoint o OneDrive no procesan correctamente el archivo

Revisa si se habilitó el procesamiento de archivos etiquetados en:

**Information Protection**

Los cambios del tenant pueden requerir tiempo para propagarse.

---

# 63. Limpieza

No elimines inmediatamente:

```text
PII
PII Policy
```

Pueden reutilizarse posteriormente.

El instructor decidirá si:

- conservarlos;
- deshabilitar la política;
- eliminar la política;
- eliminar la etiqueta.

---

# 64. Validación final

Confirma:

- [ ] Accedí a Microsoft Purview.
- [ ] Revisé Information Protection.
- [ ] Revisé la integración con SharePoint y OneDrive.
- [ ] Creé la etiqueta PII.
- [ ] Configuré el Scope.
- [ ] Revisé Control access.
- [ ] Configuré Content marking.
- [ ] Configuré Header.
- [ ] Configuré Footer.
- [ ] Configuré Watermark.
- [ ] Revisé Auto-labeling.
- [ ] Publiqué PII.
- [ ] Creé PII Policy.
- [ ] Configuré justificación para eliminar o bajar clasificación.
- [ ] Comprendí el tiempo de propagación.
- [ ] Probé una etiqueta publicada si estaba disponible.
- [ ] Revisé la marca visual.
- [ ] Probé la justificación si la política ya estaba disponible.

---

# 65. Mapeo XtremeLabs -> Standalone

| XtremeLabs | Standalone |
|---|---|
| LON-CL1 | PC del alumno |
| Holly Dickson | Usuario LAB |
| Tenant Adatum preparado | Tenant Microsoft 365 de práctica |
| Purview client predefinido como requisito | No requerido inicialmente |
| Project - Falcon | PII o etiqueta LAB prepublicada |
| Etiquetas precargadas | Etiquetas propias del tenant |
| Credenciales del proveedor | Credenciales del tenant de práctica |

---

# 66. Resultado final

El alumno debería comprender:

```text
Información
     |
     v
Clasificación
     |
     v
Sensitivity Label
     |
     +---- Content Marking
     |
     +---- Encryption
     |
     +---- Access Control
     |
     +---- Auto-labeling
     |
     v
Label Policy
     |
     v
Usuarios
```

---

# 67. Relación con DLP

Ahora podemos relacionar los dos últimos laboratorios:

```text
Sensitivity Labels
        |
        v
¿Qué es esta información?
        |
        v
Clasificar y proteger


DLP
        |
        v
¿Qué están haciendo con ella?
        |
        v
Detectar y controlar
```

---

# 68. Relación con Microsoft 365 Copilot

Microsoft 365 Copilot trabaja respetando los permisos y controles de Microsoft 365.

Por eso, antes de una implementación amplia de Copilot, una organización debe revisar:

```text
Identidades
    +
Permisos
    +
Acceso
    +
Clasificación
    +
Protección de información
```

Las Sensitivity Labels forman parte de esta estrategia de preparación y gobierno de la información.

---

# 69. Fin del laboratorio

Has completado los cuatro laboratorios principales de la modalidad Standalone:

```text
Lab 01
Tenant
   |
   v
Lab 02
Identity + Security + Roles
   |
   v
Lab 03
DLP
   |
   v
Lab 04
Sensitivity Labels
```

El siguiente paso será revisar cómo estos controles se relacionan con la preparación de seguridad y cumplimiento para Microsoft 365 Copilot.