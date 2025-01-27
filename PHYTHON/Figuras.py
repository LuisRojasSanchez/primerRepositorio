import math

# Clase base Figuras
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    # Método para mostrar el nombre de la figura
    def mostrar_nombre(self):
        print(f"El nombre de la figura es: {self.nombre}")
    
    # Método abstracto para área (será definido en cada subclase)
    def area(self):
        pass

    # Método abstracto para perímetro (será definido en cada subclase)
    def perimetro(self):
        pass

# Subclase Circulo
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def mostrar_caracteristicas(self):
        return f"Radio: {self.radio}"

# Subclase Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def mostrar_caracteristicas(self):
        return f"Lado: {self.lado}"

# Subclase Rectangulo
class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_caracteristicas(self):
        return f"Base: {self.base}, Altura: {self.altura}"

# Subclase Triangulo
class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def mostrar_caracteristicas(self):
        return f"Base: {self.base}, Altura: {self.altura}, Lados: {self.lado1}, {self.lado2}, {self.lado3}"

# Subclase Hexagono
class Hexagono(Figura):
    def __init__(self, lado):
        super().__init__("Hexágono")
        self.lado = lado

    def area(self):
        return (3 * math.sqrt(3) * (self.lado ** 2)) / 2

    def perimetro(self):
        return 6 * self.lado

    def mostrar_caracteristicas(self):
        return f"Lado: {self.lado}"

# Crear una lista de figuras
figuras = [
    Circulo(6),
    Cuadrado(4),
    Rectangulo(3, 6),
    Triangulo(3, 4, 3, 4, 5),
    Hexagono(2)
]

# Mostrar información de cada figura
for figura in figuras:
    figura.mostrar_nombre()
    print(figura.mostrar_caracteristicas())
    print(f'Área: {figura.area()}')
    print(f'Perímetro: {figura.perimetro()}\n')

