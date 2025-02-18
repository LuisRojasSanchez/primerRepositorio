estudiantes = ["Juan", "Maria", "Carlos"]
materias = ["Matematicas", "Ciencias", "Historia"]
autor=["Rojas Sanchez Luis Francisco"]
calificaciones = [
    [85, 90, 88],  # Calificaciones de Juan
    [78, 95, 92],  # Calificaciones de María
    [89, 84, 91]   # Calificaciones de Carlos
]

# Imprimir encabezados
print("Autor:Rojas Sanchez Luis Francisco")
print("Tabla de Calificaciones:\n")
print("Estudiante   ", end="")
for materia in materias:
    print(f"{materia:12}", end="")  # Ajuste de espacio
print("\n" + "-" * 45)

# Imprimir filas de calificaciones
for i in range(len(calificaciones)):
    print(f"{estudiantes[i]:12}", end="")  # Nombre del estudiante
    for j in range(len(calificaciones[i])):
        print(f"{calificaciones[i][j]:12}", end="")  # Calificación
    print()
    
