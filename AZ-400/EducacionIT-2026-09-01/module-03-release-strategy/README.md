# Module 03 - Design and Implement a Release Strategy

## Objetivo

Comprender cómo diseñar e implementar una estrategia de release utilizando Azure DevOps.

## Conceptos clave

- Release strategy
- YAML pipelines
- Stages
- Environments
- Approvals
- Gates
- Functional tests
- Deployment validation
- Pipeline as Code

## Explicación sencilla

Una estrategia de release define cómo una aplicación pasa desde el desarrollo hasta los ambientes donde será utilizada.

Flujo típico:

Code
→ Build
→ Test
→ Artifact
→ Deploy
→ Validate
→ Release

## Analogía

Podemos comparar una estrategia de release con el proceso de lanzamiento de un producto.

- Código = producto
- Build = fabricación
- Tests = control de calidad
- Artifact = producto terminado
- Deployment = distribución
- Gates = controles de autorización
- Release = producto disponible

## YAML Pipelines

YAML permite definir la pipeline como código.

Esto facilita:

- versionado
- reutilización
- control de cambios
- revisión mediante pull requests
- automatización consistente

## Stages

Una pipeline puede dividirse en stages.

Ejemplo:

Build
→ Test
→ Deploy Dev
→ Deploy Test
→ Deploy Production

Cada stage representa una fase del proceso.

## Environments

Los environments representan destinos donde una aplicación puede ser desplegada.

Ejemplos:

- Development
- Testing
- Staging
- Production

## Approvals

Permiten solicitar autorización antes de ejecutar una determinada fase.

Ejemplo:

Deploy Production
→ Approval
→ Deployment

## Gates

Los gates permiten validar condiciones antes de continuar.

Ejemplos:

- aprobación manual
- estado de servicios
- métricas
- validaciones externas
- checks automáticos

## Functional Tests

Los functional tests verifican que la aplicación se comporte correctamente desde el punto de vista funcional.

## Flujo completo

Commit
→ CI
→ Artifact
→ Release Pipeline
→ Environment
→ Validation
→ Approval
→ Production

## Demos sugeridas

1. YAML multi-stage pipeline
2. Environments
3. Approvals and checks
4. Release gates
5. Functional test execution

## Labs relacionados

- Lab 07: Configure Pipelines as Code with YAML
- Lab 08: Control Deployments using Release Gates
- Lab 09: Set up and run functional tests

## Mensaje clave

Una buena estrategia de release busca que los cambios lleguen a producción de forma:

- repetible
- controlada
- automatizada
- auditable
- segura
