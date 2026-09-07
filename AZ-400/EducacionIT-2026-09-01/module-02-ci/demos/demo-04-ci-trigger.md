# Demo 04 - CI Trigger

## Objetivo

Mostrar cómo una pipeline puede iniciarse automáticamente cuando cambia el código en el repositorio.

## Concepto

Un trigger define qué evento inicia una pipeline.

En Continuous Integration, uno de los triggers más comunes es un push sobre una rama.

## Ejemplo básico

trigger:
- main

Esto indica que los cambios enviados a la rama main pueden iniciar la pipeline.

## Escenario

Developer
→ modifica código
→ commit
→ push a main
→ trigger
→ pipeline automática

## Demo

### 1. Abrir el archivo YAML

Abrir:

azure-pipelines.yml

### 2. Revisar el trigger

Mostrar:

trigger:
- main

Explicar que la rama main está configurada para iniciar automáticamente la pipeline.

### 3. Realizar un cambio

Modificar un archivo sencillo del repositorio.

Por ejemplo:

README.md

### 4. Crear commit

Ejemplo:

git add .
git commit -m "Update application documentation"

### 5. Hacer push

Ejecutar:

git push

### 6. Revisar Azure DevOps

Ir a:

Pipelines
→ Pipelines
→ Runs

Mostrar que se creó una nueva ejecución automáticamente.

### 7. Revisar el motivo de ejecución

Explicar que el pipeline run fue iniciado por un cambio en el repositorio.

## Ejemplo con varias ramas

trigger:
  branches:
    include:
    - main
    - develop

Esto permite iniciar la pipeline para más de una rama.

## Exclusiones

También se pueden excluir ramas.

Ejemplo:

trigger:
  branches:
    include:
    - main
    exclude:
    - experimental

## Idea clave

El trigger conecta el repositorio con la automatización.

Repository
→ Event
→ Trigger
→ Pipeline

## Continuous Integration

Sin trigger automático:

Developer
→ cambio
→ ejecución manual

Con trigger automático:

Developer
→ cambio
→ push
→ pipeline automática
→ validación inmediata

## Qué mostrar a los alumnos

Durante la demo señalar:

- rama que cambia
- commit generado
- push
- nuevo pipeline run
- estado del job
- resultado final

## Mensaje clave

Una pipeline CI debe reaccionar automáticamente a los cambios relevantes del código.

El trigger es el mecanismo que inicia esa automatización.

## Pregunta para los alumnos

¿Qué problemas podríamos tener si una pipeline se ejecutara automáticamente para absolutamente todas las ramas y todos los cambios?
