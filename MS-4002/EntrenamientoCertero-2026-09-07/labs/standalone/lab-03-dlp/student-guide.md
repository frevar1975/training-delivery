# MS-4002 - Lab 03
## Implementar y probar Microsoft Purview Data Loss Prevention

**Modalidad:** Standalone  
**Entorno:** Tenant Microsoft 365 de práctica  
**Duración estimada:** 75-90 minutos

---

# 1. Objetivos

Al finalizar este laboratorio podrás:

- acceder al portal de Microsoft Purview;
- crear una política DLP personalizada;
- detectar contenido sensible basado en direcciones IP;
- crear una regla informativa para una única dirección IP;
- crear una regla de bloqueo para múltiples direcciones IP;
- configurar policy tips;
- permitir override con justificación;
- generar alertas administrativas;
- probar una política DLP utilizando Outlook on the web;
- validar el comportamiento desde una segunda identidad.

---

# 2. Escenario

La organización quiere reducir el riesgo de compartir información técnica sensible por correo electrónico.

Para este laboratorio utilizaremos direcciones IP como ejemplo de información sensible.

La política tendrá dos comportamientos:

```text
1 dirección IP
        |
        v
Mostrar Policy Tip
        |
        v
Permitir envío
```

y:

```text
2 o más direcciones IP
        |
        v
Mostrar Policy Tip
        |
        v
Bloquear envío
        |
        v
Permitir override con justificación
```

---

# 3. Entorno Standalone

No utilizaremos máquinas virtuales XtremeLabs.

Utilizaremos:

```text
PC del alumno
    |
    +-- Navegador principal
    |       |
    |       +-- Cuenta remitente
    |
    +-- Edge InPrivate / segundo perfil
            |
            +-- Cuenta destinataria
```

Como referencia utilizaremos:

```text
LAB-User1     = Remitente
LAB-User2     = Destinatario
```

Puedes utilizar otros usuarios de prueba si el instructor lo indica.

---

# 4. Requisitos

Antes de comenzar confirma:

- acceso al tenant de práctica;
- acceso a Microsoft Purview;
- permisos suficientes para administrar DLP;
- buzón disponible para LAB-User1;
- buzón disponible para LAB-User2;
- Outlook on the web accesible.

> IMPORTANTE
>
> No realices este laboratorio en un tenant de producción.

---

# 5. PARTE 1 - Abrir Microsoft Purview

## Task 1 - Acceder al portal

Abre el portal de Microsoft Purview utilizando la dirección indicada por el instructor.

Inicia sesión con la cuenta administrativa del tenant.

Ubica:

**Solutions**

Selecciona:

**Data Loss Prevention**

Luego:

**Policies**

---

# 6. Explorar las plantillas DLP

Selecciona:

**Create policy**

Revisa las categorías y plantillas disponibles.

Observa que Microsoft Purview ofrece políticas predefinidas para distintos escenarios.

Para este laboratorio utilizaremos una política personalizada.

Selecciona:

**Custom**

y luego:

**Custom policy**

Selecciona:

**Next**

---

# 7. PARTE 2 - Crear la política DLP

## Task 2 - Definir la política

Nombre:

```text
IP Address DLP Policy
```

Descripción:

```text
Detects IP addresses in Microsoft 365 content.
Users are notified when sensitive information is detected.
Content containing multiple IP addresses can be blocked.
```

Selecciona:

**Next**

---

# 8. Administrative units

Si aparece la opción para asignar Administrative Units, mantén la configuración predeterminada salvo indicación del instructor.

Selecciona:

**Next**

---

# 9. Seleccionar ubicaciones

Activa las ubicaciones indicadas por el instructor.

Para reproducir el escenario del laboratorio utilizaremos:

- Exchange email
- SharePoint sites
- OneDrive accounts
- Teams chats and channel messages

Desactiva otras ubicaciones si el instructor indica que el laboratorio debe limitarse a estas cargas de trabajo.

Selecciona:

**Next**

---

# 10. Definir configuración avanzada

Selecciona:

**Create or customize advanced DLP rules**

Selecciona:

**Next**

---

# 11. PARTE 3 - Regla para una dirección IP

## Task 3 - Crear la primera regla

Selecciona:

**Create rule**

Nombre:

```text
Single IP Address Rule
```

Descripción:

```text
Detects content containing an IP address
```

---

# 12. Configurar condición

En:

**Conditions**

selecciona:

**Add condition**

Luego:

**Content contains**

En:

**Sensitive info types**

busca:

```text
IP Address
```

Selecciona el tipo de información sensible:

**IP Address**

Agrega el tipo a la regla.

---

# 13. Instance count

Para esta primera regla mantén el número mínimo de instancias en:

```text
1
```

Esto significa que la regla puede activarse cuando se detecta al menos una dirección IP.

---

# 14. User notifications

Activa:

**Use notifications to inform your users and help educate them on the proper use of sensitive info**

Activa:

**Notify users in Microsoft 365 services with a policy tip**

Si está disponible, habilita la personalización del mensaje.

Utiliza un mensaje similar a:

```text
ATTENTION: This message contains an IP address.

Review whether the recipients are authorized to receive this information before sending the message.
```

---

# 15. Policy Tip

Si aparece la opción para mostrar el policy tip antes de enviar el correo, actívala para Exchange.

El objetivo es que el usuario reciba una advertencia antes de compartir contenido sensible.

---

# 16. Incident reports / Alerts

Activa la opción para generar una alerta administrativa cuando la regla encuentre una coincidencia, si está disponible en tu tenant.

Esto permitirá que los administradores tengan visibilidad de los eventos DLP.

---

# 17. Acción de la primera regla

No configures bloqueo para esta regla.

La lógica debe ser:

```text
Detectar IP
    |
    v
Notificar usuario
    |
    v
Generar alerta
    |
    v
Permitir envío
```

Guarda la regla.

---

# 18. PARTE 4 - Regla para múltiples direcciones IP

## Task 4 - Crear la segunda regla

Selecciona:

**Create rule**

Nombre:

```text
Multiple IP Address Rule
```

Descripción:

```text
Detects content containing two or more IP addresses
```

---

# 19. Agregar condición

Selecciona nuevamente:

**Content contains**

Agrega:

**Sensitive info types**

Busca:

```text
IP Address
```

Agrega:

**IP Address**

---

# 20. Cambiar Instance count

En la configuración del tipo:

**IP Address**

cambia el número mínimo de instancias a:

```text
2
```

La lógica ahora será:

```text
IP Address count >= 2
```

Esto permite diferenciar esta regla de la primera.

---

# 21. Configurar acción de bloqueo

En:

**Actions**

selecciona:

**Add an action**

Busca la opción relacionada con:

**Restrict access or encrypt the content in Microsoft 365 locations**

Configura el bloqueo según las opciones disponibles.

Para este laboratorio, selecciona la opción que bloquee el acceso o envío para todos los destinatarios afectados.

---

# 22. User notifications

Activa las notificaciones al usuario.

Activa:

**Policy Tip**

Utiliza un mensaje similar a:

```text
ATTENTION: This message contains multiple IP addresses.

The message is blocked because it may contain sensitive information.

Only override the block if you are authorized to share this information.
```

---

# 23. Configurar override

Busca la sección:

**User overrides**

Permite el override si la opción está disponible.

Configura:

```text
Require a business justification to override
```

y, si aparece:

```text
Allow override when the user reports a false positive
```

---

# 24. Qué significa override

El comportamiento esperado es:

```text
Contenido detectado
        |
        v
DLP bloquea
        |
        v
Usuario recibe Policy Tip
        |
        +---- Cancelar envío
        |
        +---- Override
                 |
                 v
          Justificación
                 |
                 v
              Enviar
```

---

# 25. Configurar alertas

Verifica que las alertas administrativas estén activadas para esta regla, si la opción está disponible.

Guarda la regla.

---

# 26. Revisar reglas

Debes tener:

```text
Single IP Address Rule
Multiple IP Address Rule
```

La primera regla:

```text
1 IP
-> Notify
-> Allow
```

La segunda:

```text
2+ IP
-> Notify
-> Block
-> Allow override
```

Selecciona:

**Next**

---

# 27. PARTE 5 - Modo de la política

Para un laboratorio Standalone es preferible iniciar la política en un modo controlado si el portal lo permite.

El instructor puede indicar uno de los siguientes modos:

```text
Test first
```

o:

```text
Turn it on immediately
```

Para un tenant dedicado exclusivamente a capacitación se puede activar inmediatamente.

En un tenant compartido, seguir las indicaciones del instructor.

---

# 28. Revisar y crear

Revisa:

- nombre;
- ubicaciones;
- reglas;
- acciones;
- notificaciones;
- overrides;
- alertas.

Selecciona:

**Submit**

Espera a que Microsoft Purview confirme la creación.

Selecciona:

**Done**

---

# 29. IMPORTANTE - Tiempo de propagación

Las políticas DLP no siempre se aplican inmediatamente.

Puede existir un retraso entre:

```text
Crear política
      |
      v
Distribuir configuración
      |
      v
Evaluar contenido
      |
      v
Mostrar Policy Tip
```

Si la prueba no funciona inmediatamente:

- espera;
- actualiza Outlook;
- vuelve a iniciar sesión;
- confirma que la política esté habilitada;
- confirma que los usuarios estén dentro del alcance.

No recrees la política inmediatamente.

---

# 30. PARTE 6 - Preparar la prueba

Utilizaremos dos cuentas.

## Sesión principal

```text
LAB-User1
```

será el remitente.

## Segunda sesión

Abre:

**Edge InPrivate**

o utiliza un segundo perfil del navegador.

Inicia sesión como:

```text
LAB-User2
```

Esta segunda sesión sustituye la VM secundaria utilizada en un laboratorio hospedado.

---

# 31. PARTE 7 - Probar la primera regla

## Task 5 - Abrir Outlook como remitente

En la sesión de:

**LAB-User1**

abre Outlook on the web.

Selecciona:

**New mail**

Destinatario:

```text
LAB-User2
```

Asunto:

```text
DLP Policy Test 1
```

Mensaje:

```text
Testing the following IP address: 192.168.0.1
```

---

# 32. Resultado esperado

La política debe detectar:

```text
192.168.0.1
```

y activar:

**Single IP Address Rule**

Debe aparecer un Policy Tip o advertencia.

La regla no debería bloquear el envío.

---

# 33. Enviar el mensaje

Después de revisar el Policy Tip, selecciona:

**Send**

Verifica:

**Sent Items**

Confirma que el mensaje fue enviado.

---

# 34. Revisar notificación

Revisa el Inbox del remitente.

Dependiendo de la configuración del tenant, puede aparecer una notificación relacionada con la coincidencia DLP.

---

# 35. Validar como destinatario

Cambia a la ventana:

**Edge InPrivate**

donde está conectado:

**LAB-User2**

Abre Outlook.

Verifica que llegó:

```text
DLP Policy Test 1
```

Abre el mensaje.

Confirma que contiene:

```text
192.168.0.1
```

---

# 36. Resultado de la primera prueba

El comportamiento esperado es:

```text
1 IP detectada
      |
      v
Policy Tip
      |
      v
Mensaje permitido
      |
      v
Destinatario recibe email
```

---

# 37. PARTE 8 - Probar la segunda regla

## Task 6 - Crear segundo mensaje

Regresa a la sesión de:

**LAB-User1**

Crea un nuevo correo.

Destinatario:

```text
LAB-User2
```

Asunto:

```text
DLP Policy Test 2
```

Mensaje:

```text
Testing the following IP addresses: 192.168.0.1 and 172.16.0.1
```

---

# 38. Resultado esperado

La política detectará dos direcciones IP:

```text
192.168.0.1
172.16.0.1
```

Debe activarse:

**Multiple IP Address Rule**

El mensaje debe mostrar un Policy Tip.

---

# 39. Probar el bloqueo

Intenta seleccionar:

**Send**

El comportamiento esperado es que Microsoft 365 bloquee el mensaje.

Verifica que el mensaje no aparezca en:

**Sent Items**

Puede permanecer en:

**Drafts**

---

# 40. Realizar override

Abre nuevamente el mensaje bloqueado.

En el Policy Tip selecciona la opción equivalente a:

**Show details**

Luego:

**Override**

Cuando solicite una justificación comercial, escribe un texto de laboratorio, por ejemplo:

```text
Authorized lab test for MS-4002 training.
```

No utilices información real de negocio.

---

# 41. Enviar nuevamente

Después del override:

selecciona:

**Send**

El mensaje debería poder enviarse si la política fue configurada para permitir override.

---

# 42. Validar como destinatario

En la sesión de:

**LAB-User2**

actualiza Outlook.

Verifica que llegó:

```text
DLP Policy Test 2
```

---

# 43. Resultado de la segunda prueba

El flujo esperado es:

```text
2 IP detectadas
       |
       v
Policy Tip
       |
       v
Bloqueo
       |
       v
Override
       |
       v
Justificación
       |
       v
Envío permitido
```

---

# 44. PARTE 9 - Revisar eventos DLP

Regresa al portal de Microsoft Purview.

Abre:

**Data Loss Prevention**

Revisa las áreas disponibles relacionadas con:

- alerts;
- incidents;
- activity;
- policy matches.

La disponibilidad exacta puede variar según el tenant.

Busca eventos relacionados con:

```text
IP Address DLP Policy
```

---

# 45. Qué observar

Intenta identificar:

```text
Policy
Rule
User
Workload
Action
Time
```

El objetivo es comprender que DLP no solamente actúa sobre contenido.

También produce información para investigación y monitoreo.

---

# 46. PARTE 10 - Send to Kindle

El laboratorio original de XtremeLabs incluye una configuración adicional en Microsoft Intune para deshabilitar:

```text
Send to Kindle
```

porque puede permitir que documentos salgan del entorno Microsoft 365 por un canal que no está cubierto de la misma forma por la política DLP. :contentReference[oaicite:4]{index=4}

En la versión Standalone esta tarea se considera:

```text
OPCIONAL / DEMO INSTRUCTOR
```

No es necesaria para completar el objetivo principal del laboratorio.

Si el instructor decide mostrarla, utilizar:

```text
Microsoft Intune
>
Apps
>
Policies for Office apps
```

Buscar:

```text
Turn off Send to Kindle
```

y revisar conceptualmente la configuración.

No crear una política global sin autorización del instructor.

---

# 47. Troubleshooting

## No aparece Policy Tip

Posibles causas:

- la política todavía no se propagó;
- el usuario no está dentro del alcance;
- Exchange no está habilitado en la política;
- el tipo de información sensible no coincide;
- Outlook todavía no recibió la nueva política.

Acciones:

1. Esperar algunos minutos.
2. Actualizar Outlook.
3. Revisar la política.
4. Confirmar las ubicaciones.
5. Confirmar las reglas.

---

## El correo no se bloquea

Revisa:

```text
Instance count = 2
```

en:

**Multiple IP Address Rule**

Confirma que la acción de bloqueo está configurada.

---

## El primer correo también se bloquea

Revisa el orden y las acciones de las reglas.

La primera regla no debería contener una acción de bloqueo.

---

## No aparece Override

Revisa la configuración:

**User overrides**

y confirma que esté permitido.

---

## El destinatario no recibe el correo después del override

Confirma:

- que el override fue aceptado;
- que existe una justificación;
- que el mensaje aparece en Sent Items;
- que LAB-User2 tiene buzón.

---

# 48. Limpieza

Pregunta al instructor antes de eliminar la política.

La política:

```text
IP Address DLP Policy
```

puede conservarse para demostraciones posteriores.

Si no se utilizará nuevamente, el instructor puede:

- dejarla en modo de prueba;
- deshabilitarla;
- eliminarla al finalizar la capacitación.

---

# 49. Validación final

Confirma:

- [ ] Accedí a Microsoft Purview.
- [ ] Creé IP Address DLP Policy.
- [ ] Creé Single IP Address Rule.
- [ ] Configuré IP Address como Sensitive Info Type.
- [ ] Configuré Policy Tips.
- [ ] Creé Multiple IP Address Rule.
- [ ] Configuré Instance count = 2.
- [ ] Configuré bloqueo.
- [ ] Configuré override con justificación.
- [ ] Probé un mensaje con una IP.
- [ ] El mensaje con una IP pudo enviarse.
- [ ] Probé un mensaje con dos IP.
- [ ] El segundo mensaje fue bloqueado.
- [ ] Realicé override.
- [ ] El destinatario recibió el mensaje después del override.
- [ ] Revisé los eventos relacionados con DLP.

---

# 50. Resultado final

Has implementado una política DLP que diferencia entre distintos niveles de riesgo.

```text
Contenido
    |
    v
Sensitive Info Type
    |
    v
Regla DLP
    |
    +---- Bajo riesgo
    |        |
    |        v
    |     Notify
    |        |
    |        v
    |      Allow
    |
    +---- Mayor riesgo
             |
             v
           Block
             |
             v
          Override
             |
             v
        Justification
```

---

# 51. Conexión con el siguiente laboratorio

En este laboratorio protegimos información mediante:

**Data Loss Prevention**

El siguiente laboratorio trabajará con:

**Sensitivity Labels**

El enfoque cambia de:

```text
Detectar y controlar el uso de información
```

a:

```text
Clasificar y proteger la información
```