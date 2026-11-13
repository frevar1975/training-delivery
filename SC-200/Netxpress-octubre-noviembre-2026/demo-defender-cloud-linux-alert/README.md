# Runbook por fases: Syslog primero, alerta de endpoint después

## Propósito de la demostración

La sesión tiene dos momentos separados. **Fase A** muestra recopilación Syslog con Defender for Servers desactivado. **Fase B** habilita Defender for Servers, espera el sensor Linux y prueba una detección. No confundir un evento Syslog o una alerta de ejemplo con una detección real de la VM.

## Fase A — Estado inicial, sin activar Servers

Antes de modificar planes:

1. En Defender for Cloud → **Environment settings → suscripción → Defender plans**, confirma que **Servers** esté **Off**. Registra el precio y la cantidad de recursos que el portal muestra para tomar una decisión antes de activarlo.
2. Confirma que AMA esté instalado y que una DCR Syslog esté asociada a la VM de laboratorio.
3. Desde Run Command o una sesión autorizada, manda un evento inocuo:
   ```bash
   logger -p local4.warning -t SC200-LINUX-DEMO 'Prueba de Syslog fase A'
   ```
4. En el workspace de Sentinel, demuestra que el mensaje llegó:
   ```kusto
   Syslog
   | where TimeGenerated > ago(1h)
   | where ProcessName == "SC200-LINUX-DEMO"
   | project TimeGenerated, Computer, Facility, SeverityLevel, SyslogMessage
   | order by TimeGenerated desc
   ```
5. Muestra que la recopilación funciona, pero aún no hay sensor MDE:
   ```powershell
   az vm extension list --resource-group "<grupo>" --vm-name "<vm>" --query "[].{Nombre:name,Estado:provisioningState}" -o table
   ```
   Si `mdatp` responde `command not found`, es coherente con esta fase. No descargues EICAR.

## Fase B — Activar e incorporar el sensor

1. Vuelve a **Environment settings → suscripción → Defender plans**. Revisa el precio, la prueba disponible y cuántos servidores cubrirá el ámbito. Habilita **Servers** únicamente si aceptas esas condiciones.
2. En **Settings and monitoring**, confirma **Endpoint protection: On**; pulsa **Continue** y después **Save**.
3. Mantén la VM encendida y espera a que se incorpore el sensor. Microsoft indica que normalmente puede tomar hasta una hora y, en la primera integración Linux de la suscripción, hasta 12 horas.
4. Repite la consulta de extensiones y espera a ver `MDE.Linux` con estado `Succeeded`.
5. Verifica protección en tiempo real:
   ```powershell
   az vm run-command invoke --resource-group "<grupo>" --name "<vm>" --command-id RunShellScript --scripts "sudo mdatp health --field real_time_protection_enabled" --query "value[0].message" -o tsv
   ```
   Sigue solo si el resultado es `true`. Si aparece `mdatp: command not found`, espera y revisa el estado detallado de la extensión y los requisitos de despliegue.

## Fase C — Prueba de detección

1. En la VM desechable, descarga EICAR:
   ```bash
   curl -O https://secure.eicar.org/eicar.com.txt
   ```
   EICAR es un archivo inocuo de prueba antimalware; no lo uses en producción.
2. En Defender for Cloud → **Security alerts**, busca la alerta y valida que la VM figure como recurso afectado.
3. En Sentinel → **Logs**, ejecuta:
   ```kusto
   SecurityAlert
   | where TimeGenerated > ago(1d)
   | where ProductName == "Azure Security Center"
   | where CompromisedEntity contains "<nombre-de-tu-VM>"
       or tostring(Entities) contains "<nombre-de-tu-VM>"
   | project TimeGenerated, AlertName, AlertSeverity, ProductName, CompromisedEntity
   | order by TimeGenerated desc
   ```
4. Si no llega a Sentinel, verifica conector, workspace y permisos. Una alerta que aparece en Defender for Cloud y una alerta que llega a Sentinel son dos comprobaciones separadas.

## Fase D — Cierre

1. Si Servers no se necesita de forma continua, deshabilítalo en el ámbito configurado y guarda.
2. Confirma que no quede el plan activo a nivel de recurso; revisa los medidores de Defender for Servers en Cost Management.
3. No elimines el workspace compartido. Detén o elimina la VM solo si no se reutiliza en otras prácticas.

## Qué explicar

“Primero validamos la tubería de Syslog: AMA y DCR entregan registros a Sentinel, sin generar una detección de endpoint. Después activamos Defender for Servers, incorporamos el sensor MDE de Linux y comprobamos su salud. EICAR valida la detección; Defender for Cloud muestra la alerta del servidor y Sentinel puede centralizarla si el conector funciona. Revisamos precio y cobertura antes de activar.”

## Referencias

- [Integración MDE y tiempos de incorporación](https://learn.microsoft.com/azure/defender-for-cloud/enable-defender-for-endpoint)
- [Validación de alertas](https://learn.microsoft.com/azure/defender-for-cloud/alert-validation)
- [Deshabilitar planes y revisar cargos](https://learn.microsoft.com/azure/defender-for-cloud/disable-plans)
