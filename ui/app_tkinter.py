import tkinter as tk
from modelos.tarea import Tarea
from servicios.tarea_servicio import TareaServicio


class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Profesional - Luis Flores")
        self.root.geometry("450x550")
        self.servicio = TareaServicio()

        # --- Componentes de la Interfaz ---
        tk.Label(root, text="Descripción de la Tarea:", font=("Arial", 10, "bold")).pack(pady=5)
        self.entrada = tk.Entry(root, width=40, font=("Arial", 11))
        self.entrada.pack(pady=5)
        self.entrada.focus()

        # EVENTO TECLADO (<Return>): Permite añadir tareas con la tecla Enter.
        # Lógica: Mejora la fluidez al evitar el uso constante del ratón.
        self.entrada.bind("<Return>", lambda e: self.manejador_agregar())

        tk.Button(root, text="Añadir Tarea", command=self.manejador_agregar).pack(pady=5)

        # Listbox para visualización de tareas
        self.lista_box = tk.Listbox(root, width=55, height=15, font=("Arial", 10))
        self.lista_box.pack(pady=10, padx=20)

        # EVENTO RATÓN (<Double-1>): Doble clic para completar tarea.
        # Lógica: Se implementa como un atajo intuitivo basado en estándares de escritorio.
        self.lista_box.bind("<Double-1>", lambda e: self.manejador_completar())

        # Botones de estado con colores estándar (Verde/Rojo)
        tk.Button(root, text="Marcar Completada", bg="#C8E6C9", command=self.manejador_completar).pack(pady=2)
        tk.Button(root, text="Eliminar", bg="#FFCDD2", command=self.manejador_eliminar).pack(pady=5)

        self.refrescar_lista()

    def manejador_agregar(self):
        texto = self.entrada.get().strip()
        if texto:
            nueva = Tarea(texto)
            self.servicio.añadir_tarea(nueva)
            self.entrada.delete(0, tk.END)
            self.refrescar_lista()

    def manejador_completar(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.marcar_completada(seleccion[0])
            self.refrescar_lista()

    def manejador_eliminar(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self.refrescar_lista()

    def refrescar_lista(self):
        """Actualiza la lista con feedback visual (Verde para completado, Rojo pendiente)."""
        self.lista_box.delete(0, tk.END)
        for i, tarea in enumerate(self.servicio.obtener_todas()):
            if tarea.completada:
                texto = f"✔ [HECHO] {tarea.descripcion}"
                bg, fg = "#E8F5E9", "#2E7D32"  # Colores verdes suaves
            else:
                texto = f"✖ [PENDIENTE] {tarea.descripcion}"
                bg, fg = "#FFEBEE", "#C62828"  # Colores rojos suaves

            self.lista_box.insert(tk.END, texto)
            self.lista_box.itemconfig(i, bg=bg, fg=fg)