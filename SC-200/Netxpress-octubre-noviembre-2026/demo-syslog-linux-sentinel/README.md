# Demo ejecutada de ingesta de Syslog Linux en Microsoft Sentinel

Registro de la demostración práctica realizada para SC-200. El resultado se verificó en la tabla `Syslog` del workspace. Este documento no incluye identificadores de suscripción.

**Plataforma:** Azure, Ubuntu 22.04, Azure Monitor Agent y Microsoft Sentinel.  
**Terminal:** Windows PowerShell con Azure CLI.  
**Workspace seleccionado:** `law-sc200-repo-demo`.  
**Grupo de recursos de la VM:** `rg-sc200-alert-demo`.  
**VM:** `vm-linux-syslog-demo`, `Standard_B2s`, región `eastus`.  
**DCR creada:** `recoleccionSC`.

## Resultado

Se generaron eventos Syslog de prueba desde la VM Linux y se confirmaron en Sentinel. La consulta devolvió dos filas con `Computer=vm-linux-syslog-demo`, `Facility=local4` y `SeverityLevel=warning`. La tabla `Heartbeat` también mostró registros recientes de la VM con `OSType=Linux`.

## Recorrido observado

**VM Linux → Syslog local → AMA → DCR asociada → workspace → tabla `Syslog` → consulta KQL.** La verificación de Heartbeat confirmó la comunicación del agente con Azure Monitor. La consulta de Syslog confirmó además que el evento llegó y cumplió el filtro de la DCR.

## Pasos ejecutados

### 1. Crear el grupo de recursos de prueba

```powershell
az group create --name "rg-sc200-alert-demo" --location "eastus"
```

La operación creó el grupo vacío donde después se desplegó la VM.

### 2. Crear la VM Linux

```powershell
az vm create --resource-group "rg-sc200-alert-demo" --name "vm-linux-syslog-demo" --location "eastus" --image "Ubuntu2204" --size "Standard_B2s" --admin-username "azureuser" --generate-ssh-keys --nsg-rule "NONE"
```

Azure devolvió estado `VM running`, dirección privada y dirección pública. `--nsg-rule "NONE"` no creó una regla de entrada para SSH. Las claves se generaron localmente; no se guardan en el repositorio.

### 3. Instalar la solución Syslog y abrir el conector

En Content hub se instaló la solución **Syslog**. Dentro de la solución se seleccionó **Syslog via AMA** y se abrió su página de configuración.

### 4. Crear la regla DCR y asociarla a la VM

Desde **Configuration → + Create data collection rule** se creó `recoleccionSC`. Se seleccionó `LOG_LOCAL4` con nivel mínimo `LOG_WARNING`; el asistente vinculó la regla al recurso de la VM. La página del conector mostró la DCR en su lista de reglas.

En palabras simples, la asociación asigna a la VM la regla que indica qué registros Syslog recopilar.

### 5. Verificar AMA

```powershell
az vm extension list --resource-group "rg-sc200-alert-demo" --vm-name "vm-linux-syslog-demo" --query "[].{Nombre:name,Tipo:type,Estado:provisioningState}" -o table
```

**Resultado observado:** `AzureMonitorLinuxAgent` con estado `Succeeded`.

### 6. Verificar la asociación de DCR

```powershell
az monitor data-collection rule association list --resource "$(az vm show --resource-group "rg-sc200-alert-demo" --name "vm-linux-syslog-demo" --query id -o tsv)" --query "[].{Asociacion:name,Grupo:resourceGroup}" -o table
```

**Resultado observado:** asociación `recoleccionSC-association` en el grupo de recursos de prueba. La consulta filtra la salida para no mostrar identificadores de suscripción.

### 7. Generar eventos Syslog desde Linux

```powershell
az vm run-command invoke --resource-group "rg-sc200-alert-demo" --name "vm-linux-syslog-demo" --command-id RunShellScript --scripts "logger -p local4.warning -t SC200-LINUX-DEMO 'Prueba Syslog Linux para Sentinel'"
```

Se ejecutó el envío de la prueba más de una vez. Azure CLI volvió al prompt sin imprimir salida visible; se usó la consulta en Sentinel como evidencia definitiva.

### 8. Confirmar la comunicación del agente

```kusto
Heartbeat
| where TimeGenerated > ago(1h)
| project TimeGenerated, Computer, OSType
| order by TimeGenerated desc
```

**Resultado observado:** registros recientes de `vm-linux-syslog-demo` con `OSType=Linux`.

### 9. Confirmar la ingesta de Syslog

```kusto
Syslog
| where TimeGenerated > ago(1h)
| where Computer =~ "vm-linux-syslog-demo"
| project TimeGenerated, Computer, Facility, SeverityLevel, SyslogMessage
| order by TimeGenerated desc
```

**Resultado observado:** dos filas de la VM, con facility `local4` y severidad `warning`. El texto se veía truncado en la grilla; al expandir la fila se puede revisar el mensaje completo.

Consulta para aislar solo las pruebas etiquetadas:

```kusto
Syslog
| where TimeGenerated > ago(1h)
| where SyslogMessage contains "SC200-LINUX-DEMO"
| project TimeGenerated, Computer, Facility, SeverityLevel, SyslogMessage
| order by TimeGenerated desc
```

## Explicación para la clase

“Instalamos una solución para disponer del conector Syslog via AMA. Después creamos una DCR que define el filtro y la asociamos a la VM Linux. AMA recoge los eventos de la máquina y los envía al workspace. En `Syslog` confirmamos que llegó el evento; desde ahí podemos investigarlo con KQL.”

**Analogía:** el conector es el canal de entrada, AMA es el recolector instalado en Linux y la DCR es la instrucción que le dice al recolector qué eventos aceptar y en qué máquinas aplicarla.

## Lecciones del diagnóstico

- Que AMA aparezca como `Succeeded` confirma que la extensión quedó provisionada, pero no demuestra por sí solo que Syslog haya llegado.
- `Heartbeat` confirmó que el agente se comunicaba con Azure Monitor.
- La DCR debía estar asociada a la VM y contener un filtro compatible con el evento (`local4`, `warning`).
- La evidencia final fue el registro visible en `Syslog` con facility y severidad esperadas.
- La salida vacía del comando `az vm run-command invoke` no impidió demostrar la ingesta; la consulta KQL confirmó los eventos.

## Limpieza

La VM y otros recursos de prueba pueden generar cargos. Cuando ya no se necesite el demo, revisar el contenido de `rg-sc200-alert-demo` y eliminar el grupo solo si contiene exclusivamente recursos desechables de esta práctica:

```powershell
az group delete --name "rg-sc200-alert-demo" --yes --no-wait
```

El workspace `law-sc200-repo-demo` está fuera del grupo de la VM; no se elimina con este comando.

## Referencias oficiales

- [Recopilar eventos Syslog con Azure Monitor Agent](https://learn.microsoft.com/azure/azure-monitor/vm/data-collection-syslog)
- [Solucionar problemas de Syslog con AMA en Linux](https://learn.microsoft.com/azure/azure-monitor/agents/azure-monitor-agent-troubleshoot-linux-vm-rsyslog)
- [Asociaciones de reglas de recopilación de datos](https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-rule-associations)
