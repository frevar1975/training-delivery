# SC-200 · Investigar cambios administrativos de Azure en Sentinel

**Estado:** probado para ingesta y búsqueda en Defender. **Duración sugerida:** 5–8 minutos.

**Objetivo:** identificá una operación administrativa fallida y usá su identificador de correlación para reconstruir qué pasó.

## Problema → solución → demo

**Problema:** Un cambio de configuración de Azure falló. El SOC necesita averiguar qué operación se intentó, cuándo ocurrió y cuál fue el resultado.

**Solución:** Exportar la categoría Administrative del Registro de actividad de Azure al workspace y consultar la tabla AzureActivity con KQL.

**Analogía:** Es la bitácora de cambios de Azure. El identificador de correlación permite reunir el inicio y el resultado de un mismo intento.

## Preparación

- Suscripción del lab y workspace `law-sc200-hunting` en `rg-sc200-hunting`.
- Usar la configuración de diagnóstico existente `subscriptionToSc200Hunting`, con `Administrative` habilitada hacia ese workspace.
- Verificación desde PowerShell con Azure CLI y la suscripción del lab seleccionada:

```powershell
$subId = az account show --query id -o tsv
az monitor diagnostic-settings subscription list --subscription $subId -o json
```

## Investigá el cambio en Defender

1. Abrí Microsoft Defender → Búsqueda avanzada. Seleccioná `law-sc200-hunting`.
2. Ejecutá la consulta siguiente. Para evidencia histórica, seleccionar un rango que incluya el 19 de noviembre de 2026, alrededor de las 13:10 hora de Bolivia, y ajustar el filtro temporal de la consulta.
3. Expandí la fila `Failure` y compará su `CorrelationId` con el de la fila `Start`. Anotá la operación, la hora y el resultado.

```kusto
AzureActivity
| where TimeGenerated > ago(24h)
| where OperationNameValue =~ "Microsoft.Insights/diagnosticSettings/write"
| top 20 by TimeGenerated desc
| project TimeGenerated, OperationNameValue, ActivityStatusValue,
          ActivitySubstatusValue, _ResourceId, CorrelationId
```

**Evidencia observada:** dos filas de `MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE` en Búsqueda avanzada, con estados `Start` y `Failure`. La salida de CLI permitió verificar que el fallo fue `Conflict`: otro ajuste intentó utilizar el mismo destino para la misma categoría de la suscripción. El ajuste existente ya enviaba los eventos.

**Si aparecen cero filas:** comprobar el workspace y el rango. Quitar el filtro por operación para ver cualquier registro reciente. Si aún queda vacío, ejecutar la consulta en Registros de Log Analytics del mismo workspace. Para estas escrituras a nivel de suscripción, la evidencia observada tenía `ResourceGroup` vacío.

## Variante pendiente · Escritura de etiqueta

Azure registró una escritura de etiqueta exitosa en el grupo del lab. Su correlación en Sentinel quedó pendiente. Para repetir la prueba con la exportación activa:

```powershell
$rg = 'rg-sc200-hunting'
$rgId = az group show --subscription $subId --name $rg --query id -o tsv
if (-not $rgId) { throw 'No se encontró el grupo del lab.' }
$marca = (Get-Date).ToUniversalTime().ToString('yyyyMMdd-HHmmss')
az tag update --resource-id "$rgId" --operation Merge --tags "SC200Demo=$marca" -o table
az monitor activity-log list --subscription $subId --resource-group $rg --offset 1h --query "[?operationName.value=='Microsoft.Resources/tags/write'].{Hora:eventTimestamp,Estado:status.value,CorrelationId:correlationId}" -o table
```

En Defender, buscar `AzureActivity | where CorrelationId =~ "<ID del evento exitoso>"`. La variante queda probada cuando la escritura exitosa aparece con el mismo identificador en ambos lados.

**Comprobá tu resultado.** ¿Qué operación se intentó y qué campos permiten vincular el inicio con el fallo?
