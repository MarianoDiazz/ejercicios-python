import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera ventana")
ventana.geometry("600x300+500+50")
ventana.minsize(500, 200)
# ventana.iconbitmap("rutaicono")
ventana.configure(bg="lightgreen")  # permite cambiar el color de fondo

# Transparencia
ventana.attributes("-alpha", 0.8)

# bucle principal de tkinter
ventana.mainloop()
