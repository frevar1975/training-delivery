# Lab 14 - Monitor Application Performance with Azure Load Testing

## Objetivo

Ejecutar pruebas de carga para analizar el rendimiento de una aplicación utilizando Azure Load Testing.

## Relación con el módulo

Module 08 - Implement Continuous Feedback

## Conceptos relacionados

- Load Testing
- Performance Testing
- Response Time
- Throughput
- Failed Requests
- Scalability
- Performance Validation

## Escenario

Una aplicación funciona correctamente con pocos usuarios.

Antes de liberarla, queremos conocer cómo se comporta cuando aumenta la carga.

## Flujo

Users
? Requests
? Application
? Metrics
? Analysis
? Feedback

## Parte 1 - Abrir Azure Load Testing

Ingresar a Azure Portal.

Localizar el recurso:

Azure Load Testing

## Parte 2 - Crear o revisar una prueba

Revisar la configuración de la prueba.

Identificar:

- test configuration
- users
- duration
- endpoints
- test engine

## Parte 3 - Ejecutar Load Test

Iniciar la prueba.

Observar cómo se generan solicitudes contra la aplicación.

## Parte 4 - Revisar métricas

Analizar:

- response time
- requests per second
- failed requests
- latency
- throughput

## Parte 5 - Analizar rendimiento

Identificar:

- degradación
- errores
- cuellos de botella
- límites de capacidad

## Parte 6 - Comparar resultados

Comparar distintas ejecuciones.

Ejemplo:

Version A
vs
Version B

## Parte 7 - Integrar con Pipeline

Explicar que una prueba de carga puede formar parte de un proceso de CI/CD.

Flujo:

Build
? Deploy Test Environment
? Load Test
? Evaluate
? Continue / Stop

## Validación

Al finalizar, el alumno debe poder explicar:

- qué es una prueba de carga
- diferencia entre functional testing y load testing
- qué métricas revisar
- cómo detectar degradación
- cómo integrar performance testing con DevOps

## Preguntas de cierre

1. ¿Por qué una aplicación puede funcionar bien con 10 usuarios y fallar con 1000?
2. ¿Qué significa response time?
3. ¿Qué ocurre si aumenta el número de failed requests?
4. ¿Por qué incorporar performance testing en una pipeline?

## Mensaje clave

La calidad no se mide solamente por si una aplicación funciona.

También debemos validar cómo se comporta bajo carga.

## Referencia oficial

Microsoft Learn AZ-400:
Monitor Application Performance with Azure Load Testing.
