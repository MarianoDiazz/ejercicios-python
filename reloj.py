import tkinter as tk
import time

ventana = tk.Tk()
ventana.minsize(500, 400)
ventana.iconbitmap("favicon.ico")


etiq = tk.Label(ventana, text="Soy un Label prrr")
etiq.config(bg="lightblue", font=("Arial", 20, "bold"), fg="red")
etiq.pack()


def mostrarHora():
    etiq.config(text=time.strftime("%H: %M: %S"))
    ventana.after(1000, mostrarHora)


mostrarHora()

ventana.mainloop()
