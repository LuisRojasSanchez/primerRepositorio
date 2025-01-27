class animal:
    def __init__(self, color, especie, raza, tamaño, alimentacion):
        self.color = color
        self.especie = especie
        self.raza = raza
        self.tamaño = tamaño
        self.alimentacion = alimentacion
        
    def Nombre(self):
        print("Mi nombre de animal es: ", type(self),__name__)
        
class pego (animal):
    def ColorPerro(self):
        print ("Soy un Perro de Color: ", self.color)
        
    def EspeciePerro(self):
        print ("Soy un Perro de Especie: ", self.especie)
        
    def RazaPerro(self):
        print ("Soy un Perro de Raza: ", self.raza)

    def TamañoPerro(self):
        print ("Soy un Perro de Animal: ", self.tamaño)

    def AlimentacionPerro(self):
        print ("Soy un Perro de Alimentacion: ", self.alimentacion)
        
        
mascota=pego("Miel", "Pego", "American Bully", "Mediana", "Pollo, Carne, Tortilla")
mascota.ColorPerro()
mascota.EspeciePerro()
mascota.RazaPerro()
mascota.TamañoPerro()
mascota.AlimentacionPerro()


class animal1:
    def __init__(self, color, especie, raza, tamaño, alimentacion):
        self.color = color
        self.especie = especie
        self.raza = raza
        self.tamaño = tamaño
        self.alimentacion = alimentacion
        
    def Nombre(self):
        print("Mi nombre de animal es: ", type(self),__name__)
        

class Gato (animal1):
    def ColorGato(self):
        print ("Soy un Gato de Color: ", self.color)
        
    def EspecieGato(self):
        print ("Soy un Gato de Especie: ", self.especie)
        
    def RazaGato(self):
        print ("Soy un Gato de Raza: ", self.raza)

    def TamañoGato(self):
        print ("Soy un Gato de Animal: ", self.tamaño)

    def AlimentacionGato(self):
        print ("Soy un Gato de Alimentacion: ", self.alimentacion)
        
        
mascota1=Gato("Miel", "Gato", "Siameses", "Cachorro", "Pollo, Carne, Gatina")
mascota1.ColorGato()
mascota1.EspecieGato()
mascota1.RazaGato()
mascota1.TamañoGato()
mascota1.AlimentacionGato()



class animal2:
    def __init__(self, color, especie, raza, tamaño, alimentacion):
        self.color = color
        self.especie = especie
        self.raza = raza
        self.tamaño = tamaño
        self.alimentacion = alimentacion
        
    def Nombre(self):
        print("Mi nombre de animal es: ", type(self),__name__)
        

class Pez (animal2):
    def ColorPez(self):
        print ("Soy un Pez de Color: ", self.color)
        
    def EspeciePez(self):
        print ("Soy un Pez de Especie: ", self.especie)
        
    def RazaPez(self):
        print ("Soy un Pez de Raza: ", self.raza)

    def TamañoPez(self):
        print ("Soy un Pez de Animal: ", self.tamaño)

    def AlimentacionPez(self):
        print ("Soy un Pez de Alimentacion: ", self.alimentacion)
        
        
mascota2=Pez("Naranja", "Pez", "Beta", "Pequeño", "Nose")
mascota2.ColorPez()
mascota2.EspeciePez()
mascota2.RazaPez()
mascota2.TamañoPez()
mascota2.AlimentacionPez()
