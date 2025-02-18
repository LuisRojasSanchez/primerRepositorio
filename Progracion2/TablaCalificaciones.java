package Progracion2;

public class TablaCalificaciones {
    public static void main(String[] args) {
        // Definir una matriz bidimensional para representar las calificaciones
        String[] estudiantes = { "Juan", "María", "Carlos" };
        String[] materias = { "Matemáticas", "Ciencias", "Historia" };

        int[][] calificaciones = {
                { 85, 90, 88 }, // Calificaciones de Juan
                { 78, 95, 92 }, // Calificaciones de María
                { 89, 84, 91 } // Calificaciones de Carlos
        };

        // Imprimir la tabla de calificaciones
        System.out.println("Tabla de Calificaciones:\n");

        // Imprimir encabezados
        System.out.print("Estudiante\t");
        for (String materia : materias) {
            System.out.print(materia + "\t");
        }
        System.out.println("\n------------------------------------------------");

        // Imprimir las calificaciones
        for (int i = 0; i < calificaciones.length; i++) {
            System.out.print(estudiantes[i] + "\t"); // Nombre del estudiante
            for (int j = 0; j < calificaciones[i].length; j++) {
                System.out.print(calificaciones[i][j] + "\t\t"); // Calificación
            }
            System.out.println();
        }
    }
}
