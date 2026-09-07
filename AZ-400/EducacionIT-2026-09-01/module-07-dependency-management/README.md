# Module 07 - Design and Implement a Dependency Management Strategy

## Objetivo

Comprender cómo administrar dependencias y paquetes de software de forma controlada utilizando Azure Artifacts.

## Conceptos clave

- Dependency Management
- Package Management
- Azure Artifacts
- Feeds
- Package Versions
- Upstream Sources
- NuGet
- npm
- Maven
- Python packages

## Explicación sencilla

Las aplicaciones dependen de librerías y paquetes externos.

Si esas dependencias no se administran correctamente, pueden aparecer problemas de:

- versiones incompatibles
- paquetes inseguros
- falta de trazabilidad
- builds inconsistentes

## Analogía

Podemos pensar en las dependencias como piezas utilizadas para fabricar un producto.

Si cada desarrollador utiliza piezas diferentes, el resultado puede variar.

Un gestor de paquetes permite controlar:

- qué pieza utilizar
- qué versión
- de dónde proviene
- quién puede consumirla

## Azure Artifacts

Azure Artifacts permite crear feeds privados para almacenar y distribuir paquetes.

Un feed puede contener paquetes de tecnologías como:

- NuGet
- npm
- Maven
- Python

## Feeds

Un feed funciona como un repositorio de paquetes.

Flujo:

Developer
? Package
? Azure Artifacts Feed
? Application / Pipeline

## Versionado

Los paquetes deben utilizar versiones claras.

Ejemplo:

1.0.0
1.1.0
2.0.0

Esto facilita controlar qué versión consume cada aplicación.

## Upstream Sources

Azure Artifacts puede utilizar fuentes externas como origen de paquetes.

Esto permite centralizar y controlar dependencias provenientes de repositorios públicos.

## Integración con Pipelines

Repository
? Build
? Package
? Publish
? Azure Artifacts

Luego:

Azure Artifacts
? Restore Package
? Build Application

## Seguridad

Una estrategia de dependency management ayuda a:

- controlar acceso
- reducir dependencias no autorizadas
- mejorar trazabilidad
- administrar versiones
- evitar consumo directo e indiscriminado de paquetes externos

## Lab relacionado

- Lab 13: Package Management with Azure Artifacts

## Mensaje clave

Las dependencias también forman parte de la cadena de suministro de software.

Deben ser:

- versionadas
- controladas
- trazables
- reproducibles
