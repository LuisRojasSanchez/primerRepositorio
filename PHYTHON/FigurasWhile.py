import math

class FiguraGeometrica:
    def __init__(self, tipo):
        self.tipo = tipo
        self.area = 0
        self.perimetro = 0

    def calcular_area_perimetro(self):
        if self.tipo == "cuadrado":
            lado = float(input("Introduce la longitud del lado del cuadrado: "))
            self.area = lado ** 2
            self.perimetro = 4 * lado
            print("Área del cuadrado: ", self.area)
            print("Perímetro del cuadrado: ", self.perimetro)

        elif self.tipo == "triangulo":
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            lado1 = float(input("Introduce el primer lado del triángulo: "))
            lado2 = float(input("Introduce el segundo lado del triángulo: "))
            lado3 = float(input("Introduce el tercer lado del triángulo: "))
            self.area = (base * altura) / 2
            self.perimetro = lado1 + lado2 + lado3
            print("Área del triángulo: ", self.area)
            print("Perímetro del triángulo: ", self.perimetro)

        elif self.tipo == "circulo":
            radio = float(input("Introduce el radio del círculo: "))
            self.area = math.pi * radio ** 2
            self.perimetro = 2 * math.pi * radio
            print("Área del círculo: ", self.area)
            print("Perímetro del círculo: ", self.perimetro)

        else:
            print("Figura no reconocida.")

def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular área y perímetro de un cuadrado")
        print("2. Calcular área y perímetro de un triángulo")
        print("3. Calcular área y perímetro de un círculo")
        print("4. Salir")

        opcion = int(input("Elige una opción (1-4): "))

        if opcion == 1:
            figura = FiguraGeometrica("cuadrado")
            figura.calcular_area_perimetro()
        elif opcion == 2:
            figura = FiguraGeometrica("triangulo")
            figura.calcular_area_perimetro()
        elif opcion == 3:
            figura = FiguraGeometrica("circulo")
            figura.calcular_area_perimetro()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 4.")

# Ejecutar el menú
mostrar_menu()
