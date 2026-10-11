# Demo 01 — Escalado provocado de una web con VMSS y azd

**Curso:** AZ-104 · **Centro:** Entrenamiento Certero · **Inicio de ejecución:** 2026-09-21 · **Módulo:** 8.

## Objetivo

Los siete alumnos generan solicitudes de cálculo desde una web. Un script del instructor representa usuarios adicionales. Azure Monitor agrega una segunda VM cuando Percentage CPU promedio supera 60 % en una ventana de cinco minutos. Al detener la carga, una regla por debajo de 25 % durante cinco minutos reduce el conjunto a una VM. El perfil tiene mínimo 1 y máximo 2; cooldown de cinco minutos.

La ventana de evaluación no incluye todo el tiempo de publicación de métricas, arranque de las nuevas VMs y sondas. Ensayar antes de clase.

## Arquitectura

Navegadores y script → IP pública → Load Balancer puerto 80 → backend Python puerto 8080 en VMSS Uniform Ubuntu. La sonda HTTP consulta `/health`. `app.py` ejecuta cálculos reales en `/work`, limita concurrencia y muestra el hostname de la instancia.

`azure.yaml` configura infraestructura Bicep. `infra/main.bicep` crea el grupo a nivel de suscripción y `infra/web.bicep` declara red, NSG, IP, balanceador, VMSS y autoscaling. La aplicación se incorpora desde `app.py` al cloud-init durante la compilación y se instala en cada nueva VM. No se declara un servicio separado de azd: la web queda instalada durante el aprovisionamiento.

## Abrir el proyecto

Si ya tienes clonado training-delivery, sincroniza tu clon y entra en la carpeta de esta demo. Para probar este PR antes de fusionarlo, selecciona la rama `demo/az104-vmss-autoscale-azd`.

```powershell
git clone https://github.com/frevar1975/training-delivery.git
Set-Location .\training-delivery
git switch demo/az104-vmss-autoscale-azd
Set-Location .\AZ-104\EntrenamientoCertero-2026-09-21\module-08-virtual-machines\demos\demo-01-vmss-autoscale-web
```

## Preparar y desplegar

Instala azd y Azure CLI si faltan; abre una nueva terminal después de instalar.

```powershell
winget install --exact --id Microsoft.Azd
winget install --exact --id Microsoft.AzureCLI
azd version
az version
azd auth login
az login
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\scripts\01-create-resources.ps1 -SubscriptionId "TU-ID-DE-SUSCRIPCION"
```

El script selecciona o crea `az104-certero-20260921`, fija `eastus2` y `Standard_D2s_v5`, prepara la clave pública y ejecuta `azd up`. El grupo será `rg-az104-certero-20260921`. Para consultas con Azure CLI selecciona la misma suscripción con `az account set --subscription "TU-ID-DE-SUSCRIPCION"`.

Necesitas permisos de despliegue a nivel de suscripción y cuota de hasta cuatro vCPU en la región y familia de VM. El demo no publica SSH y se administra con Azure Run Command. La clave pública temporal no conserva una clave privada utilizable para SSH.

Para el flujo manual usa la [guía detallada](GUIA-INSTRUCTOR.md). No ejecutes `azd init`: la plantilla ya está preparada.

## Verificar y compartir

```powershell
$Url = (azd env get-value DEMO_URL).Trim()
$Rg = (azd env get-value AZURE_RESOURCE_GROUP).Trim()
$Vmss = (azd env get-value VMSS_NAME).Trim()
curl.exe --connect-timeout 5 --max-time 10 "$Url/health"
curl.exe --connect-timeout 5 --max-time 30 "$Url/work"
Start-Process $Url
```

Comparte `$Url`; pide pulsar **Participar continuamente**. Muestra Percentage CPU con agregación Average, las instancias y el historial de autoscaling. La página por sí sola es liviana: los cálculos se generan con los botones.

## Reforzar la carga

En otra terminal, dentro de esta demo:

```powershell
$Url = (azd env get-value DEMO_URL).Trim()
.\scripts\Carga-Web.ps1 -Url $Url -Clientes 12 -Minutos 15
```

Si CPU no supera 60 % sostenido, detén con Ctrl+C y ensaya 20 clientes. El script abre nuevas conexiones y termina después del plazo. El balanceador no garantiza alternancia estricta de hostnames.

Para observar reducción: todos los alumnos deben detener su participación y el instructor debe terminar el script. Espera la ventana, cooldown y evaluación de estabilidad.

## Eliminar recursos

Primero detén toda la carga. Comprueba que el entorno seleccionado corresponda a esta demo:

```powershell
azd env select az104-certero-20260921
.\scripts\99-cleanup.ps1
```

El script muestra entorno y grupo y conserva la confirmación interactiva de `azd down`. Los recursos tienen costos mientras existan; otros demos en grupos diferentes no se eliminan.

## Validación

Backend probado localmente: portada, sonda y cálculos concurrentes. YAML, JSON y rutas de la plantilla revisados. No se ha compilado Bicep ni desplegado con azd en una suscripción desde este entorno; el PR queda en borrador para completar ese ensayo.

No subir `.azure/`, credenciales, URLs generadas ni archivos locales de estado. El `.gitignore` de la demo los excluye.
