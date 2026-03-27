class Tarea:
    def __init__(self, descripcion):
        # Atributos privados (Encapsulamiento)
        self._descripcion = descripcion
        self._completada = False

    @property
    def descripcion(self):
        """Getter para obtener la descripción."""
        return self._descripcion

    @property
    def completada(self):
        """Getter para obtener el estado de la tarea."""
        return self._completada

    @completada.setter
    def completada(self, valor):
        """Setter para modificar el estado con validación."""
        if isinstance(valor, bool):
            self._completada = valor
        else:
            raise ValueError("El estado debe ser un valor booleano.")