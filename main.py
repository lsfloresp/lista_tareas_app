import tkinter as tk
from ui.app_tkinter import AppTkinter

if __name__ == "__main__":
    root = tk.Tk()
    # Iniciamos la aplicación inyectando la raíz de Tkinter
    app = AppTkinter(root)
    root.mainloop()