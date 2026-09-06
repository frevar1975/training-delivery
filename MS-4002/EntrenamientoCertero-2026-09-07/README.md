# MS-4002 - Prepare Security and Compliance to Support Microsoft 365 Copilot

Template reutilizable para la preparación y dictado del curso **MS-4002**.

Este repositorio organiza el contenido teórico, demostraciones y laboratorios utilizados para preparar un entorno Microsoft 365 antes de una implementación de Microsoft 365 Copilot.

---

## Objetivo del curso

El curso aborda los controles de seguridad, identidad, permisos y protección de información que una organización debe considerar antes y durante la adopción de Microsoft 365 Copilot.

El flujo general del curso es:

```text
Microsoft 365
      |
      v
Identity
      |
      v
Secure Access
      |
      v
Roles & Permissions
      |
      v
Information Protection
      |
      +---- DLP
      |
      +---- Sensitivity Labels
      |
      v
Microsoft 365 Copilot
```

---

## Módulos

El contenido está organizado siguiendo los ocho módulos del curso.

### Module 01 - Copilot Readiness

```text
module-01-copilot-readiness
```

Preparación de Microsoft 365 para Microsoft 365 Copilot.

Temas principales:

- requisitos de Microsoft 365 Copilot;
- preparación del tenant;
- licenciamiento;
- servicios Microsoft 365;
- preparación inicial para Copilot.

---

### Module 02 - Secure Access

```text
module-02-secure-access
```

Administración del acceso seguro de usuarios.

Temas principales:

- Microsoft Entra ID;
- usuarios y grupos;
- autenticación;
- MFA;
- Conditional Access;
- Smart Lockout;
- Password Protection.

---

### Module 03 - Roles and Permissions

```text
module-03-roles-permissions
```

Administración de permisos, roles y grupos de roles.

Temas principales:

- Microsoft Entra roles;
- principio de mínimo privilegio;
- asignación directa de roles;
- role-assignable groups;
- administración delegada;
- Microsoft Graph PowerShell.

---

### Module 04 - Microsoft 365 Apps

```text
module-04-m365-apps
```

Preparación y administración de Microsoft 365 Apps para usuarios de Copilot.

Temas principales:

- Microsoft 365 Apps for enterprise;
- preparación de aplicaciones;
- canales de actualización;
- administración de aplicaciones;
- integración con servicios Microsoft 365.

---

### Module 05 - Data Loss Prevention

```text
module-05-dlp
```

Implementación de Microsoft Purview Data Loss Prevention.

Temas principales:

- Microsoft Purview;
- DLP policies;
- Sensitive Information Types;
- reglas DLP;
- Policy Tips;
- bloqueo;
- override;
- alertas y monitoreo.

---

### Module 06 - Sensitivity Labels

```text
module-06-sensitivity-labels
```

Implementación de etiquetas de confidencialidad.

Temas principales:

- Information Protection;
- Sensitivity Labels;
- clasificación;
- Content Marking;
- Encryption;
- Label Policies;
- justificación;
- integración con SharePoint y OneDrive.

---

### Module 07 - Copilot Extensibility

```text
module-07-extensibility
```

Administración de la extensibilidad de Microsoft 365 Copilot.

Temas principales:

- extensibilidad de Copilot;
- agentes;
- aplicaciones;
- controles administrativos;
- gobierno de extensiones.

---

### Module 08 - Review

```text
module-08-review
```

Revisión integral de la ruta de aprendizaje.

Relaciona:

```text
Identity
+
Access
+
Permissions
+
DLP
+
Sensitivity Labels
+
Copilot Governance
```

---

# Laboratorios

Los laboratorios se encuentran en:

```text
labs
```

Existen dos modalidades:

```text
labs
├── standalone
└── xtremelabs
```

---

## Standalone

La modalidad principal para este template es:

```text
labs/standalone
```

Está diseñada para poder realizar los ejercicios utilizando:

- PC del alumno;
- navegador;
- tenant Microsoft 365 de práctica;
- Microsoft Purview;
- Microsoft Entra;
- Microsoft 365 Admin Center;
- PowerShell local cuando sea necesario.

No depende de máquinas virtuales proporcionadas por un proveedor de laboratorios.

---

## Standalone - Lab 01

```text
labs/standalone/lab-01-tenant
```

### Initialize Microsoft 365 Tenant

Objetivos:

- acceder al tenant;
- revisar Microsoft 365 Admin Center;
- preparar un grupo piloto;
- revisar Custom Themes;
- preparar Microsoft Graph PowerShell.

---

## Standalone - Lab 02

```text
labs/standalone/lab-02-identities-security-roles
```

### Identities, Security and Roles

Objetivos:

- administrar usuarios;
- revisar licencias;
- trabajar con grupos;
- configurar Conditional Access de forma controlada;
- revisar MFA;
- revisar Smart Lockout y Password Protection;
- administrar roles;
- crear grupos asignables a roles;
- utilizar Microsoft Graph PowerShell.

---

## Standalone - Lab 03

```text
labs/standalone/lab-03-dlp
```

### Data Loss Prevention

Objetivos:

- acceder a Microsoft Purview;
- crear una política DLP;
- detectar Sensitive Information Types;
- utilizar Policy Tips;
- permitir contenido;
- bloquear contenido;
- configurar override;
- revisar alertas y eventos.

---

## Standalone - Lab 04

```text
labs/standalone/lab-04-sensitivity-labels
```

### Sensitivity Labels

Objetivos:

- crear una Sensitivity Label;
- configurar Scope;
- configurar Content Marking;
- revisar Encryption;
- publicar una etiqueta;
- crear una Label Policy;
- exigir justificación;
- probar etiquetas desde Microsoft 365.

---

# Estructura de cada laboratorio

Cada laboratorio utiliza:

```text
lab-XX
├── README.md
├── student-guide.md
├── instructor-guide.md
└── resources
    └── README.md
```

### student-guide.md

Guía paso a paso que puede compartirse con los alumnos.

### instructor-guide.md

Guía ampliada para el instructor con:

- explicación;
- analogías;
- puntos de demostración;
- recomendaciones;
- troubleshooting;
- clasificación de actividades.

### resources

Recursos adicionales utilizados por el laboratorio.

---

# XtremeLabs

La carpeta:

```text
labs/xtremelabs
```

está reservada para adaptaciones de los laboratorios cuando el centro de capacitación proporciona un entorno XtremeLabs.

El contenido de esta carpeta puede completarse progresivamente.

La documentación oficial del proveedor no debe duplicarse innecesariamente dentro del repositorio.

---

# Prompts

```text
prompts
```

Contiene prompts reutilizables utilizados durante las demostraciones o actividades relacionadas con Microsoft 365 Copilot.

---

# Scripts

```text
scripts
```

Contiene scripts reutilizables utilizados durante el curso.

Ejemplos:

- Microsoft Graph PowerShell;
- Microsoft 365;
- Microsoft Entra;
- validaciones del entorno.

---

# Datasets

```text
datasets
```

Contiene archivos de datos ficticios utilizados exclusivamente para:

- demos;
- pruebas;
- laboratorios.

No almacenar información real de usuarios o clientes.

---

# Estrategia de enseñanza

El curso utiliza tres tipos de actividades.

### ALUMNO

El alumno realiza directamente la configuración.

### DEMO INSTRUCTOR

El instructor demuestra la característica mientras explica su funcionamiento.

### OPCIONAL

Actividad dependiente de:

- tiempo;
- licencia;
- permisos;
- características del tenant;
- propagación de servicios.

---

# Seguridad de los laboratorios

Los ejercicios deben realizarse únicamente en:

```text
Tenant de práctica
```

Evitar realizar cambios de laboratorio en tenants productivos.

Especial atención a:

- Conditional Access;
- roles administrativos;
- DLP;
- Sensitivity Labels;
- Encryption;
- políticas globales.

---

# Regla del template

Este directorio contiene únicamente material:

```text
REUTILIZABLE
```

No debe contener información específica de:

- centro de capacitación;
- fecha de dictado;
- alumnos;
- credenciales;
- tenant asignado;
- contraseñas.

Las ejecuciones reales del curso se crean en:

```text
training-delivery
```

mediante:

```text
crear-curso.ps1
```

---

# Flujo de trabajo

```text
training-templates
       |
       v
MS-4002
       |
       v
Template reutilizable
       |
       v
crear-curso.ps1
       |
       v
training-delivery
       |
       v
Centro + Fecha
```

---

# Estado actual

## Standalone

```text
Lab 01 - Tenant                         [READY]
Lab 02 - Identities, Security & Roles  [READY]
Lab 03 - DLP                            [READY]
Lab 04 - Sensitivity Labels             [READY]
```

## XtremeLabs

```text
Adaptación complementaria / en desarrollo
```

---

# Resultado

La estructura busca permitir que el instructor prepare una sola vez el contenido reutilizable de MS-4002 y posteriormente genere diferentes ejecuciones del curso sin duplicar ni mezclar el material base.