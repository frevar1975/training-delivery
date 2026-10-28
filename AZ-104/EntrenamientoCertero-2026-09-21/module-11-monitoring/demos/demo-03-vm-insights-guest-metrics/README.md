# Ensayo real · Demo 3 — VM Insights clásico con KQL

**Curso:** AZ-104 · **Ejecución de referencia:** 28 de octubre de 2026 · **Módulo:** 11

Guía reutilizable para repetir este demo desde cero: [VM Insights clásico: métricas de Linux con KQL](https://github.com/frevar1975/training-templates/blob/main/AZ-104/module-11-monitoring/demos/demo-03-vm-insights-guest-metrics/README.md).

## Entorno usado en el ensayo

El ensayo se hizo en la suscripción seleccionada por el instructor, sin guardar su ID en este repositorio. Se usaron:

- Grupo: `rg-demo-loganalytics`
- VM Ubuntu: `vm-demo-logs`
- Workspace Log Analytics: `law-demo-loganalytics`
- DCR clásica: `dcr-demo-vminsights`
- Asociación: `assoc-vminsights-demo`

La VM y el workspace ya estaban creados para el laboratorio Linux de Log Analytics; en este ensayo se agregó la DCR de VM Insights. La plantilla del demo 3 describe una implementación nueva y aislada desde cero.

## Resultado validado

- Azure Monitor Agent quedó activo y Heartbeat llegó al workspace.
- La DCR clásica quedó en estado `Succeeded`, con `kind Linux`, destino `law-demo-loganalytics` y flujo `Microsoft-InsightsMetrics`.
- Después de corregir la DCR y renovar su asociación, KQL devolvió filas de `InsightsMetrics` con origen `vm.azm.ms`.
- En los resultados se observaron `Processor / UtilizationPercentage`, `Memory / AvailableMB`, `LogicalDisk / FreeSpaceMB`, `FreeSpacePercentage`, `Status` y `Computer / Heartbeat`.
- La consulta de Heartbeat mostró 66 muestras para la VM en la ventana de dos horas.
- El ensayo demostró que tener Heartbeat no garantiza por sí solo que las métricas de VM Insights ya estén llegando; validar `InsightsMetrics` por separado.

Consulta usada para verificar las métricas:

```kusto
InsightsMetrics
| where TimeGenerated > ago(1h)
| where Computer =~ "vm-demo-logs"
| where Origin == "vm.azm.ms"
| summarize Muestras=count(), Ultimo=max(TimeGenerated) by Namespace, Name, Origin
| order by Namespace asc, Name asc
```

## Errores encontrados y correcciones incorporadas a la plantilla

1. **Contexto de suscripción distinto:** una consola no encontraba el grupo porque estaba activa otra suscripción. En PowerShell o Cloud Shell, ejecutar `az account show`, seleccionar la suscripción con su ID completo mediante `az account set` y comprobar que el grupo aparece antes de ejecutar comandos sobre la VM. No usar un ID truncado con puntos suspensivos.
2. **Sintaxis del shell:** en PowerShell definir variables con `$RG = "..."`; no copiar la forma Bash `RG="..."`. Al pegar bloques, copiar el código, no los prompts `PS C:\>` ni `>>`.
3. **DCR sin tipo:** la primera actualización sin `--kind Linux` fue rechazada porque el tipo de la regla es inmutable. La plantilla pasa `--kind Linux` al crear la DCR desde el primer intento.
4. **Contador con escapes duplicados:** la primera versión del JSON llevaba cuatro barras invertidas por separador. La DCR esperaba `\\VmInsights\\DetailedMetrics` en el JSON (dos caracteres de barra por separador, que representan una barra real). Se corrigió y se comprobó el valor con `az monitor data-collection rule show`.
5. **AMA no aplicó inmediatamente la configuración corregida:** reiniciar el servicio no bastó para que la regla nueva apareciera en el caché local. Se recreó únicamente la asociación de `dcr-demo-vminsights`, se esperó la propagación y luego aparecieron las filas KQL. La guía indica esperar y tratar la asociación como paso de resincronización si una DCR actualizada sigue sin reflejarse.
6. **Rutas de métricas distintas:** el portal mostró también la experiencia OpenTelemetry con destino a un Azure Monitor workspace. Esa ruta se consulta con PromQL; no valida los datos clásicos de Log Analytics. Para este demo, la prueba de éxito es `InsightsMetrics` en `law-demo-loganalytics`.

## Guion de cierre

1. Mostrar Heartbeat para confirmar que AMA se comunica con el workspace.
2. Mostrar `InsightsMetrics` para confirmar las métricas invitadas y explicar los campos Namespace, Name, Origin y Val.
3. Ejecutar la carga de CPU controlada y volver a graficar `Processor / UtilizationPercentage`.
4. Aclarar que una vista OpenTelemetry vacía y una consulta KQL clásica vacía son diagnósticos de rutas diferentes.
5. Eliminar solo el grupo temporal cuando termine la demostración.

## Limpieza

La limpieza del grupo de ensayo se inició por el instructor. Confirmar que la operación concluyó antes de considerar el entorno eliminado:

```powershell
az group exists --name rg-demo-loganalytics
```

El resultado debe ser `false`. No guardar IDs de suscripción, direcciones IP, correos ni credenciales en el registro del curso.
