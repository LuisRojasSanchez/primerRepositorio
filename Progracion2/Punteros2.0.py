def modificar_valor(ptr):
    ptr[0] = 20  # Modifica el valor en la posición 0 del "puntero"

x = [10]  # Usamos una lista para simular punteros

print("Valor de x antes:", x[0])

modificar_valor(x)  # Pasamos la referencia de la lista

print("Valor de x después:", x[0])
