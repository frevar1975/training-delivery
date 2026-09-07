# Lab 09 - Set Up and Run Functional Tests

## Objetivo

Configurar y ejecutar pruebas funcionales como parte del proceso de validación de una aplicación.

## Relación con el módulo

Module 03 - Design and Implement a Release Strategy

## Conceptos relacionados

- Functional tests
- Quality validation
- Release validation
- Test execution
- Deployment confidence

## Escenario

Una aplicación puede compilar correctamente y aun así presentar errores funcionales.

Por eso se deben validar comportamientos reales antes de liberar una versión.

## Diferencia conceptual

Build Test
→ verifica compilación y componentes

Functional Test
→ verifica comportamiento de la aplicación

## Flujo

Build
→ Unit Tests
→ Deploy Test Environment
→ Functional Tests
→ Validation
→ Release

## Parte 1 - Preparar el ambiente

Utilizar un environment destinado a pruebas.

## Parte 2 - Ejecutar Functional Tests

Ejecutar las pruebas definidas para la aplicación.

## Parte 3 - Revisar resultados

Analizar:

- tests ejecutados
- tests exitosos
- tests fallidos
- logs
- duración
- errores

## Parte 4 - Integrar los tests al pipeline

Explicar que un fallo funcional puede bloquear la continuación del release.

Ejemplo conceptual:

Functional Tests Passed
→ Continue

Functional Tests Failed
→ Stop Release

## Validación

El alumno debe poder explicar:

- diferencia entre build y functional testing
- por qué ejecutar pruebas antes de producción
- cómo una prueba puede bloquear un release
- importancia del feedback automático

## Preguntas de cierre

1. ¿Puede una aplicación compilar correctamente y funcionar mal?
2. ¿Dónde conviene ejecutar functional tests?
3. ¿Qué debería ocurrir si una prueba crítica falla?

## Mensaje clave

Una release no debería considerarse válida solo porque la aplicación compila.

Debe comprobarse que el comportamiento esperado también funciona.

## Referencia oficial

Microsoft Learn AZ-400:
Set up and run functional tests.
