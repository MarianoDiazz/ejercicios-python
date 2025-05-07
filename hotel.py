import tkinter as tk
from tkinter import ttk, messagebox


class HotelApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de Huéspedes")
        self.master.geometry("700x600")
        self.master.configure(bg="#f5f5f5")

        self.habitaciones = {}

        ttk.Label(
            master, text="Sistema de Registro Hotelero", font=("Helvetica", 16, "bold")
        ).pack(pady=10)

        self.frame_grid = ttk.Frame(master)
        self.frame_grid.pack(pady=10)
        self.crear_grid()

        self.frame_form = ttk.LabelFrame(master, text="Formulario de registro")
        self.frame_form.pack(padx=10, pady=10, fill="x")
        self.crear_formulario()

        self.frame_lista = ttk.LabelFrame(master, text="Huéspedes registrados")
        self.frame_lista.pack(padx=10, pady=10, fill="both", expand=True)
        self.crear_lista_huespedes()

    def crear_grid(self):
        for i in range(10):
            numero = i + 1
            btn = tk.Button(
                self.frame_grid,
                text=f"{numero}",
                width=6,
                height=3,
                bg="green",
                fg="white",
                font=("Arial", 10, "bold"),
            )
            btn.grid(row=i // 5, column=i % 5, padx=10, pady=10)
            self.habitaciones[numero] = {"boton": btn, "ocupado": False}

    def crear_formulario(self):
        # Nombre
        ttk.Label(self.frame_form, text="Nombre:").grid(
            row=0, column=0, sticky="e", padx=5, pady=5
        )
        self.entry_nombre = ttk.Entry(self.frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Tipo de habitación
        ttk.Label(self.frame_form, text="Tipo de habitación:").grid(
            row=1, column=0, sticky="e", padx=5, pady=5
        )
        self.tipo_var = tk.StringVar(value="Single")
        opciones = ["Single", "Doble", "Suite"]
        self.tipo_menu = ttk.OptionMenu(self.frame_form, self.tipo_var, *opciones)
        self.tipo_menu.grid(row=1, column=1, padx=5, pady=5)

        # Celular
        ttk.Label(self.frame_form, text="Celular:").grid(
            row=2, column=0, sticky="e", padx=5, pady=5
        )
        self.entry_cel = ttk.Entry(self.frame_form)
        self.entry_cel.grid(row=2, column=1, padx=5, pady=5)

        # Número de habitación
        ttk.Label(self.frame_form, text="Nro. Habitación (1-10):").grid(
            row=3, column=0, sticky="e", padx=5, pady=5
        )
        self.entry_hab = ttk.Entry(self.frame_form)
        self.entry_hab.grid(row=3, column=1, padx=5, pady=5)

        # Botón registrar
        btn_registrar = ttk.Button(
            self.frame_form, text="Registrar Huésped", command=self.registrar_huesped
        )
        btn_registrar.grid(row=4, column=0, columnspan=2, pady=10)

    def crear_lista_huespedes(self):
        self.lista_huespedes = tk.Listbox(
            self.frame_lista, height=8, font=("Arial", 10)
        )
        self.lista_huespedes.pack(padx=5, pady=5, fill="both", expand=True)

        # Botón para eliminar seleccionado
        btn_eliminar = ttk.Button(
            self.frame_lista,
            text="Eliminar Seleccionado",
            command=self.eliminar_huesped,
        )
        btn_eliminar.pack(pady=5)

    def registrar_huesped(self):
        nombre = self.entry_nombre.get()
        tipo = self.tipo_var.get()
        celular = self.entry_cel.get()

        try:
            nro_hab = int(self.entry_hab.get())
        except ValueError:
            messagebox.showerror("Error", "El número de habitación debe ser un número.")
            return

        if nro_hab not in self.habitaciones:
            messagebox.showerror("Error", "Número de habitación inválido.")
            return

        if self.habitaciones[nro_hab]["ocupado"]:
            messagebox.showwarning(
                "Ocupado", f"La habitación {nro_hab} ya está ocupada."
            )
            return

        # Agregar huésped a la lista
        self.lista_huespedes.insert(tk.END, f"{nombre} - Habitación {nro_hab} ({tipo})")
        self.habitaciones[nro_hab]["ocupado"] = True
        self.habitaciones[nro_hab]["boton"].config(bg="red")

        # Limpiar campos
        self.entry_nombre.delete(0, tk.END)
        self.entry_cel.delete(0, tk.END)
        self.entry_hab.delete(0, tk.END)

        messagebox.showinfo(
            "Registro exitoso", f"{nombre} registrado en habitación {nro_hab}."
        )

    def eliminar_huesped(self):
        seleccion = self.lista_huespedes.curselection()
        if not seleccion:
            messagebox.showwarning(
                "Seleccionar huésped", "Por favor, seleccioná un huésped para eliminar."
            )
            return

        index = seleccion[0]
        texto = self.lista_huespedes.get(index)

        try:
            nro_hab = int(texto.split("Habitación")[1].split("(")[0].strip())
        except:
            messagebox.showerror("Error", "No se pudo extraer el número de habitación.")
            return

        # Liberar habitación
        self.habitaciones[nro_hab]["ocupado"] = False
        self.habitaciones[nro_hab]["boton"].config(bg="green")

        # Eliminar de la lista
        self.lista_huespedes.delete(index)
        messagebox.showinfo(
            "Eliminado", f"Huésped eliminado y habitación {nro_hab} liberada."
        )


# Ejecutar app
ventana = tk.Tk()
ventana.iconbitmap("favicon.ico")
style = ttk.Style()
style.theme_use("clam")
app = HotelApp(ventana)
ventana.mainloop()
