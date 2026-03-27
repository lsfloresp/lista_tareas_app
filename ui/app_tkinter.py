import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from modelos.tarea import Tarea
from servicios.tarea_servicio import TareaServicio


class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Digital Profesional - Luis Flores")
        self.root.geometry("650x750")
        self.servicio = TareaServicio()

        # --- MATERIA ---
        tk.Label(root, text="Ingrese Materia:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
        self.entrada_materia = tk.Entry(root, width=50, font=("Arial", 11))
        self.entrada_materia.pack(pady=5)
        self.entrada_materia.focus()

        # --- TÍTULO TAREA (DESCRIPCIÓN) ---
        tk.Label(root, text="Título Tarea (Descripción):", font=("Arial", 10, "bold")).pack(pady=(5, 0))
        self.entrada_desc = tk.Entry(root, width=50, font=("Arial", 11))
        self.entrada_desc.pack(pady=5)

        # --- PRIORIDAD ---
        tk.Label(root, text="Prioridad (Alta / Media / Baja):", font=("Arial", 10, "bold")).pack(pady=(5, 0))
        self.entrada_prio = tk.Entry(root, width=50, font=("Arial", 11))
        self.entrada_prio.insert(0, "Media")
        self.entrada_prio.pack(pady=5)

        # --- FECHA ---
        tk.Label(root, text="Fecha de entrega (AAAA-MM-DD):", font=("Arial", 10, "bold")).pack(pady=(5, 0))
        self.entrada_fecha = tk.Entry(root, width=50, font=("Arial", 11))
        self.entrada_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Fecha actual por defecto
        self.entrada_fecha.pack(pady=5)

        self.entrada_fecha.bind("<Return>", lambda e: self.manejador_agregar())

        # Botón Principal
        tk.Button(root, text="Añadir a la Agenda", font=("Arial", 10, "bold"),
                  bg="#2196F3", fg="white", width=30, command=self.manejador_agregar).pack(pady=15)

        # Listbox para visualización
        self.lista_box = tk.Listbox(root, width=85, height=18, font=("Consolas", 9))
        self.lista_box.pack(pady=10, padx=20)

        self.lista_box.bind("<Double-1>", lambda e: self.manejador_completar())

        # Botones de gestión
        tk.Button(root, text="Marcar como Finalizada", bg="#C8E6C9", width=30, command=self.manejador_completar).pack(
            pady=2)
        tk.Button(root, text="Eliminar de la Agenda", bg="#FFCDD2", width=30, command=self.manejador_eliminar).pack(
            pady=5)

        self.refrescar_lista()

    def validar_fecha(self, fecha_str):
        """Verifica si la fecha tiene el formato correcto AAAA-MM-DD."""
        try:
            datetime.strptime(fecha_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def manejador_agregar(self):
        materia = self.entrada_materia.get().strip()
        desc = self.entrada_desc.get().strip()
        prio_raw = self.entrada_prio.get().strip().lower()
        fecha = self.entrada_fecha.get().strip()

        # 1. Validación de campos vacíos
        if not materia or not desc or not fecha:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return

        # 2. Validación de Prioridad Estricta
        prioridades_validas = ["alta", "media", "baja"]
        if prio_raw not in prioridades_validas:
            messagebox.showerror("Error de Prioridad", "Escriba solo: Alta, Media o Baja.")
            return

        # 3. Validación de Fecha Estricta
        if not self.validar_fecha(fecha):
            messagebox.showerror("Error de Fecha", "Formato incorrecto. Use: AAAA-MM-DD\nEjemplo: 2026-03-27")
            return

        # Si todo es válido, agregamos
        self.servicio.añadir_tarea(materia, desc, prio_raw.capitalize(), fecha)

        # Limpieza
        self.entrada_materia.delete(0, tk.END)
        self.entrada_desc.delete(0, tk.END)
        self.entrada_materia.focus()
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
        self.lista_box.delete(0, tk.END)
        for i, tarea in enumerate(self.servicio.obtener_todas()):

            if tarea.completada:
                prefijo = "✔ [HECHO]"
                texto = f"{prefijo} {tarea.titulo}: {tarea.descripcion} - Finalizada"
            else:
                prefijo = f"✖ [{tarea.prioridad.upper()}]"
                texto = f"{prefijo} {tarea.titulo}: {tarea.descripcion} - Vence: {tarea.fecha}"

            self.lista_box.insert(tk.END, texto)

            # Lógica de colores según prioridad
            if tarea.completada:
                bg, fg = "#E8F5E9", "#2E7D32"
            else:
                prio = tarea.prioridad.lower().strip()
                if prio == "alta":
                    bg, fg = "#FFEBEE", "#B71C1C"
                elif prio == "media":
                    bg, fg = "#FFFDE7", "#FBC02D"
                elif prio == "baja":
                    bg, fg = "#E3F2FD", "#1976D2"
                else:
                    bg, fg = "white", "black"

            self.lista_box.itemconfig(i, bg=bg, fg=fg)