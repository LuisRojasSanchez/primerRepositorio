package Progracion2;

import java.util.Scanner;

// Este programa solicita al usuario que ingrese diferentes tipos de datos primitivos en Java
// y luego los muestra junto con su tamaño en bytes.
// Además, incluye información de identificación del programador y del contexto académico.

public class DatosPrimitivos {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in); // Lo usamos para leer los datos ingresados por el usuario

        // Solicitar datos al usuario
        System.out.print("Usuario ingrese un número entero (int): ");
        int entero = scanner.nextInt();

        System.out.print("Usuario ingrese un carácter (char): ");
        char caracter = scanner.next().charAt(0); // Leer solo un carácter

        System.out.print("Usuario ingrese un número largo (long): ");
        long largo = scanner.nextLong();

        System.out.print("Usuario ingrese un número decimal (float): ");
        float real = scanner.nextFloat();

        System.out.print("Usuario ingrese un número decimal (double): ");
        double doble = scanner.nextDouble();

        System.out.print("Usuario ingrese un número pequeño (byte): ");
        byte pequeno = scanner.nextByte();

        System.out.print("Usuario ingrese un número corto (short): ");
        short corto = scanner.nextShort();

        System.out.print("Usuario ingrese un número tipo word (short): ");
        short word = scanner.nextShort();

        // Mostrar los resultados con su tamaño en bytes
        System.out.println("\nResultados:");
        System.out.println("El valor de entero (int) es: " + entero + " y su tamaño es: " + Integer.BYTES + " bytes");
        System.out.println(
                "El valor de carácter (char) es: " + caracter + " y su tamaño es: " + Character.BYTES + " bytes");
        System.out.println("El valor de largo (long) es: " + largo + " y su tamaño es: " + Long.BYTES + " bytes");
        System.out.println("El valor de real (float) es: " + real + " y su tamaño es: " + Float.BYTES + " bytes");
        System.out.println("El valor de doble (double) es: " + doble + " y su tamaño es: " + Double.BYTES + " bytes");
        System.out.println("El valor de pequeño (byte) es: " + pequeno + " y su tamaño es: " + Byte.BYTES + " bytes");
        System.out.println("El valor de corto (short) es: " + corto + " y su tamaño es: " + Short.BYTES + " bytes");
        System.out.println("El valor de word (short) es: " + word + " y su tamaño es: " + Short.BYTES + " bytes");
        System.err.println(
                "Este programa solicita al usuario que ingrese diferentes tipos de datos primitivos en Java y muestra su tamaño en bytes.");

        // Datos
        System.out.println("Rojas Sanchez Luis Francisco T31");
        System.out.println("Matrícula: 241200016");
        System.out.println("Fecha: 12 de febrero de 2025");
        System.out.println("Materia: Estructura y organización de datos");
        System.out.println("Tecnológico Nacional de México Campus Tlalpan");
        System.out.println("Carrera Tics");

        scanner.close();
    }
}
