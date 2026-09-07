
# Lab 03 - Configure Agent Pools and Understand Pipeline Styles

## Objetivo

Configurar y comprender el uso de Agent Pools en Azure DevOps y comparar diferentes estilos de pipelines.

## Relación con el módulo

Este laboratorio corresponde a:

Module 02 - Implement CI with Azure Pipelines and GitHub Actions

Conceptos relacionados:

- Agent Pools
- Microsoft-hosted agents
- Self-hosted agents
- Jobs
- Pipeline styles
- YAML
- Pipeline as Code

## Escenario

Una organización necesita automatizar procesos de integración continua.

El equipo debe decidir:

- qué tipo de agent utilizar
- dónde ejecutar los jobs
- cómo definir la pipeline
- cuándo utilizar YAML

## Parte 1 - Revisar Agent Pools

### 1. Ingresar a Azure DevOps

Abrir la organización y proyecto utilizado para el laboratorio.

### 2. Abrir Agent Pools

Ir a:

Organization settings
→ Agent pools

### 3. Revisar los pools disponibles

Identificar los pools configurados en la organización.

Explicar que un Agent Pool agrupa uno o más agents.

## Parte 2 - Microsoft-hosted Agents

Revisar el uso de imágenes proporcionadas por Microsoft.

Ejemplos:

- ubuntu-latest
- windows-latest
- macos-latest

Ejemplo YAML:

pool:
  vmImage: ubuntu-latest

## Parte 3 - Self-hosted Agents

Explicar que una organización puede registrar sus propias máquinas como agents.

Casos comunes:

- redes privadas
- herramientas internas
- software especializado
- compiladores específicos
- dependencias preinstaladas

## Parte 4 - Comprender el flujo de ejecución

Pipeline
→ Agent Pool
→ Agent
→ Job
→ Steps

La pipeline define el trabajo.

El pool proporciona agents.

El agent ejecuta el job.

## Parte 5 - Pipeline Styles

Comparar:

### Pipeline visual

Configurada desde la interfaz de Azure DevOps.

### YAML Pipeline

Configurada mediante un archivo almacenado en el repositorio.

Ejemplo:

trigger:

- main

pool:
  vmImage: ubuntu-latest

steps:

- script: echo "Pipeline ejecutada"
  displayName: "Demo"

## Comparación

| Visual                           | YAML                         |
| -------------------------------- | ---------------------------- |
| Configuración mediante interfaz | Pipeline as Code             |
| Fácil para comenzar             | Versionable con Git          |
| Menor portabilidad               | Mayor portabilidad           |
| Cambios desde el portal          | Cambios mediante commits     |
| Útil para escenarios simples    | Adecuado para DevOps moderno |

## Validación

Al finalizar el laboratorio, comprobar que el alumno puede explicar:

- qué es un Agent
- qué es un Agent Pool
- diferencia entre Microsoft-hosted y self-hosted
- qué es un Job
- diferencia entre pipeline visual y YAML
- por qué YAML se considera Pipeline as Code

## Preguntas de cierre

1. ¿Qué ventaja tiene un Microsoft-hosted agent?
2. ¿Cuándo sería necesario un self-hosted agent?
3. ¿Por qué guardar una pipeline YAML en Git?
4. ¿Qué relación existe entre un Agent Pool y un Job?

## Referencia oficial

Microsoft Learn AZ-400:
Configure agent pools and understand pipeline styles.
