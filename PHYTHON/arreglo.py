nombres = []  # Lista para almacenar los nombres
matricula = []  # Lista para almacenar las identificaciones

tamaño = 10  # Tamaño de los datos

for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificacion = input("Identificacion: ")

    nombres.append(nombre)  # Agrega el nombre a la lista `nombres`
    matricula.append(identificacion)  # Agrega la identificación a la lista `matricula`

# Mostrar los datos de las personas
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre: ", nombres[i])
    print("Identificacion: ", matricula[i])
