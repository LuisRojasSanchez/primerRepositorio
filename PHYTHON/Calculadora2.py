class Calculadora2:
    def __init__(self,num1,num2,num3):
        self.num1= num1 #atributo 1
        self.num2= num2 #atributo 2
        self.num3= num3 #atributo 3        
        
        #Metodos
    def suma(self):
        return self.num1+self.num2+self.num3
    def resta(self):
        return self.num1-self.num2-self.num3
    def multiplicar(self):
        return self.num1*self.num2*self.num3
    def dividir(self):
        return self.num1/self.num2
    def datos(self):
        return ("Carrera: Tics Escuela: TECNM CAPUS TLALPAN")
        
#Menu de la Calculadora
print("Por favor, elige una operacion:")
print("1 Suma")
print("2 Resta")
print("3 Multiplicacion")
print("4 Divicion")
print("5 Datos")

opcion=input("Selecciona una opcion colocando el numero corrempondiente ")


num1=float(input("Ingresar el primer numero:"))
num2=float(input("Ingresar el segundo numero:"))
num3=float(input("Ingresar el tercero numero:"))


op = Calculadora2(num1,num2,num3)
if opcion == '1':
    print("La Suma de los numeros", num1,num2,num3,"es igual a", op.suma())
elif opcion == '2':
    print("La Resta de los numeros", num1,num2,num3,"es igual a", op.resta())
elif opcion == '3':
    print("La Multiplicacion de los numeros", num1,num2,num3, "es igual a", op.multiplicar())
elif opcion == '4':
    print("La Divicion de los numeros 1 y 2", num1,num2,num3,"es igual a", op.dividir())
elif opcion == '5':
    print(op.datos())
else:
    print("Opcion no valida, intenta de nuevo")

