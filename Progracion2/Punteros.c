#include <stdio.h>

int main() {
    int x = 10; // Declaramos una variable
    int *ptr = &x; // Declaramos un puntero y le asignamos la dirección de memoria de x
    
    printf("Valor de x antes: %d\n", x); // Imprime el valor de x antes
    
    *ptr = 20; // Modificamos el valor de x a través del puntero
    
    printf("Valor de x después: %d\n", x); // Imprime el valor de x después

    return 0;
}
