import tkinter as tk
from tkinter import ttk


class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación de Tareas Pendientes")
        self.master.geometry("400x400")
        self.master.iconbitmap("favicon.ico")  # Asegúrate de tener el icono favicon.ico
        self.master.configure(bg="white")  # Fondo blanco para el contenedor

        # Fondo con la imagen de Stitch
        self.bg_image = tk.PhotoImage(
            file="stitch.png"
        )  # Asegúrate de tener la imagen de Stitch llamada stitch.png
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Frame principal (con fondo transparente)
        self.frame = ttk.Frame(self.master, style="TFrame")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        ttk.Label(self.frame, text="Agregar Tarea", font=("Arial", 14, "bold")).pack(
            pady=10
        )

        # Nombre de la tarea
        ttk.Label(self.frame, text="Nueva Tarea:").pack(pady=5)
        self.entry_tarea = ttk.Entry(self.frame, width=30)
        self.entry_tarea.pack(pady=5)

        # Botón para agregar tarea
        self.boton_agregar = ttk.Button(
            self.frame, text="Agregar Tarea", command=self.agregar_tarea
        )
        self.boton_agregar.pack(pady=10)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(self.frame, height=10, font=("Arial", 12))
        self.lista_tareas.pack(pady=10, fill="both", expand=True)

        # Botón para eliminar tarea
        self.boton_eliminar = ttk.Button(
            self.frame, text="Eliminar Tarea Seleccionada", command=self.eliminar_tarea
        )
        self.boton_eliminar.pack(pady=5)

    def agregar_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            # Si la tarea está vacía, mostrar un mensaje de error
            self.show_error("La tarea no puede estar vacía.")

    def eliminar_tarea(self):
        try:
            seleccion = self.lista_tareas.curselection()  # Obtener tarea seleccionada
            if seleccion:
                self.lista_tareas.delete(seleccion)
            else:
                self.show_error("Por favor selecciona una tarea para eliminar.")
        except Exception as e:
            self.show_error(f"Ocurrió un error: {e}")

    def show_error(self, mensaje):
        error_window = tk.Toplevel(self.master)
        error_window.title("Error")
        error_window.geometry("250x100")
        label = ttk.Label(error_window, text=mensaje, font=("Arial", 12))
        label.pack(padx=20, pady=20)
        button = ttk.Button(error_window, text="Cerrar", command=error_window.destroy)
        button.pack(pady=5)


# Ejecutar la aplicación
ventana = tk.Tk()
app = TodoApp(ventana)
ventana.mainloop()
