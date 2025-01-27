class Biblioteca:
    def __init__(self, nombre_usuario, matricula_usuario):
        self.nombre_usuario = nombre_usuario
        self.matricula_usuario = matricula_usuario

        # Lista inicial de libros con algunos ejemplos.
        self.libros = [
            {"Autor": "Isabel Allende", "Nombre": "La casa de los espíritus", "Editorial": "Plaza & Janés"},
            {"Autor": "Miguel de Cervantes", "Nombre": "Don Quijote de la Mancha", "Editorial": "Francisco de Robles"},
            {"Autor": "Jane Austen", "Nombre": "Orgullo y prejuicio", "Editorial": "T. Egerton"}
        ]

    def ingresar_libro(self):
        autor = input("Ingrese el autor del libro: ")
        nombre = input("Ingrese el nombre del libro: ")
        editorial = input("Ingrese la editorial del libro: ")
        self.libros.append({"Autor": autor, "Nombre": nombre, "Editorial": editorial})
        print("\nLibro registrado exitosamente.\n")

    # Método para mostrar los libros y permitir al usuario seleccionar uno.
    def solicitar_libro(self):
        if not self.libros:
            print("No hay libros disponibles.\n")
            return

        # Mostrar la lista de libros disponibles
        for i, libro in enumerate(self.libros):
            print(f"{i + 1}. {libro['Nombre']}")

        # Pedir al usuario que seleccione un libro
        opcion = int(input("Seleccione el número del libro que desea solicitar: ")) - 1
        if 0 <= opcion < len(self.libros):
            libro = self.libros[opcion]
            print(f"\nLibro seleccionado:\nAutor: {libro['Autor']}\nNombre: {libro['Nombre']}\nEditorial: {libro['Editorial']}\n")
        else:
            print("Opción no válida.\n")

    # menú de opciones.
    def menu(self):
        while True:
            print(f"\nBienvenido, {self.nombre_usuario} (Matrícula: {self.matricula_usuario})")
            print("Menú:")
            print("1. Ingresar un libro")
            print("2. Solicitar un libro")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ingresar_libro()
            elif opcion == "2":
                self.solicitar_libro()
            elif opcion == "3":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.\n")

# Bucle para reiniciar el programa desde cero.
def iniciar_biblioteca():
    while True:
        # Pedir el nombre y la matrícula del usuario antes de iniciar el programa.
        nombre_usuario = input("Ingrese su nombre: ")
        matricula_usuario = input("Ingrese su matrícula: ")

        biblioteca = Biblioteca(nombre_usuario, matricula_usuario)
        biblioteca.menu()

        # Preguntar si el usuario desea comenzar de nuevo.
        reiniciar = input("¿Desea reiniciar el programa? (s/n): ").lower()
        if reiniciar != "s":
            print("Programa finalizado.")
            break

# Ejecutar el programa si este archivo es el principal.
if __name__ == "__main__":
    iniciar_biblioteca()
