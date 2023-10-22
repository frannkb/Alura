#include <stdio.h>

int main()
{
    int numeros[5][10];

    int** copia = numeros;

    printf("%d", copia[0][0]);
}