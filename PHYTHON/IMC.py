import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class IMC:
    def __init__(self, peso, altura, edad, sexo, nombre, enfermedad):
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.sexo = sexo
        self.nombre = nombre
        self.enfermedad = enfermedad

    def calcular_imc(self):
        if self.altura > 0:
            imc = self.peso / (self.altura ** 2)
            return round(imc, 2)
        else:
            return "Altura no válida"

    def estado_imc(self):
        imc = self.calcular_imc()
        if isinstance(imc, str):
            return imc
        elif imc < 18.5:
            return "Tu IMC es bajo."
        elif 18.5 <= imc <= 24.9:
            return "Tu IMC es normal."
        else:
            return "Tu IMC es alto."

class AplicacionIMC:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso de Datos del Paciente")
        # Establecer un tamaño mínimo para la ventana de ingreso de datos y permitir que se redimensione
        self.root.minsize(340, 200)  # Tamaño mínimo de la ventana
        self.crear_campos()

    def crear_campos(self):
        campos = ["Nombre", "Edad", "Peso (kg)", "Altura (m)", "Sexo", "Enfermedad"]
        self.entradas = {}

        for i, campo in enumerate(campos):
            tk.Label(self.root, text=campo + ":").grid(row=i, column=0, padx=50, pady=5, sticky="e")
            entrada = tk.Entry(self.root)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas[campo.lower()] = entrada

        tk.Button(self.root, text="Mostrar información del Paciente", command=self.mostrar_informacion_paciente).grid(
            row=len(campos), columnspan=2, pady=10
        )

    def mostrar_plato_del_buen_comer(self):
        # Crear una nueva ventana para mostrar el "Plato del Buen Comer"
        ventana_plato = tk.Toplevel(self.root)
        ventana_plato.title("Plato del Buen Comer")

        # Establecer la ubicación de la ventana del plato para evitar que se sobreponga
        ventana_plato.geometry("+720+0")  # Coloca la ventana a 500px desde la izquierda y 200px desde la parte superior
        ventana_plato.geometry("400x350")  # Coloca la ventana a 500px desde la izquierda y 200px desde la parte superior

        # Crear un Frame dentro de la nueva ventana
        frame_plato = tk.Frame(ventana_plato)
        frame_plato.pack(padx=10, pady=10)

        # Cargar y mostrar la imagen del plato del buen comer
        try:
            ruta_imagen_plato = "PHYTHON/images/platodelbuencomer.jpg"  # Ruta de la imagen
            imagen_plato = Image.open(ruta_imagen_plato)
            imagen_plato = imagen_plato.resize((300, 300))  # Ajuste del tamaño
            imagen_tk_plato = ImageTk.PhotoImage(imagen_plato)

            tk.Label(frame_plato, image=imagen_tk_plato).pack()
            ventana_plato.image = imagen_tk_plato  # Evitar que la imagen sea eliminada por el recolector de basura
        except Exception as e:
            tk.Label(frame_plato, text="Error al cargar la imagen del plato", fg="red").pack()

    def mostrar_informacion_paciente(self):
        try:
            nombre = self.entradas["nombre"].get()
            edad = int(self.entradas["edad"].get())
            peso = float(self.entradas["peso (kg)"].get())
            altura = float(self.entradas["altura (m)"].get())
            sexo = self.entradas["sexo"].get()
            enfermedad = self.entradas["enfermedad"].get()
        
            paciente = IMC(peso, altura, edad, sexo, nombre, enfermedad)
            self.mostrar_ventana_informacion(paciente)

            # Mostrar el plato del buen comer después de mostrar los datos del paciente
            self.mostrar_plato_del_buen_comer()

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos para todos los campos numéricos")

    def mostrar_ventana_informacion(self, paciente):
        ventana = tk.Toplevel(self.root)
        ventana.title("Información del Paciente")

        # Establecer tamaño mínimo para la ventana de información
        ventana.minsize(300, 300)  # Tamaño mínimo para la ventana de información
        ventana.geometry("+400+0")
        info_texto = (
            f"Datos del Paciente:\n\n"
            f"Nombre: {paciente.nombre}\n"
            f"Edad: {paciente.edad}\n"
            f"Peso: {paciente.peso}\n"
            f"Altura: {paciente.altura}\n"
            f"Sexo: {paciente.sexo}\n"
            f"Enfermedad: {paciente.enfermedad}\n"
            f"IMC: {paciente.calcular_imc()}\n"
        )

        tk.Label(ventana, text=info_texto, font=("Arial", 12), justify="center", padx=10, pady=10).pack()

        # Definir rutas para las imágenes según el estado de IMC
        ruta_bajo = "PHYTHON/images/flaco.jpg"     # Imagen para IMC bajo
        ruta_normal = "PHYTHON/images/normal.jpg"  # Imagen para IMC normal
        ruta_alto = "PHYTHON/images/gordo.jpg"     # Imagen para IMC alto

        # Determinar la imagen según el IMC calculado
        imc = paciente.calcular_imc()
        if isinstance(imc, str):  # Caso de error en la altura (texto "Altura no válida")
            ruta_imagen = None
        elif imc < 18.5:
            ruta_imagen = ruta_bajo
        elif 18.5 <= imc <= 24.9:
            ruta_imagen = ruta_normal
        else:
            ruta_imagen = ruta_alto

        # Cargar y mostrar la imagen si se ha definido una ruta válida
        if ruta_imagen:
            try:
                imagen = Image.open(ruta_imagen)
                imagen = imagen.resize((150, 150))
                imagen_tk = ImageTk.PhotoImage(imagen)

                tk.Label(ventana, image=imagen_tk).pack(pady=10)
                ventana.image = imagen_tk  # Evita que la imagen sea recolectada por el recolector de basura
            except Exception as e:
                tk.Label(ventana, text="Error al cargar la imagen", fg="red").pack()
        else:
            tk.Label(ventana, text="No se puede mostrar imagen por altura inválida", fg="red").pack()

        # Mostrar el estado del IMC
        estado_texto = paciente.estado_imc()
        tk.Label(ventana, text=estado_texto, font=("Arial", 12), fg="blue", padx=10, pady=10).pack()
        

# Inicialización de la aplicación
root = tk.Tk()
app = AplicacionIMC(root)
root.mainloop()
