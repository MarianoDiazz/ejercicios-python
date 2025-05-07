# Los widget son elementos graficos que utilizamos para
# diseñar la interfaz grafica de usuario

# LABEL(ETIQUETA)

import tkinter as tk

ventana = tk.Tk()
ventana.minsize(500, 400)

marco1 = tk.Frame(width=200, height=200, bg="lightblue")
# marco1.pack_propagate(False)  # evita que se achique

marco1.pack(padx=20)
etiqueta = tk.Label(marco1, text="buhito gey", bg="lightgreen", pady=20)
etiqueta.config(bg="red", font=("arial", 13, "bold"))
etiqueta.pack()

ventana.mainloop()
