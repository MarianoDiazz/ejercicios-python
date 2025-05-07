import tkinter as tk


# Clase principal de la aplicación (usando POO)
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi primer programa con Tkinter")
        self.root.geometry("300x150")

        # Label
        self.label = tk.Label(root, text="Ingrese su nombre:")
        self.label.pack(pady=5)

        # Entry
        self.entrada = tk.Entry(root)
        self.entrada.pack(pady=5)

        # Botón
        self.boton = tk.Button(root, text="Saludar", command=self.saludar)
        self.boton.pack(pady=10)

        # Label para mostrar saludo
        self.saludo_label = tk.Label(root, text="")
        self.saludo_label.pack()

    def saludar(self):
        nombre = self.entrada.get()
        self.saludo_label.config(text=f"Hola, {nombre}!")


# Crear la ventana principal
root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
