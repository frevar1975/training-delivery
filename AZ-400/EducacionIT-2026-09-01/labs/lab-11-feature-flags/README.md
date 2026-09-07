# Lab 11 - Enable Dynamic Configuration and Feature Flags

## Objetivo

Implementar configuración dinámica y Feature Flags para controlar funcionalidades sin necesidad de realizar nuevos despliegues.

## Relación con el módulo

Module 04 - Implement a Secure Continuous Deployment using Azure Pipelines

## Conceptos relacionados

- Azure App Configuration
- Feature Flags
- Dynamic Configuration
- Feature Management
- Controlled Release
- Deployment Strategy

## Escenario

Una aplicación contiene una nueva funcionalidad.

Queremos desplegar la aplicación sin habilitar inmediatamente esa funcionalidad para todos los usuarios.

## Flujo

Deploy Application
? Feature Disabled
? Validation
? Enable Feature
? Monitor

## Parte 1 - Azure App Configuration

Ingresar a Azure Portal.

Localizar:

App Configuration

Revisar el recurso utilizado para el laboratorio.

## Parte 2 - Feature Manager

Ingresar a:

Operations
? Feature manager

Revisar los Feature Flags disponibles.

## Parte 3 - Crear Feature Flag

Crear una nueva característica.

Ejemplo:

NewCheckoutExperience

Configurar inicialmente:

Disabled

## Parte 4 - Integrar con la aplicación

La aplicación consulta el estado del Feature Flag.

Conceptualmente:

Application
? App Configuration
? Feature Flag
? Enabled / Disabled

## Parte 5 - Habilitar funcionalidad

Cambiar el Feature Flag a:

Enabled

Validar el cambio en la aplicación.

## Parte 6 - Deshabilitar funcionalidad

Desactivar nuevamente la característica.

Observar que no es necesario realizar un nuevo deployment.

## Casos de uso

Feature Flags permiten:

- liberar funcionalidades gradualmente
- probar funciones con usuarios internos
- desactivar funcionalidades problemáticas
- realizar experimentación
- disminuir riesgo de despliegue

## Diferencia importante

Deployment:

código nuevo llega al ambiente.

Release:

una funcionalidad queda disponible para los usuarios.

Feature Flags permiten separar ambos conceptos.

## Validación

El alumno debe poder explicar:

- qué es configuración dinámica
- qué es un Feature Flag
- diferencia entre Deployment y Release
- por qué Feature Flags reducen riesgo
- función de Azure App Configuration

## Preguntas de cierre

1. ¿Podemos desplegar código sin liberar una funcionalidad?
2. ¿Qué ventaja tiene desactivar una función sin redeploy?
3. ¿Cómo ayudan los Feature Flags a reducir riesgo?
4. ¿Cuál es la diferencia entre deployment y release?

## Mensaje clave

Feature Flags permiten separar:

Deploy
de
Release

Esto permite controlar cuándo y para quién se habilita una funcionalidad.

## Referencia oficial

Microsoft Learn AZ-400:
Enable Dynamic Configuration and Feature Flags.
