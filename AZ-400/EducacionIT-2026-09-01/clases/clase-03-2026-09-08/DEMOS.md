# Demos - Clase 03

## Demo 01 - Agent Pools

Ruta:

Azure DevOps
? Project Settings
? Agent pools

Mostrar:

- Agent Pools
- Agents
- estado
- hosted vs self-hosted

Objetivo:

Entender quién ejecuta un Job.

---

## Demo 02 - Pipeline YAML

Ruta:

Azure DevOps
? Pipelines
? Pipelines

Mostrar:

- azure-pipelines.yml
- trigger
- pool
- steps
- jobs
- logs

Ejecutar:

Run pipeline

Objetivo:

Entender cómo una definición YAML se convierte en una ejecución real.

---

## Demo 03 - CI Trigger

Modificar README.md.

Ejecutar:

git add .

git commit -m "Trigger CI pipeline"

git push

Luego:

Azure DevOps
? Pipelines

Mostrar la ejecución automática.

Objetivo:

Visualizar Continuous Integration.

---

## Demo 04 - Logs

Abrir una ejecución.

Recorrer:

Pipeline
? Job
? Steps
? Logs

Mostrar:

- agent initialization
- checkout
- scripts
- status
- duración

Objetivo:

Enseñar dónde investigar cuando una pipeline falla.

---

# Backup Demo

Si algún laboratorio o servicio falla durante la sesión:

utilizar una pipeline mínima:

trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:

- script: echo "AZ-400 CI Demo"
  displayName: Demo Build

- script: echo "Tests OK"
  displayName: Demo Tests
