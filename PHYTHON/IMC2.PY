import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class IMC:
    def __init__(self, peso, altura, edad, sexo, nombre, enfermedad, presion):  # Se agrega presion
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.sexo = sexo
        self.nombre = nombre
        self.enfermedad = enfermedad
        self.presion = presion  # presion

    def calcular_imc(self):
        if self.altura > 0:
            imc = self.peso / (self.altura ** 2)
            return round(imc, 2)
        else:
            return "Altura no valida"

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

    def estado_presion(self):  # presion
        try:
            presion = float(self.presion)
            if presion < 120:
                return "Presion normal"
            elif 120 <= presion <= 129:
                return "Presion elevada"
            else:
                return "Presion alta"
        except ValueError:
            return "Presion no valida"

class AplicacionIMC(IMC):
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso de Datos del Paciente")
        # Establecer un tamano minimo para la ventana de ingreso de datos y permitir que se redimensione
        self.root.minsize(340, 200)
        self.crear_campos()

    def crear_campos(self):
        # Lista de campos para crear etiquetas y entradas
        campos = ["Nombre", "Edad", "Peso (kg)", "Altura (en metros)", "Sexo", "Enfermedad", "Presion arterial (mmHg)"]  # Linea 42
        self.entradas = {}

        for i, campo in enumerate(campos):
            tk.Label(self.root, text=campo + ":").grid(row=i, column=0, padx=50, pady=5, sticky="e")
            entrada = tk.Entry(self.root)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas[campo.lower()] = entrada

        tk.Button(self.root, text="Mostrar informacion del Paciente", command=self.mostrar_informacion_paciente).grid(
            row=len(campos), columnspan=2, pady=10
        )

    def mostrar_plato_del_buen_comer(self, paciente):
        # Crear una nueva ventana para mostrar el "Plato del Buen Comer"
        ventana_plato = tk.Toplevel(self.root)
        ventana_plato.title("Plato del Buen Comer")
        ventana_plato.geometry("+720+0")
        ventana_plato.geometry("600x500")

        frame_plato = tk.Frame(ventana_plato)
        frame_plato.pack(padx=10, pady=10)

        # Mostrar el nombre, edad y IMC
        texto_datos = f"Nombre: {paciente.nombre}\nEdad: {paciente.edad}\nIMC: {paciente.calcular_imc()}"
        tk.Label(frame_plato, text=texto_datos, font=("Arial", 12), justify="center", padx=10, pady=10).pack()

        # Cargar y mostrar la imagen del plato del buen comer
        try:
            ruta_imagen_plato = "PHYTHON/images/platodelbuencomer.jpg"
            imagen_plato = Image.open(ruta_imagen_plato)
            imagen_plato = imagen_plato.resize((400, 400))
            imagen_tk_plato = ImageTk.PhotoImage(imagen_plato)

            tk.Label(frame_plato, image=imagen_tk_plato).pack()
            ventana_plato.image = imagen_tk_plato
        except Exception as e:
            tk.Label(frame_plato, text="Error al cargar la imagen del plato", fg="red").pack()

    def mostrar_informacion_paciente(self):
        try:
            # Capturar datos de las entradas
            nombre = self.entradas["nombre"].get()
            edad = int(self.entradas["edad"].get())
            peso = float(self.entradas["peso (kg)"].get())
            altura = float(self.entradas["altura (en metros)"].get())
            sexo = self.entradas["sexo"].get()
            enfermedad = self.entradas["enfermedad"].get()
            presion = self.entradas["presion arterial (mmhg)"].get()  # Linea 64

            # Crear objeto IMC con los datos del paciente
            paciente = IMC(peso, altura, edad, sexo, nombre, enfermedad, presion)  # Se le agrega presion
            self.mostrar_ventana_informacion(paciente)
            self.mostrar_ventana_imc(paciente)  # Mostrar ventana de IMC

            self.mostrar_plato_del_buen_comer(paciente)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores validos para todos los campos numericos")

    def mostrar_ventana_informacion(self, paciente):
        ventana_info = tk.Toplevel(self.root)
        ventana_info.title("Informacion del Paciente")
        ventana_info.minsize(300, 300)
        ventana_info.geometry("+400+0")

        # Crear texto con la informacion del paciente
        info_texto = (
            f"Datos del Paciente:\n\n"
            f"Nombre: {paciente.nombre}\n"
            f"Edad: {paciente.edad}\n"
            f"Peso: {paciente.peso}\n"
            f"Altura: {paciente.altura}\n"
            f"Sexo: {paciente.sexo}\n"
            f"Enfermedad: {paciente.enfermedad}\n"
            f"Presion: {paciente.presion} mmHg\n"  # Presion y su medida
            f"Estado de Presion: {paciente.estado_presion()}"  # Se le agrega presion
        )

        tk.Label(ventana_info, text=info_texto, font=("Arial", 12), justify="center", padx=10, pady=10).pack()

    def mostrar_ventana_imc(self, paciente):
        ventana_imc = tk.Toplevel(self.root)
        ventana_imc.title("Resultado del IMC")
        ventana_imc.geometry("+400+350")
        ventana_imc.geometry("200x300")

        # Definir rutas para las imagenes segun el estado de IMC
        ruta_bajo = "PHYTHON/images/flaco.jpg"
        ruta_normal = "PHYTHON/images/normal.jpg"
        ruta_alto = "PHYTHON/images/gordo.jpg"

        imc = paciente.calcular_imc()
        if isinstance(imc, str):
            ruta_imagen = None
        elif imc < 18.5:
            ruta_imagen = ruta_bajo
        elif 18.5 <= imc <= 24.9:
            ruta_imagen = ruta_normal
        else:
            ruta_imagen = ruta_alto

        # Mostrar el valor del IMC
        tk.Label(ventana_imc, text=f"IMC: {imc}", font=("Arial", 12), padx=10, pady=10).pack()

        # Cargar y mostrar la imagen si se ha definido una ruta valida
        if ruta_imagen:
            try:
                imagen = Image.open(ruta_imagen)
                imagen = imagen.resize((150, 150))
                imagen_tk = ImageTk.PhotoImage(imagen)

                tk.Label(ventana_imc, image=imagen_tk).pack(pady=10)
                ventana_imc.image = imagen_tk
            except Exception as e:
                tk.Label(ventana_imc, text="Error al cargar la imagen", fg="red").pack()
        else:
            tk.Label(ventana_imc, text="No se puede mostrar imagen por altura invalida", fg="red").pack()

        # Mostrar el estado del IMC
        estado_texto = paciente.estado_imc()
        tk.Label(ventana_imc, text=estado_texto, font=("Arial", 12), fg="blue", padx=10, pady=10).pack()

# Inicializacion de la aplicacion
root = tk.Tk()
app = AplicacionIMC(root)
root.mainloop()
