# modelos/tarea.py

class Tarea:
    def __init__(self, id_tarea, titulo, descripcion, prioridad="Media", fecha="2026-03-27"):
        self.__id_tarea = id_tarea
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__fecha = fecha
        self.__completada = False

    # --- GETTERS ---
    @property
    def id_tarea(self):
        return self.__id_tarea

    @property
    def titulo(self):
        return self.__titulo

    @property
    def descripcion(self):
        return self.__descripcion  # Corregido: antes decía _descripcion

    @property
    def completada(self):
        return self.__completada   # Corregido: antes decía _completada

    @property
    def prioridad(self):
        return self.__prioridad

    @property
    def fecha(self):
        return self.__fecha

    # --- SETTERS ---
    @completada.setter
    def completada(self, valor):
        if isinstance(valor, bool):
            self.__completada = valor # Corregido: antes decía _completada
        else:
            raise ValueError("El estado debe ser un valor booleano.")

    @prioridad.setter
    def prioridad(self, valor):
        self.__prioridad = valor

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor