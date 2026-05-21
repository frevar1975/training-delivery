# Setup desde cero - Demo AI-900 Azure MCP Governance

## Objetivo

Preparar una PC Windows desde cero para ejecutar la demo de AI-900 con Azure, GitHub Copilot CLI y Azure MCP.

Esta guia instala las herramientas necesarias, autentica las cuentas, clona el repositorio y ejecuta la demo.

---

## 1. Requisitos previos

Antes de comenzar, necesitas:

- Cuenta de GitHub
- Acceso a GitHub Copilot
- Suscripcion de Azure activa
- Permisos para crear recursos en Azure
- Windows 10 o Windows 11
- PowerShell

---

## 2. Instalar Git

Abrir PowerShell como administrador y ejecutar:

```powershell
winget install --id Git.Git -e
```

Cerrar y volver a abrir PowerShell.

Validar:

```powershell
git --version
```

Configurar identidad de Git:

```powershell
git config --global user.name "Freddy Julio Vargas Ibanez"
git config --global user.email "frevar1975@gmail.com"
```

Validar:

```powershell
git config --global user.name
git config --global user.email
```

---

## 3. Instalar GitHub CLI

GitHub CLI permite autenticarse con GitHub, clonar repositorios y administrar repos desde la terminal.

Instalar:

```powershell
winget install --id GitHub.cli
```

Cerrar y volver a abrir PowerShell.

Validar:

```powershell
gh --version
```

Iniciar sesion:

```powershell
gh auth login
```

Opciones sugeridas:

```text
GitHub.com
HTTPS
Login with a web browser
```

Validar autenticacion:

```powershell
gh auth status
```

---

## 4. Instalar Azure CLI

Azure CLI permite autenticarse en Azure y crear recursos desde terminal.

Instalar:

```powershell
winget install Microsoft.AzureCLI
```

Cerrar y volver a abrir PowerShell.

Validar:

```powershell
az version
```

Iniciar sesion en Azure:

```powershell
az login
```

Validar cuenta activa:

```powershell
az account show --output table
```

Si tienes varias suscripciones, listar:

```powershell
az account list --output table
```

Seleccionar una suscripcion:

```powershell
az account set --subscription "NOMBRE_O_ID_DE_LA_SUSCRIPCION"
```

---

## 5. Instalar Node.js

Node.js es necesario para ejecutar herramientas basadas en npm y Azure MCP.

Instalar Node.js LTS:

```powershell
winget install OpenJS.NodeJS.LTS
```

Cerrar y volver a abrir PowerShell.

Validar:

```powershell
node -v
npm -v
```

---

## 6. Instalar GitHub Copilot CLI

Opcion recomendada en Windows:

```powershell
winget install GitHub.Copilot
```

Opcion alternativa usando npm:

```powershell
npm install -g @github/copilot
```

Validar:

```powershell
copilot --version
```

Iniciar Copilot CLI:

```powershell
copilot
```

Dentro de Copilot CLI, iniciar sesion:

```text
/login
```

Salir de Copilot CLI:

```text
/exit
```

---

## 7. Clonar el repositorio

Crear carpeta de trabajo:

```powershell
mkdir C:\GithubOrden
cd C:\GithubOrden
```

Clonar el repo:

```powershell
gh repo clone frevar1975/training-delivery
```

Entrar al repo:

```powershell
cd C:\GithubOrden\training-delivery
```

Validar estado:

```powershell
git status
```

---

## 8. Ubicarse en la demo

```powershell
cd C:\GithubOrden\training-delivery\courses\AI-900\demos\demo-azure-mcp-governance
```

Ver archivos:

```powershell
tree /F
```

---

## 9. Ejecutar creacion de recursos

Ejecutar:

```powershell
.\scripts\01-create-resources.ps1
```

La demo creara:

- Resource Group
- Storage Account con tags
- Virtual Network con tags
- Storage Account sin tags

El Storage Account sin tags se usa para simular un problema de gobierno cloud.

---

## 10. Abrir Copilot CLI

Desde la misma carpeta de la demo:

```powershell
copilot
```

Usar los prompts del archivo:

```text
prompts/copilot-prompts.md
```

Prompts principales:

```text
Lista los recursos del resource group rg-demo-ai900-mcp.
```

```text
Identifica que recursos no tienen tags.
```

```text
Explicame por que un recurso sin tags puede ser un problema de gobierno en Azure.
```

```text
Dame un resumen ejecutivo de esta revision para un gerente no tecnico.
```

---

## 11. Instalar o ejecutar Azure MCP

El servidor MCP de Azure se puede ejecutar con npx.

Comando base:

```powershell
npx -y @azure/mcp@latest server start
```

En Copilot CLI, agregar o validar el servidor MCP segun el flujo disponible:

```text
/mcp
```

Validar servidores MCP configurados:

```text
/mcp list
```

---

## 12. Limpieza de recursos

Al finalizar la demo, ejecutar:

```powershell
.\scripts\99-cleanup.ps1
```

Validar si el grupo de recursos sigue existiendo:

```powershell
az group exists --name rg-demo-ai900-mcp
```

Si responde:

```text
false
```

La limpieza termino correctamente.

---

## 13. Flujo rapido para futuras clases

```powershell
cd C:\GithubOrden\training-delivery
git pull
cd .\courses\AI-900\demos\demo-azure-mcp-governance
.\scripts\01-create-resources.ps1
copilot
```

Al terminar:

```powershell
.\scripts\99-cleanup.ps1
```

---

## 14. Problemas comunes

### PowerShell no reconoce un comando

Cerrar y volver a abrir PowerShell.

Validar:

```powershell
git --version
gh --version
az version
node -v
npm -v
copilot --version
```

### No aparece la suscripcion correcta de Azure

Ejecutar:

```powershell
az account list --output table
az account set --subscription "NOMBRE_O_ID_DE_LA_SUSCRIPCION"
```

### Copilot CLI pide login

Ejecutar:

```powershell
copilot
```

Dentro de Copilot:

```text
/login
```

### Error de permisos en Azure

Validar que la cuenta tenga permisos para crear:

- Resource Groups
- Storage Accounts
- Virtual Networks

---

## 15. Mensaje pedagogico

Esta demo muestra que la IA generativa puede pasar de responder preguntas a trabajar con contexto real y herramientas reales.

El punto importante para AI-900 no es aprender administracion avanzada de Azure, sino entender que un agente puede:

- recibir una solicitud en lenguaje natural
- consultar un entorno real
- identificar informacion relevante
- explicar problemas
- generar una recomendacion

Siempre bajo permisos, supervision humana y buenas practicas de gobierno.