# Runbook: demostración de alerta de Defender for Cloud en Linux

## Resultado esperado

Una alerta de detección de prueba asociada a la VM Linux aparece en Microsoft Defender for Cloud. Si el conector correspondiente está activo y apunta al workspace correcto, también se puede consultar en Microsoft Sentinel.

## Verificaciones previas

- Usa una VM de laboratorio dedicada, nunca una máquina de producción.
- Confirma que Defender for Servers está habilitado y que revisaste el precio vigente y el ámbito de cobertura de la suscripción.
- Comprueba que Defender for Endpoint esté instalado en Linux y que la protección en tiempo real esté activa.
- Si el destino es Sentinel, confirma el workspace y el estado conectado del conector de Microsoft Defender for Cloud.
- AMA y la DCR de Syslog ayudan a recopilar registros, pero no reemplazan al sensor de Defender for Endpoint para esta detección.

## Ejecución

1. Habilita **Servers** desde **Defender for Cloud → Environment settings → suscripción → Defender plans**, solo tras aceptar el costo que muestra tu portal.
2. Abre **Monitoring coverage → Settings**. En **Endpoint protections**, usa **Fix** y habilita el componente faltante bajo **Linux machines**.
3. Espera el aprovisionamiento. Confirma en las extensiones de la VM que `MDE.Linux` tenga estado `Succeeded`.
4. En la VM, ejecuta:
   ```bash
   sudo mdatp health --field real_time_protection_enabled
   ```
   Continúa solo si devuelve `true`.
5. Para una detección inocua, descarga EICAR únicamente en la VM desechable:
   ```bash
   curl -O https://secure.eicar.org/eicar.com.txt
   ```
6. Espera unos minutos. En **Defender for Cloud → Security alerts**, filtra por el recurso de prueba y confirma que la alerta corresponda a esa VM.
7. En Sentinel, abre **Logs** y consulta:
   ```kusto
   SecurityAlert
   | where TimeGenerated > ago(1d)
   | where ProductName == "Azure Security Center"
   | where CompromisedEntity contains "<nombre-de-tu-VM>"
       or tostring(Entities) contains "<nombre-de-tu-VM>"
   | project TimeGenerated, AlertName, AlertSeverity, ProductName, CompromisedEntity
   | order by TimeGenerated desc
   ```
8. Si no aparece en Sentinel, revisa el estado del conector, el workspace y los permisos de la suscripción. La presencia de alertas de ejemplo `Sample-VM` no confirma que la VM real esté generando alertas ni que la conexión en vivo funcione.
9. Al acabar, apaga el plan si no necesitas protección continua. Verifica la cobertura restante y revisa los costos de Azure.

## Registro de evidencias

- Captura del precio y alcance antes de habilitar Servers.
- Estado de la extensión y protección en tiempo real.
- Alerta de Defender for Cloud con la VM de laboratorio como recurso afectado.
- Resultado de la consulta en Sentinel y estado del conector.

## Referencias

- [Validación de alertas](https://learn.microsoft.com/azure/defender-for-cloud/alert-validation)
- [Integración de Defender for Endpoint](https://learn.microsoft.com/azure/defender-for-cloud/enable-defender-for-endpoint)
- [Habilitar Defender for Servers](https://learn.microsoft.com/azure/defender-for-cloud/tutorial-enable-servers-plan)
