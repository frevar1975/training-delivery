# Lab 07 - Configure Pipelines as Code with YAML

## Objetivo

Configurar una pipeline utilizando YAML y comprender el concepto de Pipeline as Code.

## Relación con el módulo

Module 03 - Design and Implement a Release Strategy

## Conceptos relacionados

- YAML
- Pipeline as Code
- Trigger
- Pool
- Stages
- Jobs
- Steps
- Tasks

## Escenario

El equipo desea almacenar la definición de la pipeline dentro del repositorio.

## Parte 1 - Crear el archivo YAML

Crear:

azure-pipelines.yml

## Parte 2 - Definir el trigger

Ejemplo:

trigger:
- main

## Parte 3 - Seleccionar el agent

Ejemplo:

pool:
  vmImage: ubuntu-latest

## Parte 4 - Crear Steps

Ejemplo:

steps:

- script: echo "Build"
  displayName: "Build"

- script: echo "Test"
  displayName: "Test"

## Parte 5 - Incorporar Stages

Ejemplo conceptual:

Build
→ Test
→ Deploy

## Parte 6 - Ejecutar la pipeline

Realizar:

Save and run

Revisar:

- pipeline run
- stages
- jobs
- steps
- logs

## Validación

El alumno debe poder explicar:

- qué significa Pipeline as Code
- por qué YAML puede versionarse
- diferencia entre Stage, Job y Step
- relación entre repositorio y pipeline

## Preguntas de cierre

1. ¿Qué ventaja tiene guardar la pipeline en Git?
2. ¿Qué ocurre si modificamos el YAML?
3. ¿Por qué dividir una pipeline en stages?

## Referencia oficial

Microsoft Learn AZ-400:
Configure Pipelines as Code with YAML.
