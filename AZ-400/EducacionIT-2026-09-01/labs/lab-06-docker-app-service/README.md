# Lab 06 - Deploy Docker Containers to Azure App Service Web Apps

## Objetivo

Comprender cómo construir una aplicación en un contenedor Docker y desplegarla en Azure App Service.

## Relación con el módulo

Module 02 - Implement CI with Azure Pipelines and GitHub Actions

## Conceptos relacionados

- Docker
- Containers
- Dockerfile
- Container Image
- Container Registry
- Azure App Service
- CI/CD
- Deployment

## Escenario

Una aplicación necesita ejecutarse de forma consistente entre diferentes ambientes.

Se utilizará un contenedor para empaquetar:

- aplicación
- runtime
- dependencias
- configuración necesaria

## Flujo

Source Code
? Dockerfile
? Docker Build
? Container Image
? Registry
? Azure App Service

## Parte 1 - Revisar Dockerfile

Un Dockerfile contiene instrucciones para construir una imagen.

Ejemplo conceptual:

FROM nginx:latest

COPY . /usr/share/nginx/html

## Parte 2 - Construir imagen

Ejemplo:

docker build -t demo-web-app .

## Parte 3 - Revisar imágenes

Ejecutar:

docker images

## Parte 4 - Ejecutar localmente

Ejemplo:

docker run -p 8080:80 demo-web-app

Comprobar que la aplicación responde localmente.

## Parte 5 - Container Registry

La imagen debe almacenarse en un registry accesible para el proceso de deployment.

Flujo:

Local Image
? Container Registry
? Azure App Service

## Parte 6 - Publicar imagen

Etiquetar y publicar la imagen en el registry correspondiente.

Conceptualmente:

docker tag
? docker push
? Registry

## Parte 7 - Configurar Azure App Service

Crear o revisar una Web App configurada para ejecutar un contenedor.

Azure App Service debe conocer:

- registry
- image
- tag
- authentication

## Parte 8 - Realizar Deployment

Configurar App Service para utilizar la imagen publicada.

## Parte 9 - Validar aplicación

Abrir la URL de la Web App.

Comprobar que la aplicación está funcionando.

## Parte 10 - Integración CI/CD

El proceso puede automatizarse.

Repository
? Pipeline
? Build Image
? Test
? Push Image
? Registry
? Deploy
? App Service

## Container Image vs Container

Image:

Plantilla inmutable utilizada para crear containers.

Container:

Instancia en ejecución de una image.

## Beneficios

Los contenedores proporcionan:

- consistencia
- portabilidad
- aislamiento
- despliegues repetibles
- facilidad de automatización

## Validación

Al finalizar, el alumno debe poder explicar:

- qué es Docker
- qué es un Dockerfile
- diferencia entre Image y Container
- función de un Container Registry
- cómo App Service obtiene una imagen
- cómo integrar containers dentro de CI/CD

## Preguntas de cierre

1. ¿Qué problema resuelve un contenedor?
2. ¿Qué diferencia existe entre Image y Container?
3. ¿Para qué necesitamos un Container Registry?
4. ¿Cómo integraríamos este proceso con una pipeline?

## Mensaje clave

Los contenedores permiten empaquetar una aplicación y sus dependencias de forma consistente.

Code
? Image
? Registry
? Deployment
? Application

## Referencia oficial

Microsoft Learn AZ-400:
Deploy Docker containers to Azure App Service web apps.
