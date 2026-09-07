# Lab 08 - Control Deployments using Release Gates

## Objetivo

Comprender cómo controlar despliegues utilizando gates, approvals y checks.

## Relación con el módulo

Module 03 - Design and Implement a Release Strategy

## Conceptos relacionados

- Release Gates
- Approvals
- Checks
- Environments
- Deployment control
- Production protection

## Escenario

La organización quiere evitar que una aplicación llegue a producción sin validaciones previas.

## Flujo

Build
→ Test
→ Deploy Staging
→ Validation
→ Approval
→ Production

## Parte 1 - Revisar Environments

Ingresar a:

Pipelines
→ Environments

Revisar los environments disponibles.

## Parte 2 - Configurar una validación

Explicar que antes de desplegar se pueden establecer condiciones.

Ejemplos:

- aprobación manual
- validaciones automáticas
- checks externos
- políticas internas

## Parte 3 - Aprobar un despliegue

Mostrar el flujo:

Deployment requested
→ Approval required
→ Approved
→ Deployment continues

## Parte 4 - Rechazar un despliegue

Explicar que una aprobación puede impedir que una versión continúe.

## Parte 5 - Revisar trazabilidad

Mostrar:

- quién aprobó
- cuándo aprobó
- qué versión fue desplegada
- qué environment fue utilizado

## Validación

El alumno debe poder explicar:

- qué es un gate
- qué es un approval
- por qué proteger producción
- diferencia entre automatización y autorización

## Preguntas de cierre

1. ¿Por qué no conviene desplegar directamente a producción?
2. ¿Cuándo utilizar una aprobación manual?
3. ¿Qué ventaja aporta la trazabilidad?

## Mensaje clave

Automatizar no significa eliminar controles.

DevOps busca automatizar manteniendo gobierno y seguridad.

## Referencia oficial

Microsoft Learn AZ-400:
Control Deployments using Release Gates.
