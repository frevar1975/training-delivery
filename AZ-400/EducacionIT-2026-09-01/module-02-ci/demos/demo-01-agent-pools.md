# Demo 01 - Agent Pools

## Objetivo

Mostrar cómo Azure DevOps organiza los agentes que ejecutan los jobs de una pipeline.

## Concepto

Una pipeline define qué trabajo debe ejecutarse.

El agent es la máquina que ejecuta ese trabajo.

Un Agent Pool es un conjunto de agents disponibles para ejecutar jobs.

## Analogía

Podemos pensar en un taller:

- Pipeline = orden de trabajo
- Job = trabajo asignado
- Agent = técnico que realiza el trabajo
- Agent Pool = equipo de técnicos disponibles

## Demo

### 1. Abrir Azure DevOps

Ingresar al proyecto de Azure DevOps utilizado para la demostración.

### 2. Ir a Agent Pools

Ingresar a:

Organization settings
→ Agent pools

### 3. Mostrar los pools disponibles

Explicar que Azure DevOps puede trabajar con:

- Microsoft-hosted agents
- Self-hosted agents

### 4. Explicar Microsoft-hosted agents

Microsoft proporciona temporalmente la máquina que ejecuta el job.

Ejemplos:

- windows-latest
- ubuntu-latest
- macos-latest

### 5. Explicar self-hosted agents

La organización instala y administra su propio agent.

Casos comunes:

- acceso a servidores internos
- acceso a redes privadas
- herramientas especializadas
- software propietario
- compiladores específicos

## Comparación

| Microsoft-hosted | Self-hosted |
|---|---|
| Administrado por Microsoft | Administrado por la organización |
| Máquina temporal | Máquina persistente |
| Menor mantenimiento | Mayor control |
| Entorno limpio por ejecución | Puede conservar herramientas y caché |
| Ideal para escenarios estándar | Ideal para requerimientos especiales |

## Mensaje clave

La pipeline no ejecuta directamente el código.

La pipeline entrega un job a un agent disponible.

Pipeline
→ Agent Pool
→ Agent
→ Job

## Pregunta para los alumnos

¿En qué escenario utilizarían un self-hosted agent en lugar de un Microsoft-hosted agent?
