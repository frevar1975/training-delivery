# SC-200 | Demo ejecutada: Azure Activity y análisis KQL (12-nov-2026)

**Curso:** SC-200 · **Centro:** Netxpress · **Período:** octubre–noviembre 2026.  
**Ejecución:** 12 de noviembre de 2026 · **Terminal:** Windows PowerShell 5.1.  
**Plantilla independiente del entorno:** [training-templates/SC-200/demo-azure-activity-sentinel](https://github.com/frevar1975/training-templates/tree/main/SC-200/demo-azure-activity-sentinel).

## Objetivo y resultado

Se demostró en un entorno real el flujo **Azure Activity -> diagnóstico de suscripción -> Log Analytics -> Microsoft Sentinel / KQL**. Los eventos se consultaron y se identificó quién ejecutó una operación, cuándo, qué operación y sobre qué grupo. **No se creó regla analítica, alerta ni incidente**.

## Entorno utilizado (identificadores no secretos, específicos de esta práctica)

| Parámetro | Valor |
| --- | --- |
| Suscripción | Visual Studio Enterprise |
| Subscription ID | `430c139d-1e7d-4f38-81cb-a03710c5a3d3` |
| Resource group del workspace | `rg-sc200` |
| Workspace | `law-sc200-repo-demo` |
| Workspace customerId | `34d5aab6-a337-4aab-a4f9-768c95005ef9` |
| Diagnostic setting | `diag-azureactivity-sc200` |
| Grupo de prueba | `rg-sc200-test-activity` |
| Región configurada para recursos | `eastus` |

## Reproducción desde cero (asumiendo az login hecho)

**Copiar en Windows PowerShell 5.1, no en Bash.** Estas instrucciones parten de que el workspace ya existe y está habilitado para Sentinel. Para preparar un workspace nuevo y su incorporación, ver la [demo previa de despliegue con GitHub](../demo-github-sentinel/README.md) y adaptar los pasos a PowerShell.

### 1. Seleccionar y validar suscripción

```powershell
az account set --subscription "430c139d-1e7d-4f38-81cb-a03710c5a3d3"
az account show --query "{Nombre:name,Id:id,Estado:state}" -o json
```

**Observado:** `Enabled`, nombre `Suscripción de Visual Studio Enterprise`.

### 2. Revisar diagnósticos existentes

```powershell
az monitor diagnostic-settings subscription list --subscription "430c139d-1e7d-4f38-81cb-a03710c5a3d3" -o json
```

**Antes:** `{"value":[]}`. En una repetición de esta demo ya debería existir `diag-azureactivity-sc200`: **no crearlo de nuevo ni enviar duplicados**.

### 3. Obtener el workspace ARM ID

```powershell
$workspaceId = az monitor log-analytics workspace show --resource-group "rg-sc200" --workspace-name "law-sc200-repo-demo" --query id -o tsv
Write-Host $workspaceId
```

**Observado:**

```text
/subscriptions/430c139d-1e7d-4f38-81cb-a03710c5a3d3/resourceGroups/rg-sc200/providers/Microsoft.OperationalInsights/workspaces/law-sc200-repo-demo
```

### 4. Crear la configuración (solo la primera vez)

```powershell
$logs = @(
    @{ category = "Administrative"; enabled = $true }
    @{ category = "Security"; enabled = $true }
    @{ category = "ServiceHealth"; enabled = $true }
    @{ category = "Alert"; enabled = $true }
    @{ category = "Recommendation"; enabled = $true }
    @{ category = "Policy"; enabled = $true }
    @{ category = "Autoscale"; enabled = $true }
    @{ category = "ResourceHealth"; enabled = $true }
) | ConvertTo-Json -Depth 5 -Compress
$logs | Set-Content -Path "$env:TEMP\sentinel-activity-logs.json" -Encoding UTF8

az monitor diagnostic-settings subscription create --name "diag-azureactivity-sc200" --location "eastus" --workspace $workspaceId --logs "@$env:TEMP\sentinel-activity-logs.json" -o json
az monitor diagnostic-settings subscription show --name "diag-azureactivity-sc200" -o json
```

**Observado:** se creó `diag-azureactivity-sc200`, ocho categorías `enabled: true`, el workspaceId correcto, y Azure devolvió `location: global`. El comando anterior es para **reconstruir** la práctica, no para ejecutarlo de nuevo en el estado actual.

### 5. Generar actividad

```powershell
az group create --name "rg-sc200-test-activity" --location eastus
az group show --name "rg-sc200-test-activity" --query "{Nombre:name,Estado:properties.provisioningState}" -o json
```

**Observado:** `{"Estado":"Succeeded","Nombre":"rg-sc200-test-activity"}`. Para una nueva clase usar otro nombre de grupo si el anterior sigue existiendo.

### 6. Ver el Activity Log original

```powershell
az monitor activity-log list --offset 2h --max-events 30 --query "[].{Fecha:eventTimestamp,Operacion:operationName.value,Estado:status.value,Grupo:resourceGroupName}" -o table
```

**Observado:** evento `resourcegroups/write` con `Started` y `Succeeded`. Una consulta anterior agregando `--resource-group` devolvió tabla vacía; la consulta general sí devolvió eventos.

### 7. Confirmar ingestión directa con Log Analytics CLI

```powershell
$workspaceGuid = az monitor log-analytics workspace show --resource-group "rg-sc200" --workspace-name "law-sc200-repo-demo" --query customerId -o tsv
Write-Host $workspaceGuid
az monitor log-analytics query --workspace $workspaceGuid --analytics-query "AzureActivity | where TimeGenerated > ago(4h) | summarize TotalEventos=count(), UltimoEvento=max(TimeGenerated)" -o json
az monitor log-analytics query --workspace $workspaceGuid --analytics-query "AzureActivity | where TimeGenerated > ago(4h) | project TimeGenerated, OperationNameValue, ActivityStatusValue, ResourceGroup, Caller | order by TimeGenerated desc" -o table
```

**Observado:** `TotalEventos=4`; `UltimoEvento=2026-11-12T21:59:53.0320381Z`. Los cuatro registros:

| UTC 12-nov-2026 | Operación | Estado KQL |
| --- | --- | --- |
| 21:56:29.459 | `MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE` | Start |
| 21:56:35.193 | `MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE` | Success |
| 21:59:49.047 | `MICROSOFT.RESOURCES/SUBSCRIPTIONS/RESOURCEGROUPS/WRITE` | Start |
| 21:59:53.032 | `MICROSOFT.RESOURCES/SUBSCRIPTIONS/RESOURCEGROUPS/WRITE` | Success |

Identidad observada en los cuatro: `frevarmct@hotmail.com`. Horario Bolivia = UTC-4 (17:56 y 17:59).

### 8. KQL en Microsoft Defender (Búsqueda avanzada)

Entrar a `https://security.microsoft.com`, seleccionar **área de trabajo `law-sc200-repo-demo`** y pegar en el editor **únicamente**:

```kusto
AzureActivity
| where TimeGenerated > ago(4h)
| where OperationNameValue in~ (
    "Microsoft.Resources/subscriptions/resourcegroups/write",
    "Microsoft.Resources/subscriptions/resourcegroups/delete"
)
| where ActivityStatusValue =~ "Success"
| project TimeGenerated, Caller, OperationNameValue, ResourceGroup, ActivityStatusValue
| order by TimeGenerated desc
```

**Resultado confirmado en el portal:**

```text
TimeGenerated        12-nov-2026 17:59:53 (Bolivia)
Caller               frevarmct@hotmail.com
OperationNameValue   MICROSOFT.RESOURCES/SUBSCRIPTIONS/RESOURCEGROUPS/WRITE
ResourceGroup        RG-SC200-TEST-ACTIVITY
ActivityStatusValue  Success
```

En la primera prueba KQL no había ingestión aún (`TotalEventos=0`); se confirmó después vía CLI. En otra prueba se pegó accidentalmente el encabezado PowerShell `$query = @'` en el editor KQL: causa error de sintaxis, quitar esa línea. También **`Success`** es el estado en `AzureActivity`, aunque el Activity Log CLI muestre **`Succeeded`**.

### 9. Incidente de interfaz de conectores (no bloqueante)

Al abrir **Connector details -> Azure Activity** desde `security.microsoft.com`, incluso en InPrivate, apareció `NormalizationProvider is required` en `sentinel-connectors/20261112.1`. La lista de conectores sí cargaba. Se continuó mediante CLI y búsqueda avanzada, y la recepción de logs quedó verificada. El stack trace **sugiere** un problema del componente de interfaz, no demuestra un defecto global ni justifica eliminar el workspace.

### 10. Cierre didáctico y limpieza

- Preguntas para alumnos: ¿quién realizó la operación?, ¿qué grupo afectó?, ¿a qué hora?, ¿cómo se confirmó el estado?
- La operación `write` incluye creación **o actualización**; aquí sabemos que fue una creación porque se ejecutó `az group create`.
- **No se probó** regla automática ni incidente; eso es una ampliación posterior.
- Limpieza **si ya no se necesita** el grupo temporal y no contiene otros recursos:

```powershell
az group delete --name "rg-sc200-test-activity" --yes --no-wait
```

- No eliminar `diag-azureactivity-sc200` si seguirán usando la ingesta. Es posible que Log Analytics genere costos según uso.
