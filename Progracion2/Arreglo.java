package Progracion2;

public class Arreglo {
    public static void main(String[] args) {

        // Declarar un arreglo unidimensional de enteros con 5 elementos
        int[] numeros = new int[5];

        numeros[0] = 10;
        numeros[1] = 20;
        numeros[2] = 30;
        numeros[3] = 40;
        numeros[4] = 50;

        // Imprimir los valores del arreglo
        System.out.println("Valores del arreglo:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elemento " + i + ": " + numeros[i]);
        }
        System.out.println("Programa de Rojas Sanchez Luis Francisco T31");
    }
}