import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera ventana")
ventana.geometry("600x300+500+50")


# Los frames son practicamente para ir ordenando el codigo
frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bd=5, bg="red")
frame1.pack()

frame2 = tk.Frame(frame1)
frame2.configure(width=100, height=100, bd=2, bg="blue")

button = tk.Button(frame1, text="hola pa")
button.pack()

frame2.pack()  # EL pacj es clave para saber el orden de los elemtos

ventana.mainloop()
