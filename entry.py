import tkinter as tk

ventana = tk.Tk()
ventana.minsize(500, 400)
ventana.iconbitmap("favicon.ico")


def mostrarNombre():
    nombre = entrada.get()
    resultado.config(text="hola " + nombre)


etiq = tk.Label(ventana, text="Ingresa tu nombre")
etiq.config(bg="lightblue", font=("Arial", 14, "bold"), fg="red")
etiq.pack()

entrada = tk.Entry(ventana)
entrada.pack()
boton = tk.Button(ventana, text="Mostrar nombre", command=mostrarNombre)
boton.pack()
resultado = tk.Label(ventana, text="")
resultado.pack()


ventana.mainloop()
