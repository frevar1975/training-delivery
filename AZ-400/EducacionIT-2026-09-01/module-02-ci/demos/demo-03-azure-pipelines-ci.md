# Demo 03 - Azure Pipelines CI

## Objetivo

Crear y explicar una pipeline básica de Continuous Integration en Azure Pipelines.

## Escenario

Tenemos una aplicación almacenada en un repositorio.

Queremos que cada cambio enviado a la rama main ejecute automáticamente un proceso de integración continua.

## Flujo

Developer
→ Commit
→ Push
→ Repository
→ Trigger
→ Azure Pipeline
→ Agent
→ Build
→ Test
→ Resultado

## Demo

### 1. Abrir Azure DevOps

Ingresar al proyecto utilizado para la demostración.

### 2. Ir a Pipelines

Ingresar a:

Pipelines
→ Pipelines

### 3. Crear una nueva pipeline

Seleccionar:

New pipeline

### 4. Seleccionar el repositorio

Elegir el repositorio que contiene la aplicación.

### 5. Configurar la pipeline

Crear o utilizar un archivo:

azure-pipelines.yml

### 6. Revisar el trigger

Ejemplo:

trigger:
- main

Esto indica que los cambios realizados sobre main pueden iniciar automáticamente la pipeline.

### 7. Seleccionar el agent

Ejemplo:

pool:
  vmImage: ubuntu-latest

La pipeline utilizará un Microsoft-hosted agent basado en Ubuntu.

### 8. Agregar steps

Ejemplo:

steps:

- script: echo "Iniciando build"
  displayName: "Build"

- script: echo "Ejecutando tests"
  displayName: "Test"

### 9. Guardar y ejecutar

Seleccionar:

Save and run

Observar cómo Azure DevOps crea una ejecución de la pipeline.

### 10. Revisar el resultado

Mostrar:

- Run
- Job
- Agent
- Steps
- Logs
- Status

## Qué explicar durante la ejecución

La pipeline contiene la definición del proceso.

El Agent Pool proporciona capacidad de ejecución.

El Agent ejecuta el Job.

El Job contiene los Steps.

Cada Step ejecuta una Task o un Script.

## Jerarquía

Pipeline
→ Stage
→ Job
→ Step
→ Task / Script

## Resultado esperado

El alumno debe poder relacionar:

Push
→ Trigger
→ Pipeline Run
→ Agent
→ Job
→ Steps
→ Resultado

## Mensaje clave

Continuous Integration no significa solamente compilar código.

CI busca validar continuamente los cambios para detectar problemas lo antes posible.

## Pregunta para los alumnos

¿Qué ocurriría si uno de los tests devuelve un error durante la ejecución de la pipeline?
