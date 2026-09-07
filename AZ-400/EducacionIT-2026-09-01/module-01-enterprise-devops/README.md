# Module 01 - Implement Development for Enterprise DevOps

## Objetivo

Comprender cómo organizar el trabajo de desarrollo empresarial utilizando Azure Boards y Azure Repos.

## Conceptos clave

- Agile Planning
- Backlogs
- Epics
- Features
- User Stories
- Tasks
- Bugs
- Sprints
- Git
- Branches
- Commits
- Pull Requests
- Azure Repos
- Version Control

## Explicación sencilla

DevOps comienza antes de escribir código.

Primero necesitamos organizar:

- qué queremos construir
- quién lo hará
- cuándo se hará
- cómo se dividirá el trabajo
- cómo controlaremos los cambios del código

## Azure Boards

Azure Boards permite planificar y dar seguimiento al trabajo.

Jerarquía típica:

Epic
? Feature
? User Story
? Task

## Epics

Representan iniciativas grandes.

Ejemplo:

Modernizar plataforma de ventas

## Features

Representan capacidades importantes dentro de una Epic.

Ejemplo:

Nuevo proceso de checkout

## User Stories

Representan necesidades concretas del usuario.

Ejemplo:

Como cliente quiero pagar con tarjeta para finalizar mi compra.

## Tasks

Representan trabajo técnico necesario para completar una User Story.

Ejemplo:

Implementar endpoint de pago.

## Bugs

Permiten registrar defectos encontrados durante desarrollo o pruebas.

## Backlogs

El backlog contiene el trabajo pendiente.

Puede priorizarse según:

- valor
- urgencia
- riesgo
- dependencia

## Sprints

Un Sprint representa un periodo de trabajo planificado.

Ejemplo:

Sprint 1
? User Stories
? Tasks
? Development
? Review

## Azure Repos

Azure Repos proporciona repositorios Git privados dentro de Azure DevOps.

Permite trabajar con:

- branches
- commits
- pull requests
- policies
- reviewers
- tags

## Git

Git permite registrar cambios en archivos a lo largo del tiempo.

Flujo básico:

Working Directory
? git add
? Staging
? git commit
? Local Repository
? git push
? Remote Repository

## Branches

Las ramas permiten trabajar en cambios sin modificar directamente la rama principal.

Ejemplo:

main
? feature/login
? commit
? pull request
? main

## Pull Requests

Un Pull Request permite revisar cambios antes de integrarlos.

Puede incluir:

- reviewers
- discussions
- validation
- policies
- build checks

## Flujo empresarial

Requirement
? Work Item
? Branch
? Code
? Commit
? Pull Request
? Review
? Merge

## Labs relacionados

- Lab 01: Agile planning and portfolio management with Azure Boards
- Lab 02: Version Control with Git in Azure Repos

## Mensaje clave

Enterprise DevOps conecta planificación y código.

Work
? Code
? Review
? Delivery
