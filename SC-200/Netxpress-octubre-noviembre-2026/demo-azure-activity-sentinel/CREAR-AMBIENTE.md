# CREAR AMBIENTE — SC-200 | Microsoft Sentinel

Ejecución registrada el **13 de noviembre de 2026** para el curso SC-200 de Netxpress. Terminal: **Windows PowerShell 5.1**. La suscripción se selecciona por su nombre; este documento no guarda su identificador.

## 1. Seleccionar y comprobar la suscripción

Azure CLI ya tenía una sesión iniciada. Si se necesita iniciar sesión de nuevo, ejecutar:

```powershell
az login
```

Se seleccionó la suscripción **Visual Studio Enterprise** por nombre y se verificó que estuviera habilitada:

```powershell
$subscriptionName = "Suscripción de Visual Studio Enterprise"
az account set --subscription $subscriptionName
az account show --query "{Suscripcion:name,Estado:state,Tenant:tenantId}" -o table
```

El comando de consulta no muestra el ID de la suscripción.

## 2. Crear el grupo de recursos

```powershell
az group create --name "rg-sc200" --location "eastus"
```

## 3. Crear el workspace de Log Analytics

```powershell
az monitor log-analytics workspace create `
  --resource-group "rg-sc200" `
  --workspace-name "law-sc200-repo-demo" `
  --location "eastus" `
  --sku "PerGB2018"
```

**Resultado observado:** `ProvisioningState: Succeeded`, ubicación `eastus`, grupo `rg-sc200`, retención inicial de 30 días.

## 4. Habilitar Microsoft Sentinel

En Azure Portal:

1. Buscar y abrir **Microsoft Sentinel**.
2. Seleccionar **Create**.
3. Elegir el workspace `law-sc200-repo-demo` del grupo `rg-sc200`.
4. Seleccionar **Add** y esperar a que termine.

## 5. Instalar Azure Activity desde Content hub

1. En Sentinel, abrir **Content hub** (Centro de contenido).
2. Buscar y seleccionar la solución **Azure Activity**.
3. Seleccionar **Install** y esperar a que finalice.

**Estado al cerrar esta guía:** el grupo y el workspace fueron creados correctamente; Sentinel quedó agregado al workspace y la solución Azure Activity quedó instalada. Aún falta configurar el conector de datos para enviar eventos de la suscripción al workspace. Esa configuración se documentará en el siguiente paso del demo.

## Comandos usados

```powershell
az account set --subscription $subscriptionName
az account show --query "{Suscripcion:name,Estado:state,Tenant:tenantId}" -o table
az group create --name "rg-sc200" --location "eastus"
az monitor log-analytics workspace create --resource-group "rg-sc200" --workspace-name "law-sc200-repo-demo" --location "eastus" --sku "PerGB2018"
```
