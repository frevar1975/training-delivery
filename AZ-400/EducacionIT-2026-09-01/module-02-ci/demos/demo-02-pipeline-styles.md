# Demo 02 - Pipeline Styles

## Objetivo

Mostrar las diferentes formas de definir una pipeline en Azure DevOps y explicar cuándo utilizar cada enfoque.

## Concepto

Una pipeline describe los pasos necesarios para automatizar procesos como:

- Build
- Test
- Package
- Publish
- Deploy

Azure DevOps permite definir pipelines principalmente mediante:

- interfaz visual
- YAML

## Analogía

Una pipeline es como una receta.

### Pipeline visual

La receta se configura mediante formularios y opciones en una interfaz.

### Pipeline YAML

La receta está escrita en un archivo que puede almacenarse junto con el código.

## Demo

### 1. Abrir Azure DevOps

Ingresar al proyecto utilizado para la demostración.

### 2. Ir a Pipelines

Ingresar a:

Pipelines
→ Pipelines

### 3. Mostrar una pipeline

Explicar sus componentes principales:

Repository
→ Trigger
→ Stage
→ Job
→ Task

### 4. Mostrar YAML

Ejemplo:

trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- script: echo "Build iniciado"
  displayName: "Build"

### 5. Explicar Pipeline as Code

El archivo YAML puede almacenarse dentro del repositorio.

Esto permite:

- versionar la pipeline
- revisar cambios
- utilizar pull requests
- reutilizar configuraciones
- mantener código y automatización juntos

## Comparación

| Visual | YAML |
|---|---|
| Configuración mediante interfaz | Configuración como código |
| Fácil para comenzar | Ideal para automatización |
| Cambios realizados desde el portal | Cambios versionados con Git |
| Menor portabilidad | Mayor portabilidad |
| Útil para escenarios simples | Recomendado para DevOps moderno |

## Mensaje clave

Con YAML, la definición de la pipeline se convierte en parte del repositorio.

Code
→ Git
→ YAML Pipeline
→ Agent
→ Build/Test
→ Artifact

## Pregunta para los alumnos

¿Qué ventaja tiene guardar la definición de una pipeline en el mismo repositorio que el código?
