# Lab 10 - Integrate Azure Key Vault with Azure DevOps

## Objetivo

Integrar Azure Key Vault con Azure DevOps para utilizar secretos de forma segura dentro de pipelines.

## Relación con el módulo

Module 04 - Implement a Secure Continuous Deployment using Azure Pipelines

## Conceptos relacionados

- Azure Key Vault
- Secrets
- Variable Groups
- Service Connections
- Secure Pipelines
- Secret Management

## Escenario

Una aplicación necesita utilizar credenciales durante el proceso de despliegue.

Estas credenciales no deben almacenarse directamente en:

- código
- YAML
- repositorios
- scripts

## Flujo

Azure Pipeline
? Service Connection
? Azure Key Vault
? Secret
? Deployment

## Parte 1 - Crear o revisar Key Vault

Ingresar a Azure Portal.

Localizar:

Key Vaults

Seleccionar el Key Vault utilizado para el laboratorio.

## Parte 2 - Revisar Secrets

Ingresar a:

Objects
? Secrets

Identificar los secretos almacenados.

## Parte 3 - Configurar acceso

Asegurar que la identidad utilizada por Azure DevOps tenga permisos para acceder a los secretos necesarios.

## Parte 4 - Abrir Azure DevOps

Ingresar al proyecto.

Ir a:

Pipelines
? Library

## Parte 5 - Crear Variable Group

Crear un Variable Group.

Configurar integración con Azure Key Vault.

Seleccionar:

- Azure subscription
- Key Vault
- Secrets

## Parte 6 - Consumir el secreto

Utilizar la variable desde la pipeline.

Ejemplo conceptual:

variables:
- group: secure-variables

## Parte 7 - Ejecutar pipeline

Ejecutar la pipeline.

Comprobar que los valores sensibles no aparecen expuestos en logs.

## Validación

Al finalizar el laboratorio, el alumno debe poder explicar:

- por qué no guardar secretos en YAML
- función de Azure Key Vault
- función de una Service Connection
- relación entre Variable Groups y Key Vault
- cómo una pipeline consume secretos

## Preguntas de cierre

1. ¿Qué riesgo existe si almacenamos una contraseña directamente en Git?
2. ¿Qué ventaja proporciona Key Vault?
3. ¿Debe una pipeline mostrar secretos en los logs?
4. ¿Qué función cumple una Service Connection?

## Mensaje clave

Los secretos deben administrarse fuera del código y recuperarse de forma segura durante la ejecución.

## Referencia oficial

Microsoft Learn AZ-400:
Integrate Azure Key Vault with Azure DevOps.
