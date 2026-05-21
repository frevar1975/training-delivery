# ============================
# Demo AI-900 - Azure MCP Governance
# Limpieza de recursos
# ============================

$rg = "rg-demo-ai900-mcp"

Write-Host "====================================="
Write-Host "Eliminando recursos de la demo"
Write-Host "Resource Group: $rg"
Write-Host "====================================="

az group delete `
  --name $rg `
  --yes `
  --no-wait

Write-Host "Solicitud de eliminación enviada."
Write-Host "Puedes verificar con:"
Write-Host "az group exists --name $rg"