# Module 04 - Implement a Secure Continuous Deployment using Azure Pipelines

## Objetivo

Comprender cómo proteger procesos de despliegue continuo utilizando Azure Pipelines.

## Conceptos clave

- Secure Continuous Deployment
- Secrets
- Azure Key Vault
- Variable Groups
- Service Connections
- Feature Flags
- Dynamic Configuration
- Azure App Configuration
- Deployment Security

## Explicación sencilla

Una pipeline puede automatizar despliegues, pero no debería exponer:

- contraseñas
- connection strings
- tokens
- secretos
- credenciales

La automatización debe ser segura.

## Flujo seguro

Pipeline
? Identity
? Secret Store
? Deployment
? Application

## Azure Key Vault

Azure Key Vault permite almacenar información sensible.

Ejemplos:

- passwords
- API keys
- certificates
- connection strings
- secrets

La pipeline puede consumir esos valores sin escribirlos directamente en YAML.

## Variable Groups

Azure DevOps permite utilizar Variable Groups para centralizar variables utilizadas por pipelines.

También pueden integrarse con Azure Key Vault.

## Service Connections

Una Service Connection permite que Azure DevOps se autentique contra servicios externos.

Ejemplo:

Azure DevOps
? Service Connection
? Azure Subscription

## Feature Flags

Los Feature Flags permiten activar o desactivar funcionalidades sin realizar un nuevo despliegue completo.

Ejemplo:

Application deployed
? Feature disabled
? Validation
? Feature enabled

## Dynamic Configuration

La configuración puede mantenerse separada del código.

Esto permite cambiar comportamiento sin recompilar la aplicación.

## Ejemplo empresarial

Una empresa despliega una nueva funcionalidad.

La aplicación llega a producción, pero la funcionalidad permanece desactivada.

Luego:

- se habilita para usuarios internos
- se valida
- se habilita para un porcentaje de usuarios
- finalmente se habilita para todos

## Labs relacionados

- Lab 10: Integrate Azure Key Vault with Azure DevOps
- Lab 11: Enable Dynamic Configuration and Feature Flags

## Mensaje clave

Continuous Deployment debe combinar:

Automation
? Security
? Configuration
? Controlled Release
