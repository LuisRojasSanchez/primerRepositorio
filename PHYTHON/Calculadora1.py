class Calculadora:
    def __init__ (self, num1,num2):
        self.a=num1
        self.b=num2
    def suma(self):
        d=self.a+self.b
        print("El resultado de la suma es: ", d)
        
objeto=Calculadora(1,2)
objeto.suma()