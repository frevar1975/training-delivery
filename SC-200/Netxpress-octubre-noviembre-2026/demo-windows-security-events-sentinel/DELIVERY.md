# Ejecución del demo de eventos Windows 4625 en Microsoft Sentinel

Guía de ejecución: [Demo_Evento_4625_Windows_Microsoft_Sentinel_SC-200.docx](Demo_Evento_4625_Windows_Microsoft_Sentinel_SC-200.docx).

## Resultado verificado

Se generó un fallo de autenticación controlado en la VM `winsentdemo`. La búsqueda en Microsoft Sentinel devolvió **una fila** en la tabla `SecurityEvent`, con `EventID=4625` y detalle `An account failed to log on`. La consulta de Heartbeat devolvió 10 filas de `winsentdemo`, confirmando que AMA se comunicaba con el workspace.

El demo concluyó con la consulta del registro. No se creó una regla analítica; por lo tanto, no se generó una alerta ni un incidente de Sentinel.

## Entorno usado

- Workspace: `law-sc200-repo-demo` en `rg-sc200`, East US.
- Grupo de recursos de VM y DCR: `rg-sc200-windows-demo`.
- VM: `winsentdemo`, Windows Server 2022, Standard_B2s, East US.
- Agente: `AzureMonitorWindowsAgent`, estado `Succeeded`.
- DCR: `dcr-windows-4625-demo`, con filtro XPath para Security Event ID 4625.
- Asociación: `assoc-win-4625-demo`.
- Fuente/flujo: `Microsoft-SecurityEvent`.
- Destino: workspace `law-sc200-repo-demo`.

No se conserva en este registro el ID de suscripción, IP pública, contraseña ni información personal.

## Pasos que se ejecutaron

1. Se creó el grupo de recursos dedicado `rg-sc200-windows-demo`.
2. Se creó la VM `winsentdemo`. El intento inicial con un nombre de VM demasiado largo falló porque el nombre del equipo Windows supera el límite de 15 caracteres; se recreó con el nombre corto `winsentdemo`.
3. Se asignó identidad administrada a la VM y se instaló `AzureMonitorWindowsAgent`.
4. Se recuperó el ID del workspace `law-sc200-repo-demo`.
5. Se preparó una DCR Windows con fuente `windowsEventLogs`, stream `Microsoft-SecurityEvent`, filtro `Security!*[System[(EventID=4625)]]`, destino Log Analytics y flujo al workspace.
6. El comando `az monitor data-collection rule create --rule-file` devolvió `InvalidResource: properties are missing`. La DCR se creó correctamente con `az rest` usando la API ARM `2023-03-11`. El GET REST confirmó fuente, filtro, destino, flujo y estado `Succeeded`.
7. Se asoció la DCR a `winsentdemo` con `assoc-win-4625-demo`.
8. Se verificó la política de auditoría `Logon`; reportó `Success and Failure`.
9. Se usó `net.exe use \\localhost\IPC$` con usuario ficticio y contraseña falsa. La salida `System error 1326` era esperada. Windows escribió el evento local 4625.
10. Se confirmó el evento local y luego se consultaron `Heartbeat` y `SecurityEvent` en Sentinel.

## Consultas finales

```kusto
Heartbeat
| where Category == "Azure Monitor Agent"
| where Computer contains "winsentdemo"
| where TimeGenerated > ago(1h)
| take 10
```

```kusto
SecurityEvent
| where TimeGenerated > ago(2h)
| where EventID == 4625
| where Computer contains "winsentdemo"
| project TimeGenerated, Computer, EventID, Account, IpAddress, Activity
| order by TimeGenerated desc
```

La consulta de diagnóstico con `union isfuzzy=true` encontró el mismo evento en `SecurityEvent`; no apareció en `Event`.

## Mensaje para presentar

“Creamos un fallo de autenticación controlado en Windows. AMA recoge los eventos seleccionados por la DCR y los envía al workspace. Sentinel ya puede consultar el EventID 4625 para investigar el equipo y el detalle. En esta demostración validamos ingesta e investigación; crear una alerta requiere una regla analítica adicional y no forma parte del recorrido.”

## Notas de ejecución

- `Heartbeat` confirma comunicación del agente, pero la prueba de ingesta fue la fila de 4625 en `SecurityEvent`.
- El evento se generó contra `localhost`; su dirección de origen fue `::1`. No se debe presentarlo como un intento de ataque externo.
- La pantalla de Analytics rule wizard se abrió, pero se decidió obviar la creación de la regla para mantener el alcance del demo en ingesta e investigación.
- La imagen `Win2022Datacenter` emitió un aviso de deprecación futura. Validar la imagen disponible antes de repetir el laboratorio.
- Para limpieza, eliminar únicamente `rg-sc200-windows-demo` si ya no se necesita. El workspace queda fuera de ese grupo.
