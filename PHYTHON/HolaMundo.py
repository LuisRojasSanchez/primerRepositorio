import tkinter as tk

# Crear una instancia de la ventana principal
root = tk.Tk()

# Configurar propiedades de la ventana
root.title("Mi Aplicación")
root.geometry("300x200")

# Crear widgets dentro de la ventana principal
label = tk.Label(root, text="¡Hola, Mundo!")
label.pack()

button = tk.Button(root, text="Cerrar", command=root.quit)
button.pack()

# Iniciar el ciclo de eventos
root.mainloop()
