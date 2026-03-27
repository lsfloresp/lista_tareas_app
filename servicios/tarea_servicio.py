from modelos.tarea import Tarea


class TareaServicio:
    def __init__(self):
        # Lista de tareas (Estado del sistema)
        self._tareas = []

    def añadir_tarea(self, titulo, descripcion, prioridad, fecha):
        """Crea el objeto Tarea con los nuevos datos y lo añade a la lista."""
        # Generamos un ID simple basado en la posición
        nuevo_id = len(self._tareas) + 1

        # Creamos la instancia del Modelo con los 5 datos necesarios
        nueva_tarea = Tarea(nuevo_id, titulo, descripcion, prioridad, fecha)

        self._tareas.append(nueva_tarea)
        return nueva_tarea

    def marcar_completada(self, indice):
        """Usa el setter del modelo para cambiar el estado."""
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].completada = True

    def eliminar_tarea(self, indice):
        """Elimina una tarea por su índice."""
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)

    def obtener_todas(self):
        """Retorna la lista completa para la UI."""
        return self._tareas