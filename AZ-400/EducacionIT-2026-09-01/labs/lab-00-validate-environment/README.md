# Lab 00 - Validate Lab Environment

## Objetivo

Validar que el entorno necesario para realizar los laboratorios AZ-400 esté correctamente configurado.

## Relación con el módulo

Module 00 - Welcome

## Parte 1 - Validar Azure

Ingresar a Azure Portal.

Comprobar que:

- la cuenta puede iniciar sesión
- existe acceso a la suscripción correspondiente
- pueden visualizarse los recursos necesarios

## Parte 2 - Validar Azure DevOps

Ingresar a Azure DevOps.

Comprobar:

- acceso a la organización
- acceso al proyecto
- permisos disponibles

## Parte 3 - Revisar servicios

Dentro del proyecto identificar:

- Boards
- Repos
- Pipelines
- Test Plans
- Artifacts

## Parte 4 - Validar Git

Desde PowerShell ejecutar:

git --version

Confirmar que Git está instalado.

## Parte 5 - Validar Azure CLI

Ejecutar:

az version

Si el laboratorio requiere autenticación:

az login

## Parte 6 - Validar repositorios

Comprobar que se puede acceder al repositorio requerido por el laboratorio.

Conceptualmente:

Local Computer
? Git
? Repository
? Azure DevOps / GitHub

## Parte 7 - Validar permisos

Comprobar que la identidad utilizada dispone de los permisos necesarios para realizar las actividades previstas.

## Checklist

Antes de continuar:

- Azure accesible
- Azure DevOps accesible
- Proyecto accesible
- Repos accesibles
- Git instalado
- Azure CLI disponible cuando corresponda
- Permisos correctos

## Validación

El alumno debe poder identificar las herramientas que utilizará durante el curso y confirmar que puede acceder a ellas.

## Mensaje clave

Validar el entorno antes de comenzar evita perder tiempo solucionando problemas de acceso durante los laboratorios.

## Referencia oficial

Microsoft Learn AZ-400:
Validate lab environment.
