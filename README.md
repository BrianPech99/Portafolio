# Portafolio
Evidencias - Tareas

## TAREA 998 - Editar el Readme
Listo subame 10

---

## Bitácora de Clase

### 15 de agosto de 2025
- **Tema:** High Availability (Alta disponibilidad)  
- **Apuntes de clase:**  
  - **A nivel de red**  
  - **RAID (Redundant Array of Independent/Inexpensive Disks)**  
  - Unicaribe.edu.mx: diferencia entre acceso **privado y público**.  
  - **Load Balancer (LB):**  
    - Uso de *Keepalived* (cuando un nodo activo pasa a pasivo).  
    - Los balanceadores distribuyen tráfico mediante algoritmos.  
    - **Algoritmos:** Round Robin, Round Weighted (peso), basados en contexto (características).  
  - **AWS Load Balancer:**  
    - HTTP, HTTPS.  
    - **Application LB**.  
    - **Network LB**: TCP, UDP (puertos 3306, 1433).  
    - **Classic LB**: no exclusivo de tráfico web.  
  - **Arquitectura de 3 capas:** Frontend – Backend – Conexión a nivel de transporte y red.  
  - **Contenedores:** Docker, LXC, Podman (herramientas de virtualización ligera).  
  - Kubernetes (manifestador de contenedores).  
- **Notas:** Se revisaron las principales soluciones de alta disponibilidad y balanceo de carga.  

### 20 de agosto de 2025
- **Tema:** Clusters y conceptos relacionados  
- **Apuntes de clase:**  
  - **Cluster:** conjunto de computadoras que funcionan como un solo sistema.  
    - Tipos:  
      - **Alta disponibilidad (HA):** garantiza continuidad del servicio.  
      - **Balanceo de carga (LB):** distribuye tareas entre nodos.  
      - **Alto rendimiento (HPC):** usado en cálculos científicos y complejos.  
  - **SSH Keys:** permiten conexiones seguras y automatizadas entre nodos.  
  - **Herramientas de trabajo:**  
    - **Visual Studio Code** (editor con soporte para SSH y Git).  
    - **Git Bash** (terminal en Windows similar a Linux).  
    - **Markdown** (documentación ligera y clara).  
  - **Orden de encendido y apagado en clusters:**  
    - Encendido: primero el nodo maestro, luego los secundarios.  
    - Apagado: primero los secundarios, al final el maestro.  
  - **Alta disponibilidad:**  
    - **BCP (Business Continuity Plan):** asegura que la empresa siga operando en caso de fallas o desastres.  
    - **DR (Disaster Recovery):** plan para restaurar infraestructura y servicios de TI (incluye backups y sitios alternos).  
- **Notas:** Se destacaron la importancia de la seguridad con SSH y el papel de los clusters en la continuidad del servicio.  

### 21 de agosto de 2025
- **Tema:** Introducción al curso y organización del portafolio.
- **Actividades:** 
  - Revisión de objetivos del semestre.
  - Edición inicial del archivo README.md.
- **Notas:** Se explicó la importancia de documentar el trabajo realizado.

### 22 de agosto de 2025
- **Tema:** Primeros pasos con Markdown.
- **Actividades:** 
  - Práctica de sintaxis básica de Markdown.
  - Ejemplo de listas, títulos y separación de secciones.
- **Notas:** Se recomienda mantener la bitácora actualizada después de cada clase.

### 27 de agosto de 2025
- **Tema:** Cluster con contenedores  
- **Apuntes de clase:**  
  - **Virtualización tradicional:**  
    - Uso de **VirtualBox** con hipervisores que crean máquinas virtuales completas (hardware, disco, sistema operativo).  
    - Alto consumo de recursos.  
  - **Contenedores:**  
    - Espacios aislados para aplicaciones con librerías y frameworks necesarios.  
    - Menor consumo de recursos que una máquina virtual.  
    - Ejemplo: contenedor con Linux mínimo (Tiny Core Linux, Alpine).  
    - Son efímeros, pero pueden configurarse para persistir (ejemplo: procesos SQL).  
  - **Docker:**  
    - Usa **imágenes** y **contenedores**.  
    - Archivos **Dockerfile** definen cómo construir una imagen.  
    - Comandos clave: `build`, `run`, `stop`, `ps`, `start`.  
    - Ejemplo práctico: contenedor *Hola Mundo* y creación de imágenes personalizadas.  
  - **Redes y nodos en clusters:**  
    - Cada nodo (n1, n2, n3) debe coincidir con nombres e IP configuradas en la red.  
  - **Kubernetes (K8s):**  
    - Orquestador de contenedores para administrar clusters a gran escala.  
- **Notas:** Se compararon máquinas virtuales e infraestructura con contenedores, destacando la eficiencia y escalabilidad de Docker y Kubernetes en clusters modernos.  

### 29 de agosto de 2025
- **Tema:** Sysbench y despliegue con Docker  
- **Apuntes de clase:**  
  - **Sysbench:**  
    - Herramienta para simular cargas de trabajo y pruebas de rendimiento.  
    - Evalúa procesador (multinúcleo, hilos), memoria, lectura/escritura y desempeño en múltiples nodos.  
    - Parámetro clave: `time` (duración de la prueba).  
  - **Docker y despliegue:**  
    - Uso de contenedores para simplificar la ejecución de aplicaciones.  
    - Ejemplo con **Dockerfile**:  
      - Imagen base ligera como `alpine`.  
      - Ejemplo *Hello World* con Python 3.10.  
      - Uso de variables de entorno (`ENV`) para configuración.  
    - Comandos clave: `RUN`, `EXPOSE`, `CMD`.  
  - **Flask (Python):**  
    - Framework ligero para aplicaciones web rápidas.  
    - Corre en contenedores y mantiene el servicio activo hasta que se detenga manualmente.  
    - Configuración de puertos: se mapean entre el host y el contenedor (`host:puerto → contenedor:puerto`).  
  - **Bases de datos en contenedores:**  
    - Ejemplo: levantar **MySQL** en nodo 1 (puerto 3306) y en un segundo nodo con la misma configuración.  
    - Necesidad de mapear correctamente los puertos y direcciones IP.  
    - Se destacó el concepto de **puertos efímeros** (0–65535).  
- **Notas:** La clase integró pruebas de rendimiento con Sysbench y la práctica de despliegue de aplicaciones en contenedores usando Docker y Flask.  
