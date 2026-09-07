# Lab 12 - Deployments using Azure Bicep Templates

## Objetivo

Desplegar infraestructura en Azure utilizando plantillas Bicep y comprender el enfoque Infrastructure as Code.

## Relación con el módulo

Module 05 - Manage Infrastructure as Code using Azure and DSC

## Conceptos relacionados

- Infrastructure as Code
- Azure Bicep
- Declarative Infrastructure
- Parameters
- Resources
- Outputs
- Azure CLI
- Deployment Automation

## Escenario

La organización necesita crear infraestructura de forma repetible.

En lugar de crear recursos manualmente desde Azure Portal, se utilizará Bicep.

## Flujo

Bicep File
? Validation
? Deployment
? Azure Resource Manager
? Azure Resources

## Parte 1 - Revisar Bicep

Abrir el archivo:

main.bicep

Identificar sus componentes.

## Parte 2 - Revisar parámetros

Ejemplo:

param location string = resourceGroup().location

Los parámetros permiten adaptar la plantilla sin modificar su estructura principal.

## Parte 3 - Definir un recurso

Ejemplo conceptual:

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'storageexample'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

## Parte 4 - Validar la plantilla

Utilizar herramientas como Azure CLI para validar el deployment.

## Parte 5 - Realizar Deployment

Ejemplo conceptual:

az deployment group create

Indicando:

- Resource Group
- Bicep file
- Parameters

## Parte 6 - Revisar Azure

Ingresar a Azure Portal.

Comprobar que los recursos fueron creados.

## Parte 7 - Modificar infraestructura

Cambiar una propiedad declarada en Bicep.

Ejecutar nuevamente el deployment.

Analizar cómo Azure actualiza el estado existente.

## Parte 8 - Versionar infraestructura

Guardar el archivo Bicep en Git.

Flujo:

Change
? Commit
? Pull Request
? Pipeline
? Deployment

## Validación

Al finalizar, el alumno debe poder explicar:

- qué significa Infrastructure as Code
- qué es Bicep
- diferencia entre enfoque manual y declarativo
- función de parámetros
- por qué versionar infraestructura
- cómo integrar Bicep con pipelines

## Preguntas de cierre

1. ¿Qué problema resuelve Infrastructure as Code?
2. ¿Qué ventaja tiene utilizar Bicep frente a crear recursos manualmente?
3. ¿Por qué almacenar plantillas en Git?
4. ¿Qué ocurre al ejecutar nuevamente una plantilla declarativa?

## Mensaje clave

La infraestructura debe poder reconstruirse utilizando código.

Code
? Deployment
? Infrastructure

## Referencia oficial

Microsoft Learn AZ-400:
Deployments using Azure Bicep templates.
