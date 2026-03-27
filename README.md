# Agenda Digital Interactiva - Luis Flores

Este proyecto consiste en una aplicación de escritorio profesional para la gestión de tareas (To-Do List), desarrollada en Python utilizando la librería **Tkinter**. El sistema permite organizar actividades académicas por materia, descripción, prioridad y fecha de entrega.

## 📂 Arquitectura del Proyecto (Patrón por Capas)
El código está estrictamente organizado para separar la lógica de negocio de la interfaz de usuario:

- **`modelos/tarea.py`**: Define la entidad `Tarea` con atributos privados (`__`), Getters y Setters (@property), asegurando el encapsulamiento.
- **`servicios/tarea_servicio.py`**: Contiene la lógica de control, gestión de la lista de tareas y cambios de estado.
- **`ui/app_tkinter.py`**: Gestiona toda la interfaz gráfica, estilos y captura de datos.
- **`main.py`**: Punto de entrada que inicializa la aplicación.

## 🛠️ Requisitos Técnicos Implementados

### 1. Manejo de Eventos Avanzados
Para mejorar la fluidez de la experiencia de usuario (UX), se implementaron los siguientes manejadores:
* **Teclado (`<Return>`)**: Permite añadir tareas presionando la tecla Enter desde el campo de entrada.
* **Ratón (`<Double-1>`)**: Permite marcar una tarea como completada instantáneamente haciendo doble clic sobre ella en la lista.

### 2. Feedback Visual Dinámico
La aplicación utiliza un sistema de colores tipo "semáforo" para identificar la urgencia:
* **Rojo (Alta)**: Tareas urgentes.
* **Amarillo (Media)**: Tareas importantes.
* **Azul (Baja)**: Tareas de rutina.
* **Verde (✔ [HECHO])**: Tareas finalizadas satisfactoriamente.

### 3. Validaciones de Datos
* **Prioridad**: Solo acepta los valores "Alta", "Media" o "Baja".
* **Fecha**: Valida estrictamente el formato `AAAA-MM-DD` para evitar errores en la agenda.

## 📦 Compilación (Ejecutable)
El proyecto fue empaquetado utilizando **PyInstaller** como un archivo único e independiente:

```bash
pyinstaller --clean --onefile --noconsole --name "TkMiApp" main.py