from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        # Lista privada de tareas (Estado del sistema)
        self._tareas = []

    def añadir_tarea(self, tarea: Tarea):
        """Añade un objeto Tarea (Inyección de Dependencia)."""
        self._tareas.append(tarea)

    def marcar_completada(self, indice):
        """Usa el setter del modelo para cambiar el estado."""
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].completada = True

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)

    def obtener_todas(self):
        return self._tareas