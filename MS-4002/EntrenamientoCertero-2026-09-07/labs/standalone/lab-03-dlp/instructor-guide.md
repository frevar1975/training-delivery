# MS-4002 - Lab 03
## Guía del instructor - Microsoft Purview Data Loss Prevention

**Modalidad:** Standalone  
**Curso:** MS-4002 - Prepare security and compliance to support Microsoft 365 Copilot  
**Duración sugerida:** 75-90 minutos

---

# 1. Propósito del laboratorio

Este laboratorio adapta la práctica de Data Loss Prevention de XtremeLabs a un entorno sin laboratorio hospedado.

El alumno trabajará con:

- su propia PC;
- navegador principal;
- Edge InPrivate o segundo perfil;
- dos usuarios de prueba;
- Microsoft Purview;
- Outlook on the web;
- un tenant Microsoft 365 de práctica.

No se requiere:

- LON-CL1;
- LON-CL2;
- usuarios precargados por XtremeLabs;
- credenciales del proveedor.

---

# 2. Objetivos didácticos

Al finalizar el laboratorio el alumno debería comprender:

- qué es Data Loss Prevention;
- cómo se crea una política DLP personalizada;
- cómo se utilizan Sensitive Info Types;
- cómo funciona Instance Count;
- cómo se muestran Policy Tips;
- cómo se bloquea contenido;
- cómo funciona Override;
- cómo se solicita una justificación;
- cómo se generan alertas;
- cómo se prueba una política DLP desde Outlook;
- cómo se revisan eventos de DLP.

---

# 3. Clasificación de actividades

Usaremos tres tipos:

## ALUMNO

El alumno ejecuta la tarea.

## DEMO INSTRUCTOR

El instructor demuestra la configuración.

## OPCIONAL

Actividad que puede omitirse si no hay tiempo, permisos o licencias suficientes.

---

# 4. Preparación previa del instructor

Antes de la clase valida:

- acceso al tenant de práctica;
- acceso a Microsoft Purview;
- permisos para administrar DLP;
- Exchange Online disponible;
- buzón para LAB-User1;
- buzón para LAB-User2;
- Outlook on the web funcional.

Usuarios sugeridos:

- LAB-User1
- LAB-User2

LAB-User1 será el remitente.

LAB-User2 será el destinatario.

---

# 5. Seguridad del laboratorio

> IMPORTANTE
>
> No realizar este ejercicio en un tenant de producción.
>
> No reutilizar direcciones IP reales internas de una organización.
>
> Utilizar exclusivamente valores de laboratorio.
>
> No crear políticas globales sin comprender su impacto.

---

# 6. PARTE 1 - Introducción a DLP

## Tipo

**DEMO INSTRUCTOR**

## Tiempo sugerido

5 minutos

Explicar que DLP busca reducir la exposición accidental o no autorizada de información.

---

# 7. Analogía

"Un detector de seguridad en un aeropuerto revisa qué intenta sacar una persona del área controlada."

En DLP:

```text
Usuario
   |
   v
Contenido
   |
   v
DLP
   |
   +---- Permitir
   |
   +---- Advertir
   |
   +---- Bloquear
```

---

# 8. Diferencia importante

DLP no significa solamente:

```text
Bloquear
```

También puede:

- detectar;
- advertir;
- educar;
- registrar;
- alertar;
- bloquear;
- permitir override.

---

# 9. PARTE 2 - Abrir Microsoft Purview

## Tipo

**ALUMNO**

## Tiempo sugerido

5 minutos

Mostrar:

**Microsoft Purview > Solutions > Data Loss Prevention > Policies**

Explicar que Purview centraliza capacidades relacionadas con:

- protección de información;
- cumplimiento;
- riesgo;
- Data Loss Prevention.

---

# 10. PARTE 3 - Crear política DLP

## Tipo

**ALUMNO**

## Tiempo sugerido

10 minutos

Crear:

**IP Address DLP Policy**

Tipo:

**Custom policy**

Descripción sugerida:

```text
Detects IP addresses in Microsoft 365 content.
Users are notified when sensitive information is detected.
Content containing multiple IP addresses can be blocked.
```

---

# 11. Ubicaciones

Configurar según disponibilidad:

- Exchange email
- SharePoint sites
- OneDrive accounts
- Teams chats and channel messages

---

## Explicación

Una misma política puede aplicarse sobre múltiples cargas de trabajo.

```text
DLP Policy
    |
    +---- Exchange
    |
    +---- SharePoint
    |
    +---- OneDrive
    |
    +---- Teams
```

---

# 12. PARTE 4 - Sensitive Info Types

## Tipo

**DEMO INSTRUCTOR + ALUMNO**

Explicar que una regla necesita saber qué contenido debe identificar.

Para el laboratorio utilizaremos:

**IP Address**

---

# 13. Analogía

"El Sensitive Info Type es el patrón que el detector está buscando."

Ejemplos conceptuales:

```text
Credit Card
Social Security Number
Passport
IP Address
```

Para este ejercicio:

```text
IP Address
```

---

# 14. PARTE 5 - Primera regla

## Tipo

**ALUMNO**

## Tiempo sugerido

10 minutos

Crear:

**Single IP Address Rule**

Condición:

```text
Sensitive Info Type = IP Address
Instance count >= 1
```

---

# 15. Acción de la primera regla

Configurar:

- Policy Tip;
- User notification;
- alerta administrativa si está disponible.

No configurar bloqueo.

---

## Resultado conceptual

```text
1 IP
 |
 v
Detect
 |
 v
Notify
 |
 v
Allow
```

---

# 16. Qué explicar

La primera regla tiene un enfoque educativo.

No impide la acción.

Informa al usuario para que revise si realmente debería compartir esa información.

---

# 17. PARTE 6 - Segunda regla

## Tipo

**ALUMNO**

## Tiempo sugerido

15 minutos

Crear:

**Multiple IP Address Rule**

Condición:

```text
Sensitive Info Type = IP Address
Instance count >= 2
```

---

# 18. Acción

Configurar:

- Policy Tip;
- bloqueo;
- override;
- justificación;
- alerta administrativa.

---

# 19. Resultado conceptual

```text
2+ IP
  |
  v
Detect
  |
  v
Notify
  |
  v
Block
  |
  v
Override?
  |
  +---- NO --> Cancelar
  |
  +---- SI
         |
         v
    Justificación
         |
         v
       Allow
```

---

# 20. Qué explicar sobre Instance Count

Instance Count permite utilizar el mismo Sensitive Info Type de manera distinta dependiendo de cuántas coincidencias existen.

Ejemplo:

```text
1 coincidencia  = advertencia
2+ coincidencias = bloqueo
```

Esto permite utilizar DLP de manera proporcional al riesgo.

---

# 21. Qué explicar sobre Override

Override no significa que DLP haya fallado.

Es una decisión controlada.

Puede permitir:

```text
Usuario
   |
   v
DLP bloquea
   |
   v
Usuario justifica
   |
   v
Evento registrado
   |
   v
Acción permitida
```

---

# 22. Analogía

"Un empleado necesita sacar un documento de un área segura."

El sistema puede detenerlo.

Si tiene autorización, debe explicar por qué.

La acción queda registrada.

---

# 23. PARTE 7 - Policy Tips

## Tipo

**ALUMNO**

Explicar que el Policy Tip proporciona retroalimentación en el momento en que el usuario intenta realizar una acción.

No es solamente una alerta administrativa posterior.

---

# 24. Mensaje sugerido para una IP

```text
ATTENTION: This message contains an IP address.

Review whether the recipients are authorized to receive this information before sending the message.
```

---

# 25. Mensaje sugerido para múltiples IP

```text
ATTENTION: This message contains multiple IP addresses.

The message is blocked because it may contain sensitive information.

Only override the block if you are authorized to share this information.
```

---

# 26. PARTE 8 - Modo de la política

## Tipo

**DEMO INSTRUCTOR**

Si el tenant permite:

preferir inicialmente un modo de prueba.

Si es un tenant exclusivamente de capacitación:

puede activarse la política para realizar la demostración.

---

# 27. Propagación

Explicar antes de realizar la prueba:

```text
Crear política
      |
      v
Distribución
      |
      v
Servicio recibe configuración
      |
      v
Contenido evaluado
```

Esto no siempre es inmediato.

---

# 28. Regla de clase

Si la política no funciona inmediatamente:

**NO recrearla.**

Primero revisar:

- estado;
- ubicación;
- alcance;
- reglas;
- propagación.

---

# 29. PARTE 9 - Primera prueba

## Tipo

**ALUMNO**

## Tiempo sugerido

10 minutos

Sesión principal:

**LAB-User1**

Abrir Outlook on the web.

Crear mensaje para:

**LAB-User2**

Asunto:

```text
DLP Policy Test 1
```

Contenido:

```text
Testing the following IP address: 192.168.0.1
```

---

# 30. Resultado esperado

```text
192.168.0.1
      |
      v
IP Address detected
      |
      v
Single IP Address Rule
      |
      v
Policy Tip
      |
      v
Send allowed
```

---

# 31. Qué mostrar

El instructor debe llamar la atención sobre:

- Policy Tip;
- nombre de la política si aparece;
- posibilidad de enviar;
- diferencia entre advertencia y bloqueo.

---

# 32. Segunda sesión

## Tipo

**ALUMNO**

Abrir:

**Edge InPrivate**

Iniciar sesión como:

**LAB-User2**

Abrir Outlook on the web.

---

## Explicación

Esto reemplaza el uso de:

**LON-CL2**

en el laboratorio hospedado.

---

# 33. Validar recepción

Confirmar que LAB-User2 recibe:

```text
DLP Policy Test 1
```

---

# 34. PARTE 10 - Segunda prueba

## Tipo

**ALUMNO**

Regresar a:

**LAB-User1**

Crear correo:

Asunto:

```text
DLP Policy Test 2
```

Contenido:

```text
Testing the following IP addresses: 192.168.0.1 and 172.16.0.1
```

---

# 35. Resultado esperado

```text
2 IP addresses
      |
      v
Multiple IP Address Rule
      |
      v
Policy Tip
      |
      v
Block
```

---

# 36. Validar bloqueo

Intentar enviar.

El mensaje debería quedar bloqueado según la configuración de la regla.

Mostrar que no aparece en:

**Sent Items**

---

# 37. PARTE 11 - Override

## Tipo

**ALUMNO**

Seleccionar la opción de override disponible en el Policy Tip.

Ingresar una justificación de laboratorio.

Ejemplo:

```text
Authorized lab test for MS-4002 training.
```

---

# 38. Qué explicar

La justificación:

- no elimina la política;
- no desactiva DLP;
- no cambia permanentemente la regla.

Solo documenta por qué el usuario necesita continuar con esa operación concreta.

---

# 39. Enviar después del override

Enviar nuevamente el mensaje.

Verificar:

**Sent Items**

---

# 40. Validar destinatario

En Edge InPrivate como:

**LAB-User2**

actualizar Outlook.

Confirmar recepción de:

```text
DLP Policy Test 2
```

---

# 41. Comparación de pruebas

Mostrar:

| Prueba | Contenido | Acción |
|---|---|---|
| Test 1 | 1 IP | Notify + Allow |
| Test 2 | 2 IP | Block + Override |

---

# 42. Qué debe comprender el alumno

La política no actúa de manera binaria.

Puede responder de manera diferente según:

- contenido;
- cantidad;
- contexto;
- usuario;
- ubicación;
- acción.

---

# 43. PARTE 12 - Alertas y monitoreo

## Tipo

**DEMO INSTRUCTOR + ALUMNO**

## Tiempo sugerido

10 minutos

Regresar a Microsoft Purview.

Revisar las áreas relacionadas con:

- alerts;
- incidents;
- activity;
- policy matches.

---

# 44. Qué buscar

Intentar identificar:

```text
Policy
Rule
User
Workload
Action
Time
```

---

# 45. Explicación

DLP tiene dos caras:

```text
Experiencia del usuario
        +
Monitoreo administrativo
```

El usuario recibe Policy Tips.

El administrador recibe visibilidad sobre eventos.

---

# 46. PARTE 13 - Send to Kindle

## Tipo

**OPCIONAL / DEMO INSTRUCTOR**

El laboratorio de XtremeLabs incluye una tarea adicional para deshabilitar:

**Send to Kindle**

mediante una política para aplicaciones de Office.

En nuestra versión Standalone no es requisito para completar el laboratorio principal.

---

# 47. Qué explicar

La idea detrás de esa tarea es mostrar que existen canales que pueden permitir que la información salga del entorno protegido.

Por eso DLP debe formar parte de una estrategia de protección más amplia.

---

# 48. Si se demuestra Send to Kindle

Mostrar conceptualmente:

```text
Microsoft Intune
    |
    v
Apps
    |
    v
Policies for Office apps
    |
    v
Turn off Send to Kindle
```

No aplicar una política global sin validar previamente el impacto.

---

# 49. Troubleshooting - Policy Tip no aparece

Posibles causas:

- propagación;
- usuario fuera del alcance;
- ubicación incorrecta;
- regla incorrecta;
- Sensitive Info Type incorrecto;
- Outlook todavía no recibió la configuración.

---

# 50. Orden de troubleshooting

Revisar:

```text
1. Policy enabled?
2. Workload included?
3. User included?
4. Rule enabled?
5. Sensitive Info Type correct?
6. Instance count correct?
7. Propagation completed?
```

---

# 51. El mensaje con dos IP no se bloquea

Revisar:

```text
Multiple IP Address Rule
```

Confirmar:

```text
Instance count >= 2
```

y acción:

```text
Block
```

---

# 52. El mensaje con una IP también se bloquea

Revisar la acción de:

**Single IP Address Rule**

Debe:

```text
Notify
```

pero no:

```text
Block
```

---

# 53. Override no aparece

Revisar:

**User overrides**

Confirmar que el usuario tenga permitido realizar override.

---

# 54. La política aún no funciona

No detener toda la clase.

Plan B:

**DEMO INSTRUCTOR**

Mostrar:

- configuración;
- reglas;
- Policy Tips esperados;
- flujo conceptual.

Continuar con el curso.

---

# 55. Limpieza

Al terminar, el instructor decide si:

- conserva la política;
- la deja en modo de prueba;
- la deshabilita;
- la elimina.

No es necesario eliminarla inmediatamente si se utilizará nuevamente.

---

# 56. Qué ejecuta el alumno

## ALUMNO

- acceder a Purview;
- crear política;
- crear Single IP Address Rule;
- crear Multiple IP Address Rule;
- configurar Policy Tips;
- configurar bloqueo;
- configurar override;
- probar una IP;
- probar dos IP;
- realizar override;
- validar recepción.

---

# 57. Qué hace el instructor

## DEMO INSTRUCTOR

- explicar DLP;
- explicar Sensitive Info Types;
- explicar Instance Count;
- explicar propagación;
- revisar alertas;
- troubleshooting;
- decidir modo de la política.

---

# 58. Qué dejamos opcional

## OPCIONAL

- Send to Kindle;
- configuración de Intune;
- investigación avanzada de alertas;
- ajustes adicionales de política;
- pruebas sobre SharePoint;
- pruebas sobre OneDrive;
- pruebas sobre Teams.

---

# 59. Distribución sugerida del tiempo

| Actividad | Tiempo |
|---|---:|
| Introducción DLP | 5 min |
| Crear política | 10 min |
| Regla 1 | 10 min |
| Regla 2 | 15 min |
| Policy Tips / Override | 10 min |
| Propagación / revisión | 5 min |
| Test 1 | 10 min |
| Test 2 + Override | 15 min |
| Alertas | 10 min |

**Total aproximado:** 90 minutos

Si hay retrasos de propagación:

continuar con explicación y volver posteriormente a las pruebas.

---

# 60. Mapeo XtremeLabs -> Standalone

| XtremeLabs | Standalone |
|---|---|
| LON-CL1 | Navegador principal |
| Holly Dickson | LAB-User1 |
| LON-CL2 | Edge InPrivate / segundo perfil |
| Lynne Robbins | LAB-User2 |
| Tenant preparado | Tenant Microsoft 365 de práctica |
| Usuarios precargados | Usuarios LAB |
| Credenciales del proveedor | Credenciales de laboratorio propias |

---

# 61. Resultado final

El alumno debería comprender:

```text
Datos
  |
  v
Sensitive Info Type
  |
  v
DLP Rule
  |
  +---- Notify
  |
  +---- Block
  |
  +---- Override
  |
  +---- Alert
```

---

# 62. Conexión con Microsoft 365 Copilot

Antes de habilitar ampliamente Microsoft 365 Copilot, la organización debe comprender cómo se protege la información existente.

Copilot utiliza información a la que el usuario ya tiene acceso.

DLP forma parte del conjunto de controles que ayuda a gobernar cómo se utiliza y comparte esa información.

---

# 63. Conexión con el siguiente laboratorio

El siguiente laboratorio será:

**Lab 04 - Sensitivity Labels**

En DLP preguntamos:

```text
¿Qué está intentando hacer el usuario con la información?
```

Con Sensitivity Labels empezamos a responder:

```text
¿Qué tipo de información es y cómo debe protegerse?
```