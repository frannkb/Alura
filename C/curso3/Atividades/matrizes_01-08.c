// Alocar uma matriz de 05 linhas e 10 colunas dinamicamente


#include <stdio.h>
#include <stdlib.h>

int main(){

    int linhas = 5;
    int colunas = 10;

    int** matriz = malloc(sizeof(int*) * linhas);

    for(int i = 0; i < linhas; i++){
        matriz[i] = malloc(sizeof(int) * (colunas + 1));
    }

        for(int i = 0; i < linhas; i++){
            for(int j = 0; j < colunas; j++){
               printf("%d %d", i, j);
            }
            printf("\n");
        }


    for(int i = 0; i < linhas; i++){
        free(matriz[i]);
    }

    free(matriz);
}