# MS-4002 - Lab 04
## Guía del instructor - Microsoft Purview Sensitivity Labels

**Modalidad:** Standalone  
**Curso:** MS-4002 - Prepare security and compliance to support Microsoft 365 Copilot  
**Duración sugerida:** 75-90 minutos

---

# 1. Propósito del laboratorio

Este laboratorio adapta la práctica de Sensitivity Labels del entorno XtremeLabs a un escenario Standalone.

El objetivo es enseñar cómo Microsoft Purview permite:

- clasificar información;
- aplicar protección;
- agregar marcas visuales;
- publicar etiquetas;
- exigir justificación cuando una clasificación se elimina o reduce;
- integrar la clasificación con Microsoft 365.

El alumno utilizará:

- su propia PC;
- Microsoft Purview;
- Word para la Web;
- OneDrive o SharePoint;
- un tenant Microsoft 365 de práctica.

No se requiere:

- LON-CL1;
- LON-CL2;
- usuarios precargados;
- etiquetas precargadas;
- credenciales de XtremeLabs.

---

# 2. Objetivos didácticos

Al finalizar el laboratorio el alumno debería comprender:

- qué es una Sensitivity Label;
- diferencia entre clasificación y protección;
- cómo crear una etiqueta;
- cómo definir su Scope;
- cómo configurar Control access;
- cómo configurar Content marking;
- cómo funcionan Header, Footer y Watermark;
- qué relación existe con Sensitive Info Types;
- cómo publicar una etiqueta;
- qué función cumple una Label Policy;
- cómo exigir justificación;
- cómo probar una etiqueta desde Word;
- cómo afecta la propagación al laboratorio.

---

# 3. Clasificación de actividades

## ALUMNO

El alumno realiza directamente la configuración.

## DEMO INSTRUCTOR

El instructor demuestra o explica una característica.

## OPCIONAL

Actividad que puede omitirse dependiendo de:

- tiempo;
- licencia;
- permisos;
- propagación;
- características disponibles en el tenant.

---

# 4. Preparación previa del instructor

Antes de la clase validar:

- acceso a Microsoft Purview;
- permisos administrativos suficientes;
- acceso a Information Protection;
- acceso a Sensitivity labels;
- OneDrive disponible;
- Word para la Web disponible;
- al menos un usuario LAB con licencia adecuada.

Usuarios sugeridos:

```text
LAB-User1
LAB-User2
```

---

# 5. Preparación especialmente importante

Las etiquetas publicadas pueden tardar en aparecer en las aplicaciones.

Por este motivo se recomienda preparar previamente una etiqueta sencilla.

Ejemplo:

```text
LAB - Confidential
```

Publicarla antes de la clase a:

```text
LAB-User1
LAB-User2
```

La etiqueta prepublicada servirá únicamente para la demostración si:

```text
PII
```

todavía no se propagó.

---

# 6. Estrategia del laboratorio

El laboratorio tiene dos objetivos diferentes:

```text
CONFIGURAR
    |
    v
Crear PII


PROBAR
    |
    v
PII si está disponible
    |
    OR
    |
    v
LAB - Confidential
```

Esto evita depender de la propagación durante la clase.

---

# 7. Seguridad del laboratorio

> IMPORTANTE
>
> No utilizar información personal real.
>
> No utilizar documentos reales de la organización.
>
> No publicar etiquetas globalmente en un tenant de producción.
>
> No configurar cifrado para usuarios reales durante una demostración.
>
> Utilizar exclusivamente identidades y documentos de laboratorio.

---

# 8. PARTE 1 - Introducción a Sensitivity Labels

## Tipo

**DEMO INSTRUCTOR**

## Tiempo sugerido

5 minutos

Comenzar preguntando:

```text
¿Cómo sabe una organización que un documento es confidencial?
```

Explicar que una Sensitivity Label permite asociar una clasificación con controles de protección.

---

# 9. Analogía

Utilizar el ejemplo de una carpeta física.

Una organización puede marcarla:

```text
PÚBLICO

INTERNO

CONFIDENCIAL

ALTAMENTE CONFIDENCIAL
```

La etiqueta indica cómo debe tratarse la información.

En Microsoft 365:

```text
Documento
    |
    v
Sensitivity Label
    |
    +---- Clasificación
    |
    +---- Protección
    |
    +---- Marcado
    |
    +---- Control de acceso
```

---

# 10. Diferencia entre etiqueta y política

Este punto debe quedar muy claro.

## Sensitivity Label

Define:

```text
QUÉ significa la clasificación
```

y qué protección puede aplicar.

## Label Policy

Define:

```text
QUIÉN recibe la etiqueta
```

y determinados comportamientos asociados.

---

# 11. Analogía etiqueta vs política

La etiqueta es:

```text
CONFIDENTIAL
```

La política determina:

```text
¿Quién puede utilizar CONFIDENTIAL?
```

Por eso:

```text
Crear etiqueta
      !=
Publicar etiqueta
```

---

# 12. PARTE 2 - Microsoft Purview

## Tipo

**ALUMNO**

## Tiempo sugerido

5 minutos

Mostrar:

**Microsoft Purview > Solutions > Information Protection**

Luego:

**Sensitivity labels**

---

# 13. Qué explicar

Information Protection permite administrar clasificación y protección de información.

Mostrar las áreas disponibles sin detenerse demasiado en cada una.

El objetivo principal es:

```text
Sensitivity labels
```

---

# 14. PARTE 3 - SharePoint y OneDrive

## Tipo

**DEMO INSTRUCTOR**

Revisar si el tenant solicita habilitar el procesamiento de archivos etiquetados en:

- SharePoint;
- OneDrive;
- Office para la Web.

Si aparece:

```text
Turn on now
```

explicar la función.

---

# 15. Qué explicar

Sin integración con SharePoint y OneDrive, determinados escenarios de archivos etiquetados pueden no funcionar como se espera.

Conceptualmente:

```text
Sensitivity Label
       |
       v
Document
       |
       v
SharePoint / OneDrive
       |
       +---- Search
       +---- Collaboration
       +---- DLP
       +---- eDiscovery
```

---

# 16. PARTE 4 - Protección de PDF

## Tipo

**OPCIONAL / DEMO INSTRUCTOR**

Si aparece una opción relacionada con:

```text
Protect PDFs with Auto-labeling
```

mostrarla.

No convertir esta configuración en requisito para completar el laboratorio.

---

# 17. PARTE 5 - Crear PII

## Tipo

**ALUMNO**

## Tiempo sugerido

20 minutos

Seleccionar:

**Create a label**

Configurar:

```text
Name:
PII

Display name:
PII
```

Descripción para usuarios:

```text
Documents, files, and emails with PII
```

Descripción administrativa:

```text
Documents, files, and emails with PII
```

---

# 18. Explicar PII

PII significa:

```text
Personally Identifiable Information
```

No utilizar datos personales reales para demostrarlo.

---

# 19. Scope

Mostrar el concepto de Scope.

La etiqueta puede estar disponible para diferentes tipos de recursos.

Para este laboratorio concentrarse principalmente en:

```text
Items
```

que puede incluir:

```text
Files
Emails
Meetings
```

según las opciones actuales del tenant.

---

# 20. Analogía de Scope

Una etiqueta puede diseñarse para:

```text
Documento
Correo
Reunión
Grupo
Sitio
```

No todas las etiquetas tienen que utilizarse para todos los recursos.

---

# 21. PARTE 6 - Protection settings

## Tipo

**ALUMNO**

Seleccionar según disponibilidad:

```text
Control access
```

y:

```text
Apply content marking
```

---

# 22. Control access

Explicar que una etiqueta puede hacer más que mostrar:

```text
CONFIDENTIAL
```

También puede proteger el contenido.

---

# 23. Analogía

Una etiqueta física puede decir:

```text
CONFIDENTIAL
```

pero una Sensitivity Label puede además:

```text
CONFIDENTIAL
+
LOCK
```

Es decir:

```text
Clasificación
+
Protección
```

---

# 24. Encryption

## Tipo

**DEMO INSTRUCTOR + ALUMNO SEGÚN TENANT**

Mostrar las opciones disponibles para controlar acceso mediante cifrado.

Utilizar únicamente usuarios LAB.

No utilizar:

- correos personales;
- usuarios externos reales;
- información empresarial.

---

# 25. Qué explicar sobre cifrado

Conceptualmente:

```text
Documento
    |
    v
PII
    |
    v
Encryption
    |
    v
Authorized identities
```

La protección puede acompañar al archivo.

---

# 26. PARTE 7 - Content marking

## Tipo

**ALUMNO**

## Tiempo sugerido

10 minutos

Configurar:

### Header

```text
PII - CONFIDENTIAL
```

### Footer

```text
Contains Personally Identifiable Information
```

### Watermark

```text
CONFIDENTIAL - PII
```

---

# 27. Qué explicar sobre Content Marking

Content Marking permite que la clasificación sea visible.

Ejemplo:

```text
             CONFIDENTIAL - PII


        Información del documento


Contains Personally Identifiable Information
```

---

# 28. Clasificación vs marcado

Explicar:

```text
Sensitivity Label
```

no es simplemente un watermark.

El watermark es solamente una de las acciones que puede producir la etiqueta.

---

# 29. PARTE 8 - Auto-labeling

## Tipo

**DEMO INSTRUCTOR / OPCIONAL**

Mostrar la sección si aparece durante el asistente.

Explicar la relación:

```text
Contenido
    |
    v
Sensitive Info Type
    |
    v
Coincidencia
    |
    v
Label
```

---

# 30. Ejemplo

Utilizar conceptualmente:

```text
U.S. Social Security Number
```

No utilizar números pertenecientes a personas reales.

---

# 31. Qué explicar

Manual labeling:

```text
Usuario decide
    |
    v
PII
```

Auto-labeling:

```text
Sistema detecta contenido
    |
    v
PII
```

---

# 32. Groups and Sites

## Tipo

**OPCIONAL**

Si el asistente muestra:

```text
Define protection settings for groups and sites
```

no configurarlo para este laboratorio salvo que el instructor quiera ampliar el ejercicio.

---

# 33. Schematized data assets

## Tipo

**OPCIONAL**

Si aparece:

```text
Auto-labeling for schematized data assets
```

explicar brevemente que Purview puede extender clasificación a otros tipos de activos.

No habilitar para este ejercicio.

---

# 34. Crear etiqueta

## Tipo

**ALUMNO**

Revisar:

- nombre;
- scope;
- protección;
- content marking;
- auto-labeling.

Seleccionar:

**Create label**

---

# 35. Punto crítico

Al terminar la creación:

**no asumir que la etiqueta ya está disponible para los usuarios.**

Todavía falta:

```text
PUBLICAR
```

---

# 36. PARTE 9 - Publicar PII

## Tipo

**ALUMNO**

## Tiempo sugerido

15 minutos

Seleccionar:

```text
PII
```

Luego:

```text
Publish label
```

---

# 37. Label Policy

Crear:

```text
PII Policy
```

Descripción:

```text
Publishes the PII sensitivity label for the MS-4002 lab and requires justification when the label is removed or its classification is lowered.
```

---

# 38. Usuarios

Preferir:

```text
LAB-User1
LAB-User2
```

si el portal permite limitar fácilmente la política.

Evitar:

```text
All users
```

en tenants compartidos.

---

# 39. Justificación

Activar:

```text
Users must provide a justification to remove a label or lower its classification
```

---

# 40. Qué explicar

Esto introduce control cuando un usuario intenta reducir la protección.

```text
PII
 |
 v
Remove / Downgrade
 |
 v
Justification
 |
 v
Audit
```

---

# 41. Analogía

Un empleado tiene un documento:

```text
CONFIDENTIAL
```

y quiere convertirlo en:

```text
PUBLIC
```

La organización puede decir:

```text
Puedes hacerlo,
pero tienes que explicar por qué.
```

---

# 42. Default Label

El laboratorio original puede configurar PII como etiqueta predeterminada.

En Standalone:

**no hacerlo globalmente por defecto.**

Solo utilizarlo si:

- tenant exclusivo de laboratorio;
- instructor conoce el impacto;
- es necesario para la demostración.

---

# 43. Crear PII Policy

Revisar configuración.

Seleccionar:

```text
Submit
```

Esperar confirmación.

---

# 44. PARTE 10 - Explicar propagación

## Tipo

**DEMO INSTRUCTOR**

Este es uno de los puntos más importantes del laboratorio.

Una etiqueta recién publicada puede no aparecer inmediatamente.

El laboratorio fuente advierte que la propagación puede tardar hasta 24 horas.

Por eso no debemos construir una clase que dependa de que PII aparezca inmediatamente.

---

# 45. Flujo de propagación

Explicar:

```text
Create Label
      |
      v
Publish Label
      |
      v
Label Policy
      |
      v
Microsoft 365 services
      |
      v
User applications
```

Existe tiempo entre estos pasos.

---

# 46. Estrategia para la clase

Si PII aparece:

```text
Usar PII
```

Si PII todavía no aparece:

```text
Usar LAB - Confidential
```

prepublicada previamente.

---

# 47. Diferencia con XtremeLabs

XtremeLabs puede disponer de una etiqueta previamente preparada:

```text
Project - Falcon
```

para poder realizar inmediatamente la prueba.

Nuestra versión Standalone utiliza el mismo principio, pero sin depender de contenido precargado.

Usamos:

```text
LAB - Confidential
```

preparada por el instructor.

---

# 48. PARTE 11 - Prueba desde Word

## Tipo

**ALUMNO**

## Tiempo sugerido

15 minutos

Abrir:

**Microsoft 365 > Word**

Crear:

**Blank document**

---

# 49. Contenido de prueba

Utilizar:

```text
MS-4002 Sensitivity Label Test

This document contains sample personally identifiable information for a training exercise.

Sample SSN: 111-11-1111
```

Aclarar:

**el valor es exclusivamente de laboratorio.**

---

# 50. Aplicar Sensitivity Label

Buscar:

```text
Sensitivity
```

Aplicar:

```text
PII
```

si está disponible.

En caso contrario:

```text
LAB - Confidential
```

---

# 51. Qué observar

Mostrar:

- indicador de sensibilidad;
- Header;
- Footer;
- Watermark;
- posibles restricciones.

---

# 52. Resultado conceptual

```text
Word document
      |
      v
Sensitivity
      |
      v
PII
      |
      +---- Header
      +---- Footer
      +---- Watermark
      +---- Protection
```

---

# 53. Watermark no visible inmediatamente

## Tipo

**DEMO INSTRUCTOR**

Si el watermark no aparece exactamente como se esperaba durante la edición:

probar:

```text
View
```

y una vista de lectura si está disponible.

Explicar que la representación puede variar entre:

- Word para la Web;
- Reading View;
- Word Desktop.

---

# 54. PARTE 12 - Justificación

## Tipo

**ALUMNO**

Intentar:

- eliminar la etiqueta;

o:

- bajar la clasificación.

---

# 55. Resultado esperado

Debe aparecer una solicitud de justificación si la política ya se propagó.

Ejemplo:

```text
Authorized MS-4002 lab test.
```

---

# 56. Qué explicar

El objetivo no es impedir absolutamente toda modificación.

El objetivo es:

```text
Control
+
Justificación
+
Trazabilidad
```

---

# 57. PARTE 13 - OneDrive / SharePoint

## Tipo

**OPCIONAL / ALUMNO**

Guardar el documento en:

```text
OneDrive
```

o:

```text
SharePoint
```

Compartir únicamente con:

```text
LAB-User2
```

---

# 58. Qué demostrar

Mostrar que la clasificación forma parte del documento y puede interactuar con los servicios de Microsoft 365.

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
 +---- Access
 +---- DLP
 +---- Search
 +---- Compliance
```

---

# 59. PARTE 14 - Revisar configuración en Purview

## Tipo

**ALUMNO**

Regresar a:

**Information Protection**

Revisar:

```text
PII
```

y:

```text
PII Policy
```

---

# 60. Comparación con DLP

Esta comparación debe hacerse antes de terminar.

| Sensitivity Labels | DLP |
|---|---|
| Clasifica | Detecta uso |
| Puede proteger | Puede bloquear |
| Puede cifrar | Puede advertir |
| Puede marcar | Puede generar Policy Tips |
| Viaja con el contenido según configuración | Evalúa actividades y ubicaciones |

---

# 61. Explicación simple

Sensitivity Label:

```text
¿Qué ES este documento?
```

DLP:

```text
¿Qué están HACIENDO con este documento o sus datos?
```

---

# 62. Cómo trabajan juntas

Ejemplo conceptual:

```text
Documento
    |
    v
PII Label
    |
    v
Usuario intenta compartir
    |
    v
DLP
    |
    v
Block / Notify / Allow
```

---

# 63. Troubleshooting - PII no aparece

No recrear inmediatamente:

```text
PII
```

No recrear:

```text
PII Policy
```

Primero revisar:

```text
1. Label created?
2. Label published?
3. User included?
4. Policy active?
5. Correct Office account?
6. Propagation completed?
```

---

# 64. Sensitivity no aparece en Word

Posibles causas:

- licencia;
- política;
- propagación;
- usuario fuera del alcance;
- sesión de Office;
- características del tenant.

Plan B:

```text
DEMO INSTRUCTOR
```

o utilizar:

```text
LAB - Confidential
```

---

# 65. No aparece el Watermark

Revisar:

```text
PII
>
Content marking
```

Confirmar que:

```text
Watermark = Enabled
```

Luego revisar la vista utilizada en Word.

---

# 66. No solicita justificación

Revisar:

```text
PII Policy
```

Confirmar:

```text
Users must provide a justification
to remove a label or lower its classification
```

También considerar propagación.

---

# 67. El cifrado impide abrir el documento

Revisar:

- usuarios autorizados;
- cuenta utilizada;
- configuración de Encryption;
- permisos del documento.

No modificar permisos de usuarios reales durante la clase.

---

# 68. Plan B si la propagación impide las pruebas

No detener la clase.

Continuar con:

```text
Configuración
    |
    v
Explicación
    |
    v
Etiqueta prepublicada
    |
    v
Demo
```

---

# 69. Limpieza

No eliminar inmediatamente:

```text
PII
PII Policy
```

El instructor decidirá si:

- conservar;
- deshabilitar;
- modificar;
- eliminar posteriormente.

---

# 70. Qué ejecuta el alumno

## ALUMNO

- acceder a Purview;
- revisar Information Protection;
- crear PII;
- configurar Scope;
- configurar Content Marking;
- revisar Control access;
- publicar PII;
- crear PII Policy;
- configurar justificación;
- aplicar una etiqueta si está disponible;
- probar justificación.

---

# 71. Qué realiza el instructor

## DEMO INSTRUCTOR

- explicar Sensitivity Labels;
- explicar clasificación vs protección;
- explicar Scope;
- revisar integración SharePoint/OneDrive;
- explicar Encryption;
- explicar Auto-labeling;
- explicar propagación;
- realizar troubleshooting.

---

# 72. Qué dejamos opcional

## OPCIONAL

- protección PDF;
- Auto-labeling completo;
- Groups and Sites;
- Schematized data assets;
- compartir externamente;
- pruebas avanzadas de cifrado;
- SharePoint;
- pruebas adicionales con DLP.

---

# 73. Distribución sugerida del tiempo

| Actividad | Tiempo |
|---|---:|
| Introducción | 5 min |
| Purview / Information Protection | 5 min |
| Crear PII | 20 min |
| Content Marking | 10 min |
| Publicar etiqueta | 15 min |
| Explicar propagación | 5 min |
| Prueba Word | 15 min |
| Justificación | 10 min |
| Cierre DLP + Labels | 5 min |

**Total aproximado:** 90 minutos

---

# 74. Mapeo XtremeLabs -> Standalone

| XtremeLabs | Standalone |
|---|---|
| LON-CL1 | PC del alumno |
| MOD Administrator | Admin del tenant de práctica |
| Holly Dickson | LAB-User1 |
| Tenant Adatum | Tenant de práctica |
| Project - Falcon | LAB - Confidential |
| Usuarios precargados | Usuarios LAB |
| Cliente preparado | Microsoft 365 web |
| Credenciales del proveedor | Credenciales propias del laboratorio |

---

# 75. Relación con Microsoft 365 Copilot

Este es el punto donde debemos conectar el laboratorio con el curso.

Microsoft 365 Copilot trabaja dentro del contexto de acceso del usuario.

Antes de desplegar Copilot ampliamente, una organización debe comprender:

```text
¿Qué información existe?

¿Quién puede verla?

¿Cómo está clasificada?

¿Cómo está protegida?

¿Qué puede compartir el usuario?
```

---

# 76. Visión completa de los cuatro laboratorios

Ahora podemos unir todo:

```text
LAB 01
Tenant
   |
   v
Preparar entorno
   |
   v
LAB 02
Identity + Access + Roles
   |
   v
¿Quién puede entrar?
   |
   v
LAB 03
DLP
   |
   v
¿Qué puede compartir?
   |
   v
LAB 04
Sensitivity Labels
   |
   v
¿Qué información es y cómo se protege?
```

---

# 77. Modelo de seguridad resultante

```text
IDENTITY
   |
   v
ACCESS
   |
   v
PERMISSIONS
   |
   v
INFORMATION
   |
   +---- Classification
   |
   +---- Protection
   |
   +---- DLP
   |
   v
MICROSOFT 365 COPILOT
```

---

# 78. Mensaje de cierre para los alumnos

La preparación para Microsoft 365 Copilot no consiste únicamente en:

```text
Asignar una licencia de Copilot
```

Antes debemos revisar:

```text
Identidades
+
Acceso
+
Permisos
+
Datos
+
Clasificación
+
Protección
```

Copilot se incorpora sobre el entorno de Microsoft 365 que la organización ya tiene.

Por eso la preparación de seguridad y cumplimiento es una parte fundamental del despliegue.

---

# 79. Resultado final

Al completar los cuatro laboratorios Standalone, el alumno ha recorrido:

```text
Microsoft 365 Tenant
        |
        v
Microsoft Entra
        |
        v
Conditional Access
        |
        v
Roles & Permissions
        |
        v
Microsoft Purview
        |
        +---- DLP
        |
        +---- Sensitivity Labels
        |
        v
Microsoft 365 Copilot Readiness
```

---

# 80. Fin del laboratorio

Has completado:

**MS-4002 - Lab 04 - Sensitivity Labels**

y con ello los cuatro laboratorios principales de la modalidad:

**Standalone**