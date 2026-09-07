# Clase 03 - AZ-400

## EducaciónIT

Fecha: 2026-09-08

Horario Bolivia:

18:00 - 21:00

Duración:

3 horas

## Module 02

Implement CI with Azure Pipelines and GitHub Actions

## Foco de esta clase

- Azure Pipelines
- Pipeline architecture
- Agents
- Agent Pools
- Microsoft-hosted agents
- Self-hosted agents
- Pipeline styles
- Classic Pipelines
- YAML Pipelines
- Continuous Integration
- Triggers
- Build
- Test
- Artifacts

## Labs

- Lab 03 - Configure Agent Pools and Understand Pipeline Styles
- Lab 04 - Enable Continuous Integration with Azure Pipelines

---

# Objetivo de la clase

Al finalizar la sesión, los alumnos deberían poder explicar:

1. Qué es Azure Pipelines.
2. Qué ejecuta realmente una pipeline.
3. Qué es un Agent.
4. Qué es un Agent Pool.
5. Diferencia entre Microsoft-hosted y self-hosted agents.
6. Diferencia entre Classic Pipeline y YAML Pipeline.
7. Qué significa Continuous Integration.
8. Cómo un cambio en Git puede iniciar automáticamente una pipeline.

---

# 18:00 - 18:15

## Repaso de la clase anterior

Partimos del flujo visto previamente:

Developer
? Branch
? Code
? Commit
? Push
? Pull Request
? Merge

Pregunta para los alumnos:

¿Qué debería ocurrir después de que un desarrollador hace push?

Respuesta conceptual:

No queremos depender de que una persona ejecute manualmente:

- compilación
- pruebas
- validaciones
- generación de artefactos

Ahí aparece Continuous Integration.

Nuevo flujo:

Developer
? Git
? Push
? Pipeline
? Build
? Test
? Artifact

## Analogía

Un repositorio es como una cocina que recibe ingredientes.

La pipeline es la línea de producción.

Cada vez que llega una nueva versión de la receta, la línea puede:

- preparar
- revisar
- probar
- empaquetar

automáticamente.

---

# 18:15 - 18:40

## Arquitectura de Azure Pipelines

Explicar:

Pipeline
? Stage
? Job
? Step

Un Step puede utilizar:

- Script
- Task

## Pipeline

Representa todo el proceso de automatización.

Ejemplo:

Build Application

## Stage

Representa una fase lógica.

Ejemplo:

Build

Test

Deploy

## Job

Agrupa pasos que se ejecutan sobre un Agent.

Ejemplo:

BuildJob

## Step

Unidad concreta de trabajo.

Ejemplo:

dotnet build

## Task

Componente preconstruido de Azure DevOps.

Ejemplo conceptual:

Publish Build Artifacts

## Diagrama

Pipeline

? Stage: Build

   ? Job: BuildApplication

      ? Checkout

      ? Restore

      ? Build

      ? Test

      ? Publish

## Pregunta para clase

¿Dónde se ejecutan realmente estos comandos?

Respuesta:

En un Agent.

---

# 18:40 - 19:10

## Agents

Un Agent es la máquina que ejecuta los Jobs de una pipeline.

Flujo:

Pipeline
? Job
? Agent
? Commands

El Agent puede ejecutar:

- scripts
- compiladores
- tests
- Docker
- Azure CLI
- PowerShell
- herramientas de desarrollo

## Analogía

Azure DevOps es el jefe de producción.

La Pipeline es la orden de trabajo.

El Agent es el trabajador que realmente ejecuta esa orden.

Sin Agent:

la pipeline tiene instrucciones, pero nadie las ejecuta.

---

# Microsoft-hosted Agent

Microsoft proporciona la máquina temporalmente.

Ejemplos:

- windows-latest
- ubuntu-latest
- macos-latest

## Ventajas

- no administramos servidores
- entorno limpio
- mantenimiento Microsoft
- rápido de utilizar
- útil para escenarios comunes

## Limitaciones

- máquina temporal
- configuración limitada
- software especial puede no estar instalado
- cada ejecución puede utilizar una máquina diferente

---

# Self-hosted Agent

La organización administra la máquina.

Puede ser:

- VM
- servidor físico
- máquina on-premises
- recurso dentro de una red privada

## Ventajas

- control total
- herramientas personalizadas
- acceso a redes privadas
- cache persistente
- software específico

## Desventajas

La organización debe administrar:

- sistema operativo
- actualizaciones
- seguridad
- herramientas
- capacidad
- disponibilidad

---

# Comparación

Microsoft-hosted

Azure DevOps
? Microsoft Agent
? Execute
? Destroy

Self-hosted

Azure DevOps
? My Agent
? Execute
? Remains Available

## Ejemplo real

Aplicación pública sencilla:

Microsoft-hosted agent.

Sistema empresarial que necesita acceder a:

SQL Server interno
o
servidor on-premises

probablemente:

Self-hosted agent.

---

# Agent Pools

Un Agent Pool es un conjunto lógico de Agents.

Pipeline
? Agent Pool
? Agent

Ejemplo:

ProductionAgents

? Agent01
? Agent02
? Agent03

## ¿Por qué Pool?

Azure DevOps puede seleccionar un Agent disponible dentro del grupo.

Esto permite:

- organización
- capacidad
- escalabilidad
- separación de workloads

---

# 19:10 - 19:25

# DEMO 1 - Agent Pools

## Objetivo

Mostrar visualmente dónde viven los Agents que ejecutan pipelines.

## Azure DevOps

Ingresar a:

Project Settings

? Agent pools

Mostrar los pools disponibles.

Explicar:

Aquí no estamos creando todavía una pipeline.

Estamos viendo la infraestructura que puede ejecutarla.

## Mostrar

- Pool
- Agents
- Status
- Capabilities cuando corresponda

## Pregunta

Si tenemos tres Agents dentro del pool y uno está ocupado:

¿Qué podría hacer Azure DevOps?

Utilizar otro Agent disponible.

---

# 19:25 - 19:35

## Pausa y preguntas

Preguntas rápidas:

¿Qué ejecuta un Job?

Agent.

¿Qué agrupa Agents?

Agent Pool.

¿Quién administra un Microsoft-hosted agent?

Microsoft.

¿Quién administra un self-hosted agent?

La organización.

---

# 19:35 - 20:00

# Pipeline Styles

Azure DevOps permite diferentes formas de definir pipelines.

## Classic Pipeline

Configuración principalmente mediante interfaz gráfica.

Conceptualmente:

Azure DevOps UI
? Tasks
? Configuration
? Pipeline

## Ventaja

Fácil de visualizar inicialmente.

## Problema

La definición no vive naturalmente junto al código.

---

# YAML Pipeline

La definición de la pipeline se almacena como código.

Ejemplo:

azure-pipelines.yml

Repository

? Application Code
? Pipeline Code

## Ejemplo YAML

trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:

- script: echo Building application
  displayName: Build

- script: echo Running tests
  displayName: Test

## Concepto importante

Pipeline as Code.

La pipeline:

- puede versionarse
- puede revisarse
- puede pasar por Pull Request
- tiene historial
- puede reutilizarse

## Analogía

Classic Pipeline:

configurar una máquina usando botones.

YAML:

guardar las instrucciones de configuración como receta dentro del proyecto.

---

# 20:00 - 20:20

# Continuous Integration

Continuous Integration significa integrar cambios frecuentemente y validarlos automáticamente.

## Flujo

Developer

? Commit

? Push

? Trigger

? Pipeline

? Build

? Test

? Result

## Trigger

El Trigger determina cuándo se ejecuta la pipeline.

Ejemplo:

trigger:
- main

Significa:

cuando cambia main

? ejecutar pipeline

## CI no significa únicamente compilar

Una pipeline CI puede realizar:

- restore dependencies
- build
- unit tests
- static analysis
- security checks
- packaging
- artifact generation

## Resultado

Si todo está correcto:

Build Successful

Si algo falla:

Build Failed

El desarrollador obtiene feedback rápidamente.

---

# Artifact

Después de construir una aplicación podemos generar un Artifact.

Ejemplo:

Source Code

? Build

? Application.zip

Ese archivo puede utilizarse posteriormente durante deployment.

## Diferencia importante

CI:

Code
? Build
? Test
? Artifact

CD:

Artifact
? Environment
? Deployment

No mezclar ambos conceptos.

---

# 20:20 - 20:35

# DEMO 2 - Azure Pipeline YAML

## Objetivo

Mostrar una pipeline sencilla y explicar cada parte.

Ir a:

Azure DevOps

? Pipelines

? Pipelines

Mostrar o crear una pipeline.

Revisar:

azure-pipelines.yml

## Explicar

trigger

Define qué evento inicia la pipeline.

pool

Define dónde se ejecutará.

steps

Define qué debe realizar el Agent.

## Ejemplo

trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:

- script: echo "Build"
  displayName: Build application

- script: echo "Test"
  displayName: Run tests

## Ejecutar

Run pipeline

Mostrar:

Pipeline

? Job

? Agent

? Steps

? Logs

---

# 20:35 - 20:50

# DEMO 3 - Continuous Integration Trigger

## Objetivo

Demostrar que no necesitamos presionar Run Pipeline manualmente.

Modificar un archivo del repositorio.

Ejemplo:

README.md

Luego:

git add .

git commit -m "Trigger CI pipeline"

git push

Ir inmediatamente a:

Azure DevOps

? Pipelines

Mostrar que aparece una nueva ejecución.

## Explicación

No fue Azure DevOps quien detectó mágicamente el código.

El flujo fue:

Git Push

? Repository Event

? Trigger

? Pipeline

? Agent

? Build

? Result

Esto es Continuous Integration.

---

# 20:50 - 21:00

# Relación con los laboratorios

## Lab 03

Configure Agent Pools and Understand Pipeline Styles

Los alumnos deben prestar atención a:

- Agent
- Agent Pool
- hosted agents
- self-hosted agents
- Classic
- YAML

## Lab 04

Enable Continuous Integration with Azure Pipelines

Los alumnos deben identificar:

- Pipeline
- Trigger
- Build
- Agent
- Job
- Steps
- Logs
- CI execution

---

# Preguntas finales

1. ¿Quién ejecuta realmente los comandos de una pipeline?

Agent.

2. ¿Qué es un Agent Pool?

Un grupo lógico de Agents.

3. ¿Qué ventaja tiene YAML?

Pipeline as Code.

4. ¿Qué inicia automáticamente una pipeline CI?

Un Trigger.

5. ¿Qué ocurre después de un push?

Repository Event
? Trigger
? Pipeline

6. ¿Qué diferencia existe entre CI y CD?

CI valida y construye cambios.

CD entrega o despliega los resultados.

---

# Mapa conceptual final

Developer

? Git

? Commit

? Push

? Trigger

? Azure Pipeline

? Agent Pool

? Agent

? Job

? Steps

? Build

? Test

? Artifact

? Feedback

---

# Mensaje de cierre

Una Pipeline no ejecuta el trabajo por sí misma.

La Pipeline define qué hacer.

El Agent ejecuta el trabajo.

El Trigger decide cuándo comenzar.

CI conecta esos tres conceptos para validar automáticamente cada cambio.
