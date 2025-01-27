matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Elemento en la fila 1, columna 2: ",matriz[0],[1])
print("Elemento en la fila 3, columna 1: ",matriz[2],[0])

print("Todos los elementos de la matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
