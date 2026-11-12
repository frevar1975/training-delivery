# SC-200 — Demo de despliegue de consultas en Microsoft Sentinel

**Curso:** SC-200  
**Centro y periodo:** Netxpress, octubre–noviembre de 2026  
**Workspace:** `law-sc200-repo-demo`  
**Repositorio de contenido:** [frevar1975/sentinel](https://github.com/frevar1975/sentinel)  
**Rama:** `main`

Esta guía de ejecución toma como base la [plantilla reutilizable de training-templates](https://github.com/frevar1975/training-templates/blob/main/SC-200/demo-github-sentinel/README.md).

## Comandos usados para crear el entorno desde cero

Estos comandos se ejecutan en **Git Bash (UCRT64)** después de `az login`. Seleccionan la suscripción de Visual Studio, crean el grupo y el workspace, registran el proveedor y habilitan Microsoft Sentinel. La identidad de Azure CLI necesita permisos para crear recursos y registrar proveedores en la suscripción.

~~~bash
# 1. Seleccionar la suscripción correcta
SUBSCRIPTION_ID="430c139d-1e7d-4f38-81cb-a03710c5a3d3"
az account set --subscription "$SUBSCRIPTION_ID"
az account show --query "{subscription:name, id:id, tenant:tenantId}" -o table

# 2. Crear el grupo de recursos y el workspace en East US
az group create --name rg-sc200 --location eastus -o table

az monitor log-analytics workspace create \
  --resource-group rg-sc200 \
  --workspace-name law-sc200-repo-demo \
  --location eastus \
  -o table

# 3. Confirmar que el workspace terminó de aprovisionarse
az monitor log-analytics workspace show \
  --resource-group rg-sc200 \
  --workspace-name law-sc200-repo-demo \
  --query "{name:name, location:location, state:provisioningState}" \
  -o table

# Si el nombre no aparece o se quiere revisar qué workspaces hay:
az monitor log-analytics workspace list \
  --query "[].{name:name, resourceGroup:resourceGroup, location:location, state:provisioningState}" \
  -o table

# 4. Registrar Microsoft Sentinel en la suscripción
az provider register --namespace Microsoft.SecurityInsights

# Consultar el estado; esperar hasta que muestre Registered
az provider show --namespace Microsoft.SecurityInsights --query registrationState -o tsv

# 5. Habilitar Microsoft Sentinel para el workspace
az rest --method put \
  --url "https://management.azure.com/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/rg-sc200/providers/Microsoft.OperationalInsights/workspaces/law-sc200-repo-demo/providers/Microsoft.SecurityInsights/onboardingStates/default?api-version=2025-09-01" \
  --body '{"properties":{"customerManagedKey":false}}'

# 6. Verificar que existe el estado de onboarding
az rest --method get \
  --url "https://management.azure.com/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/rg-sc200/providers/Microsoft.OperationalInsights/workspaces/law-sc200-repo-demo/providers/Microsoft.SecurityInsights/onboardingStates/default?api-version=2025-09-01" \
  -o jsonc
~~~

El comando `az provider register` puede quedar en estado `Registering` durante un rato. Repite `az provider show` hasta ver `Registered` antes de ejecutar el `az rest --method put`; si se ejecuta antes, Azure devuelve que la suscripción no está registrada.

Para este demo, después del onboarding también conectamos el repositorio desde el portal de Sentinel: **Content management → Repositories → Add new**. Allí se autoriza GitHub y se seleccionan el repositorio y la rama. Sentinel genera el workflow de GitHub Actions; el flujo no se configura solo con `az login` ni con el onboarding REST.

## Objetivo de la demostración

Crear una consulta guardada en el repositorio, desplegarla con GitHub Actions y comprobarla en Microsoft Sentinel.

La KQL usa `print` para devolver una fila de demostración. No depende de logs ingeridos, conectores ni alertas. La demo presenta el ciclo de contenido como código: GitHub → Actions → Sentinel.

## Estado previo verificado

- El workspace `law-sc200-repo-demo` está conectado al repositorio `frevar1975/sentinel`.
- El workflow **Deploy Content to law-sc200-repo-demo** despliega al workspace desde la rama `main`.
- Ya se desplegaron consultas de prueba desde el repositorio y se comprobó su origen **Repositories/Repositorios** en la lista de consultas.
- Se ejecutó correctamente una KQL `print` y devolvió una fila.

## Preparación antes de presentar

1. Abrir el workspace `law-sc200-repo-demo` en el portal Microsoft Defender/Sentinel.
2. Abrir GitHub, repositorio `frevar1975/sentinel`, y comprobar que **Actions** está habilitado.
3. Tener abiertas las pestañas de GitHub **Code**, **Actions** y Microsoft Sentinel **Hunting → Queries**.

## Paso a paso para mostrar la creación

### 1. Crear el archivo de consulta

En GitHub:

1. Abrir `SentinelContent/Queries`.
2. Seleccionar **Add file → Create new file**.
3. Escribir como ruta del archivo:

   `SentinelContent/Queries/SC200-Demo-RepoQuery-3.json`

4. Pegar el siguiente JSON:

~~~json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "workspace": {
      "type": "string"
    }
  },
  "resources": [
    {
      "type": "Microsoft.OperationalInsights/workspaces/savedSearches",
      "apiVersion": "2020-03-01-preview",
      "name": "[concat(parameters('workspace'), '/sc200-demo-repo-query-3')]",
      "properties": {
        "Category": "Hunting Queries",
        "DisplayName": "SC-200 Demo 3 - Consulta creada en GitHub",
        "Query": "print Demo = 'Consulta creada en GitHub y desplegada en Sentinel'",
        "Tags": [
          {
            "Name": "Description",
            "Value": "Consulta de demostración para mostrar el despliegue desde GitHub."
          },
          {
            "Name": "Tactics",
            "Value": "Discovery"
          }
        ]
      }
    }
  ]
}
~~~

5. Seleccionar **Commit changes**, usar el mensaje `Agregar consulta demo 3` y confirmar directamente en `main`.

El sufijo `3` hace único el nombre interno y el archivo. Si ya se usó en otra presentación, aumentar el sufijo en el archivo, el nombre interno y el título.

### 2. Mostrar el despliegue

1. En el repositorio, abrir **Actions**.
2. Abrir el run que corresponde al commit recién hecho.
3. Esperar al estado **Succeeded** (marca verde).
4. Abrir el job `deploy-content` y mostrar el paso **Deploy Content to Microsoft Sentinel** finalizado correctamente.

El workflow se inicia con cambios en la rama `main`. Si no aparece un run, revisar el commit y confirmar que Actions no esté deshabilitado.



#### Verificación opcional por Azure CLI

Después del run exitoso, confirma que el recurso se guardó en el workspace:

~~~bash
az rest --method get \\
  --url "https://management.azure.com/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/rg-sc200/providers/Microsoft.OperationalInsights/workspaces/law-sc200-repo-demo/savedSearches/sc200-demo-repo-query-3?api-version=2020-03-01-preview" \\
  --query "{name:name, displayName:properties.displayName, category:properties.category, query:properties.query}" \\
  -o yaml
~~~

Debe mostrar el nombre interno `sc200-demo-repo-query-3`, el título **SC-200 Demo 3 - Consulta creada en GitHub** y la KQL. Este GET es opcional; en clase también puedes demostrarlo desde la lista **Queries/Consultas** de Sentinel.

### 3. Mostrar la consulta en Sentinel

1. Volver al workspace `law-sc200-repo-demo`.
2. Ir a **Threat management → Hunting → Queries** (en español puede aparecer como **Consultas**).
3. Buscar **SC-200 Demo 3 - Consulta creada en GitHub**.
4. Seleccionarla y mostrar que el origen del contenido indica **Repositories/Repositorios**.

No buscarla en **Hunts/Búsquedas**: una Hunt es una investigación diferente de una consulta guardada.

### 4. Mostrar el resultado KQL

1. Abrir **Advanced hunting / Búsqueda avanzada** con el workspace `law-sc200-repo-demo` seleccionado.
2. Pegar:

~~~kusto
print Demo = 'Consulta creada en GitHub y desplegada en Sentinel'
~~~

3. Seleccionar **Run query / Ejecutar consulta**.
4. Mostrar una fila en los resultados, con la columna `Demo`.

La lista de **Queries/Consultas** confirma que el contenido se desplegó desde el repositorio. La ejecución de `print` demuestra el resultado sin requerir telemetría real. Si Advanced hunting abre el editor vacío, pegar la KQL manualmente: la lista de consultas guardadas y el editor son pantallas distintas.

## Guion para explicar mientras se presenta

> “La consulta está definida como contenido en GitHub. Al confirmar el archivo en la rama principal, GitHub Actions ejecuta el workflow que publica ese contenido en Sentinel. Verificamos el run, vemos la consulta con origen Repositories y ejecutamos su KQL para obtener una fila de prueba.”

## Evidencias que mostrar

1. Archivo JSON nuevo en `SentinelContent/Queries`.
2. Commit en `main`.
3. Run exitoso en GitHub Actions.
4. Consulta en Sentinel con origen **Repositories**.
5. Resultado de una fila en Advanced hunting.

## Si falla

- **No aparece el run:** confirmar que el commit está en `main` y que Actions está habilitado.
- **Actions falla:** abrir el paso fallido y revisar su log; validar la conexión del repositorio y los permisos de la identidad de despliegue.
- **La consulta no aparece:** comprobar que se está viendo el workspace `law-sc200-repo-demo`, actualizar la lista y buscar el título completo.
- **El editor aparece vacío:** pegar la KQL anterior y ejecutarla.
- **No hay logs en el workspace:** la prueba sigue funcionando; `print` no consulta tablas de eventos.

## Cierre didáctico

La consulta se mantiene en Git como código fuente y el workflow automatiza su publicación en Sentinel. En un escenario real, el contenido versionado puede revisarse y desplegarse de forma controlada; esta prueba se centra en el ciclo de administración del contenido, no en generar una detección.
