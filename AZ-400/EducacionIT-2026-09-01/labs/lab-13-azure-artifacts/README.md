# Lab 13 - Package Management with Azure Artifacts

## Objetivo

Administrar paquetes mediante Azure Artifacts y comprender cómo integrar dependencias dentro de procesos DevOps.

## Relación con el módulo

Module 07 - Design and Implement a Dependency Management Strategy

## Conceptos relacionados

- Azure Artifacts
- Feeds
- Packages
- Versions
- Dependency Management
- Package Restore
- Package Publish
- Upstream Sources

## Escenario

Una organización desarrolla aplicaciones que utilizan librerías compartidas.

Se necesita un repositorio centralizado donde almacenar y distribuir paquetes internos.

## Flujo

Source Code
? Build
? Package
? Azure Artifacts Feed

Y posteriormente:

Azure Artifacts Feed
? Restore
? Application Build

## Parte 1 - Abrir Azure Artifacts

Ingresar al proyecto de Azure DevOps.

Ir a:

Artifacts

## Parte 2 - Crear o revisar un Feed

Crear o seleccionar un feed.

Analizar:

- nombre
- visibilidad
- permisos
- upstream sources

## Parte 3 - Revisar formatos soportados

Azure Artifacts puede trabajar con paquetes como:

- NuGet
- npm
- Maven
- Python

## Parte 4 - Publicar un paquete

Generar un paquete desde un proyecto.

Publicarlo en el feed configurado.

## Parte 5 - Revisar versiones

Observar las versiones disponibles del paquete.

Explicar que diferentes aplicaciones pueden consumir versiones distintas.

## Parte 6 - Consumir un paquete

Configurar una aplicación para utilizar el feed.

Restaurar la dependencia.

Flujo:

Application
? Feed
? Package Version
? Build

## Parte 7 - Integrar con Pipeline

Explicar cómo una pipeline puede:

- restaurar paquetes
- compilar la aplicación
- generar nuevos paquetes
- publicar paquetes en Azure Artifacts

## Parte 8 - Revisar permisos

Analizar quién puede:

- leer paquetes
- publicar paquetes
- administrar feeds

## Validación

Al finalizar, el alumno debe poder explicar:

- qué es un feed
- qué problema resuelve Azure Artifacts
- por qué versionar paquetes
- diferencia entre publicar y consumir
- cómo integrar paquetes con pipelines
- qué función tienen los upstream sources

## Preguntas de cierre

1. ¿Por qué una organización necesitaría un feed privado?
2. ¿Qué problema puede causar utilizar siempre la última versión de una dependencia?
3. ¿Qué ventaja aporta centralizar paquetes?
4. ¿Cómo participa Azure Artifacts dentro de una pipeline?

## Mensaje clave

Una build reproducible necesita dependencias controladas.

Code
? Dependencies
? Build
? Artifact

## Referencia oficial

Microsoft Learn AZ-400:
Package Management with Azure Artifacts.
