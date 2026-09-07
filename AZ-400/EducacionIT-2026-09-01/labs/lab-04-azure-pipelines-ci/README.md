# Lab 04 - Enable Continuous Integration with Azure Pipelines

## Objetivo

Implementar Continuous Integration utilizando Azure Pipelines y comprobar cómo los cambios realizados en un repositorio pueden iniciar automáticamente una pipeline.

## Relación con el módulo

Este laboratorio corresponde a:

Module 02 - Implement CI with Azure Pipelines and GitHub Actions

Conceptos relacionados:

- Continuous Integration
- Azure Pipelines
- YAML
- Triggers
- Agents
- Jobs
- Steps
- Build
- Tests
- Pipeline Runs

## Escenario

Un equipo de desarrollo almacena su aplicación en un repositorio Git.

Cada vez que se realizan cambios relevantes sobre la rama principal, se quiere ejecutar automáticamente un proceso que valide el código.

Flujo esperado:

Developer
→ Commit
→ Push
→ Repository
→ Trigger
→ Azure Pipeline
→ Agent
→ Build / Test
→ Resultado

## Parte 1 - Abrir Azure Pipelines

Ingresar al proyecto de Azure DevOps.

Ir a:

Pipelines
→ Pipelines

## Parte 2 - Crear una Pipeline

Seleccionar:

New pipeline

Elegir el repositorio que contiene la aplicación.

## Parte 3 - Configurar YAML

Crear o utilizar:

azure-pipelines.yml

Ejemplo básico:

trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:

- script: echo "Iniciando proceso de CI"
  displayName: "Start CI"

- script: echo "Ejecutando build"
  displayName: "Build"

- script: echo "Ejecutando tests"
  displayName: "Test"

## Parte 4 - Analizar la Pipeline

Identificar:

- Trigger
- Pool
- Agent
- Job
- Steps
- Scripts

Explicar la relación:

Pipeline
→ Job
→ Steps
→ Tasks / Scripts

## Parte 5 - Ejecutar la Pipeline

Seleccionar:

Save and run

Observar:

- Pipeline Run
- Job
- Agent
- Steps
- Logs
- Status

## Parte 6 - Probar Continuous Integration

Realizar un cambio sencillo en el repositorio.

Por ejemplo:

README.md

Crear un commit y realizar push.

Ejemplo:

git add .
git commit -m "Test CI pipeline"
git push

## Parte 7 - Comprobar el Trigger

Volver a:

Pipelines
→ Pipelines
→ Runs

Comprobar que se inició una nueva ejecución automáticamente.

## Parte 8 - Analizar los Logs

Abrir el Pipeline Run.

Revisar:

- Agent utilizado
- Job ejecutado
- Steps
- duración
- logs
- resultado

## Validación

Al finalizar, el alumno debe poder explicar:

- qué es Continuous Integration
- qué evento inicia la pipeline
- qué función cumple el trigger
- dónde se ejecuta el job
- qué función cumple el agent
- qué contiene un step
- dónde revisar errores de una ejecución

## Preguntas de cierre

1. ¿Qué provoca una nueva ejecución de CI?
2. ¿Qué ocurre si falla uno de los steps?
3. ¿Dónde podemos investigar el motivo de un fallo?
4. ¿Qué ventaja obtenemos al ejecutar estas validaciones automáticamente?

## Mensaje clave

Continuous Integration crea un ciclo automático de validación:

Code
→ Commit
→ Pipeline
→ Build
→ Test
→ Feedback

El objetivo es detectar problemas lo antes posible.

## Referencia oficial

Microsoft Learn AZ-400:
Enable Continuous Integration with Azure Pipelines.
