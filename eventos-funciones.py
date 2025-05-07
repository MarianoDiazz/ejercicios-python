import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola")
ventana.config(width=300, height=300, bg="lightblue")
ventana.attributes("-alpha", 0.8)


def Onclick(e):
    print("Boton presionado")


button = tk.Button(ventana, text="Haz click derecho")
button.pack()

button.bind("<Button-3>", Onclick)

ventana.mainloop()
