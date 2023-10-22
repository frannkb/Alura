// Imprimindo uma matriz
// Imprima a matriz de inteiros abaixo
// int numeros[20][10], para isso use dois for s.

#include <stdio.h>

int main()
{
    char mapa[20][10];

    for(int i = 0; i < 20; i++)
    {
        for( int j = 0; j < 10; j++)
        {
            printf("%d ", mapa[i][j]);
        }
        printf("\n");
    }
}