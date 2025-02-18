package Progracion2;

public class StringBuilderExample {

    public static void main(String[] args) {

        StringBuilder sb = new StringBuilder();

        // Concatenación de cadenas
        sb.append("Hola");
        sb.append(" ");
        sb.append("mundo");
        sb.append("!");

        System.out.println(sb.toString()); // Salida: "Hola mundo!"

        sb.replace(0, 4, "Adiós");

        System.out.println(sb.toString()); // Salida: "Adiós mundo!"

        // Eliminamos parte de la cadena
        sb.delete(5, 11);

        System.out.println(sb.toString());

        // Insertamos algo en la cadena
        sb.insert(5, " cruel");

        // Mostramos el resultado después de insertar
        System.out.println(sb.toString());
    }
}
