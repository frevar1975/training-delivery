# Lab 02 - Version Control with Git in Azure Repos

## Objetivo

Utilizar Git y Azure Repos para administrar cambios de código mediante branches, commits y pull requests.

## Relación con el módulo

Module 01 - Implement Development for Enterprise DevOps

## Conceptos relacionados

- Git
- Azure Repos
- Clone
- Branch
- Commit
- Push
- Pull
- Pull Request
- Merge
- Version Control

## Escenario

Un equipo desarrolla una aplicación de forma colaborativa.

Necesita controlar cambios, evitar sobrescribir trabajo y revisar modificaciones antes de integrarlas.

## Parte 1 - Abrir Azure Repos

Ingresar al proyecto.

Ir a:

Repos
? Files

Revisar el repositorio.

## Parte 2 - Clonar repositorio

Obtener la URL del repositorio.

Ejemplo:

git clone <repository-url>

Ingresar a la carpeta:

cd <repository>

## Parte 3 - Revisar estado

Ejecutar:

git status

## Parte 4 - Crear una Branch

Ejemplo:

git switch -c feature/demo

La nueva branch permite trabajar sin modificar directamente main.

## Parte 5 - Realizar un cambio

Modificar un archivo.

Ejemplo:

README.md

## Parte 6 - Preparar cambios

Ejecutar:

git add .

## Parte 7 - Crear Commit

Ejecutar:

git commit -m "Add demo change"

## Parte 8 - Publicar Branch

Ejecutar:

git push -u origin feature/demo

## Parte 9 - Crear Pull Request

En Azure DevOps:

Repos
? Pull requests
? New pull request

Seleccionar:

Source:
feature/demo

Target:
main

## Parte 10 - Revisar cambios

Analizar:

- Files changed
- Commits
- Reviewers
- Discussion
- Policies

## Parte 11 - Completar Pull Request

Después de la revisión:

Complete

Comprobar que los cambios fueron integrados en main.

## Flujo

Clone
? Branch
? Change
? Add
? Commit
? Push
? Pull Request
? Review
? Merge

## Buenas prácticas

- evitar trabajar directamente sobre main
- utilizar commits descriptivos
- crear branches pequeñas
- revisar cambios mediante Pull Requests
- aplicar políticas en ramas críticas

## Validación

Al finalizar, el alumno debe poder explicar:

- diferencia entre Git y Azure Repos
- qué es una branch
- qué es un commit
- qué hace git push
- qué es un Pull Request
- por qué revisar cambios antes de merge

## Preguntas de cierre

1. ¿Por qué no trabajar siempre directamente sobre main?
2. ¿Qué diferencia existe entre commit y push?
3. ¿Para qué sirve un Pull Request?
4. ¿Qué ventaja aporta el historial de Git?

## Mensaje clave

Git registra los cambios.

Azure Repos permite colaborar y gobernar esos cambios dentro de Azure DevOps.

## Referencia oficial

Microsoft Learn AZ-400:
Version Control with Git in Azure Repos.
