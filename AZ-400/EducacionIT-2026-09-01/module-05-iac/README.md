# Module 05 - Manage Infrastructure as Code using Azure and DSC

## Objetivo

Comprender cómo administrar infraestructura mediante código utilizando Azure y técnicas de Infrastructure as Code.

## Conceptos clave

- Infrastructure as Code
- Declarative Infrastructure
- Azure Bicep
- ARM Templates
- Version Control
- Repeatable Deployments
- Idempotency
- Configuration Management

## Explicación sencilla

Infrastructure as Code permite definir infraestructura utilizando archivos de texto versionables.

En lugar de crear recursos manualmente desde el portal, podemos describir el estado deseado.

## Analogía

En lugar de construir una casa improvisando cada vez, utilizamos planos.

El archivo de infraestructura es el plano.

La plataforma interpreta el plano y crea los recursos.

## Beneficios

- repetibilidad
- automatización
- trazabilidad
- versionado
- consistencia
- menor error manual
- recuperación más rápida

## Enfoque declarativo

Declaramos qué infraestructura queremos.

Ejemplo conceptual:

Quiero:

- Resource Group
- Storage Account
- App Service
- Database

La plataforma determina cómo alcanzar ese estado.

## Azure Bicep

Bicep es un lenguaje declarativo para desplegar recursos en Azure.

Permite definir:

- recursos
- parámetros
- variables
- outputs
- dependencias
- módulos

## Ejemplo conceptual

resource storage 'Microsoft.Storage/storageAccounts@...' = {
  name: 'mystorage'
  location: resourceGroup().location
}

## Parámetros

Permiten reutilizar una plantilla para diferentes entornos.

Ejemplo:

Development
Testing
Production

## Version Control

Los archivos Bicep pueden almacenarse en Git.

Esto permite:

- revisar cambios
- utilizar pull requests
- mantener historial
- integrar infraestructura con pipelines

## Integración con CI/CD

Repository
? Bicep
? Pipeline
? Azure
? Infrastructure

## Idempotencia

Ejecutar nuevamente una plantilla no debería crear recursos duplicados si el estado deseado ya existe.

## Lab relacionado

- Lab 12: Deployments using Azure Bicep templates

## Mensaje clave

Infrastructure as Code convierte la infraestructura en un activo:

- reproducible
- versionable
- automatizable
- auditable
