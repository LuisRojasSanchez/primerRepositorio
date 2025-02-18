package Progracion2;

import java.util.Scanner;

public class Expo {
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner scanner = new Scanner(System.in);

        // Pedir al usuario que ingrese un solo carácter
        System.out.print("Este programa busca en el codigo ASCII un caracter que ingrese el usuario");
        System.out.print("Por favor, ingresa un carácter: ");
        char letra = scanner.next().charAt(0); // Leemos solo el primer carácter ingresado

        // Mostrar el valor del carácter
        System.out.println("El carácter ingresado es: " + letra);

        // Mostrar el código ASCII del carácter
        int codigoAscii = (int) letra; // Convertir el carácter a su código ASCII
        System.out.println("El código ASCII de '" + letra + "' es: " + codigoAscii);
        System.out.print(
                "Este programa fue realizado por el ingeniero Dilan  Rivera Rosillo y Mancilla Gonzalez Francisco el dia 12/02/25");

        // Cerrar el scanner para liberar recursos
        scanner.close();
    }
}