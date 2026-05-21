# ============================
# Demo AI-900 - Azure MCP Governance
# Crear recursos base en Azure
# ============================

$random = Get-Random -Minimum 10000 -Maximum 99999

$rg = "rg-demo-ai900-mcp"
$location = "eastus"
$storage = "stdemoai900$random"
$storageNoTags = "stnotags$random"
$vnet = "vnet-demo-ai900"
$subnet = "subnet-apps"

Write-Host "====================================="
Write-Host "Creando recursos para la demo AI-900 MCP"
Write-Host "====================================="
Write-Host "Resource Group: $rg"
Write-Host "Location: $location"
Write-Host "Storage con tags: $storage"
Write-Host "Storage sin tags: $storageNoTags"
Write-Host "VNet: $vnet"
Write-Host "Subnet: $subnet"
Write-Host "====================================="

# Validar cuenta activa
az account show --output table

# Crear Resource Group
az group create `
  --name $rg `
  --location $location `
  --tags Proyecto=DemoAI900MCP Ambiente=Demo Responsable=Freddy

# Crear Storage Account con tags
az storage account create `
  --name $storage `
  --resource-group $rg `
  --location $location `
  --sku Standard_LRS `
  --kind StorageV2 `
  --min-tls-version TLS1_2 `
  --allow-blob-public-access false `
  --tags Proyecto=DemoAI900MCP Ambiente=Demo Servicio=Storage Responsable=Freddy

# Crear Virtual Network con Subnet
az network vnet create `
  --name $vnet `
  --resource-group $rg `
  --location $location `
  --address-prefix 10.10.0.0/16 `
  --subnet-name $subnet `
  --subnet-prefixes 10.10.1.0/24 `
  --tags Proyecto=DemoAI900MCP Ambiente=Demo Servicio=Network Responsable=Freddy

# Crear Storage Account sin tags para simular problema de gobierno
az storage account create `
  --name $storageNoTags `
  --resource-group $rg `
  --location $location `
  --sku Standard_LRS `
  --kind StorageV2 `
  --min-tls-version TLS1_2 `
  --allow-blob-public-access false

# Listar recursos creados
Write-Host "====================================="
Write-Host "Recursos creados:"
Write-Host "====================================="

az resource list `
  --resource-group $rg `
  --output table

Write-Host "====================================="
Write-Host "Demo creada correctamente."
Write-Host "Ahora abre Copilot CLI con: copilot"
Write-Host "====================================="