class Lista:
    def __init__(self):  
        self.elementos = []

    def insertar(self, elemento, posicion):
        self.elementos.insert(posicion, elemento)

    def eliminar(self, posicion):
        if 0 <= posicion < len(self.elementos):
            return self.elementos.pop(posicion)
        return None

    def obtener(self, posicion):
        if 0 <= posicion < len(self.elementos):
            return self.elementos[posicion]
        return None

    def mostrar(self):
        return self.elementos


expo = Lista()
expo.insertar(10, 0)
expo.insertar(20, 1)
expo.insertar(30, 2)
expo.insertar(40, 3)
expo.insertar(50, 4)
expo.eliminar(4)

print(expo.mostrar())  
print("ESTE PROGRAMA FUE ELABORADO POR EL ING URIEL MUÑOZ")
