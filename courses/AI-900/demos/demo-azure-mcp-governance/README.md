# Demo AI-900 - Azure MCP Governance

## Descripcion

Esta demo muestra como usar GitHub Copilot CLI con Azure MCP Server para consultar recursos reales en Azure y revisar aspectos basicos de gobierno, como el uso de tags.

La demo crea:

- Un Resource Group
- Un Storage Account con tags
- Una Virtual Network con tags
- Un Storage Account sin tags para simular un problema de gobierno

## Objetivo pedagogico

Demostrar como un agente de IA puede usar herramientas para consultar recursos reales, razonar sobre ellos y generar explicaciones utiles.

## Requisitos

- Azure CLI
- PowerShell
- GitHub Copilot CLI
- Node.js
- Suscripcion de Azure activa
- Permisos para crear recursos en Azure

## Ejecucion

Desde la carpeta del demo:

```powershell
cd C:\GithubOrden\training-delivery\courses\AI-900\demos\demo-azure-mcp-governance
```

Ejecutar el script:

```powershell
.\scripts\01-create-resources.ps1
```

Luego abrir Copilot CLI:

```powershell
copilot
```

Usar los prompts del archivo:

```text
prompts/copilot-prompts.md
```

## Limpieza

Al finalizar la demo, ejecutar:

```powershell
.\scripts\99-cleanup.ps1
```

## Relacion con AI-900

Esta demo complementa los temas de:

- IA generativa
- Copilots
- Agentes
- Uso responsable de IA
- Contexto y grounding
- Automatizacion asistida por IA

## Nota

Este material es complementario y no reemplaza el contenido oficial del curso Microsoft.
