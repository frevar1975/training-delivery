# Lab 05 - Implement GitHub Actions for CI/CD

## Objetivo

Implementar un workflow de CI/CD utilizando GitHub Actions y comprender su relación con los eventos del repositorio.

## Relación con el módulo

Module 02 - Implement CI with Azure Pipelines and GitHub Actions

## Conceptos relacionados

- GitHub Actions
- Workflows
- Events
- Jobs
- Steps
- Actions
- Runners
- YAML
- Continuous Integration
- Continuous Delivery

## Escenario

Una aplicación se encuentra almacenada en GitHub.

Queremos automatizar validaciones cuando los desarrolladores realizan cambios sobre el repositorio.

## Flujo

Developer
? Commit
? Push
? GitHub Repository
? Event
? Workflow
? Runner
? Job
? Steps

## Parte 1 - Abrir GitHub Actions

Ingresar al repositorio.

Seleccionar:

Actions

## Parte 2 - Crear Workflow

Los workflows se almacenan en:

.github/workflows/

Ejemplo:

.github/workflows/ci.yml

## Parte 3 - Definir el evento

Ejemplo:

on:
  push:
    branches:
      - main

Esto permite ejecutar el workflow cuando existe un push sobre main.

## Parte 4 - Crear Job

Ejemplo:

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

    - uses: actions/checkout@v4

    - name: Build
      run: echo "Building application"

    - name: Test
      run: echo "Running tests"

## Parte 5 - Comprender Runner

El runner es la máquina que ejecuta el Job.

Ejemplos:

- ubuntu-latest
- windows-latest
- macos-latest

## Parte 6 - Ejecutar Workflow

Realizar un cambio en el repositorio.

Crear:

git add .
git commit -m "Test GitHub Actions workflow"
git push

## Parte 7 - Revisar ejecución

En GitHub:

Actions
? Workflow
? Run

Revisar:

- Event
- Job
- Steps
- Logs
- Status

## Azure Pipelines vs GitHub Actions

Azure Pipelines:

Repository
? Pipeline
? Agent
? Job
? Steps

GitHub Actions:

Repository
? Workflow
? Runner
? Job
? Steps

Los conceptos son similares aunque utilizan terminología diferente.

## Parte 8 - CI/CD

GitHub Actions también puede utilizarse para:

- build
- tests
- packages
- containers
- deployments
- Azure deployments

## Validación

Al finalizar, el alumno debe poder explicar:

- qué es un Workflow
- qué inicia un Workflow
- qué es un Runner
- qué es un Job
- qué contiene un Step
- dónde se almacenan los workflows
- relación entre GitHub Actions y CI/CD

## Preguntas de cierre

1. ¿Qué diferencia existe entre Workflow y Job?
2. ¿Qué función cumple un Runner?
3. ¿Qué evento puede iniciar un Workflow?
4. ¿Qué similitud existe entre un Azure Pipelines Agent y un GitHub Runner?

## Mensaje clave

GitHub Actions permite convertir eventos del repositorio en procesos automáticos.

Code
? Event
? Workflow
? Validation
? Feedback

## Referencia oficial

Microsoft Learn AZ-400:
Implement GitHub Actions for CI/CD.
