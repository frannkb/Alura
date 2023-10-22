#include <stdio.h>
#include <stdlib.h>

// char mapa[5][10+1];
char** mapa;

int linhas;
int colunas;
 
int main()
{

    FILE* f;
    f = fopen("mapa.txt","r");
    if (f == 0)
    {
        printf("Erro na leitura do mapa \n");
        exit(1);
    }

    // pega primeira posicao do arquivo txt para trazer a quantidade de linhas e colunas
    fscanf(f, "%d%d", &linhas, &colunas);
    printf("Linhas %d colunas %d \n", linhas, colunas);

    //liberando espaco dinamicamente para a matriz mapa - linhas
    mapa =  malloc(sizeof(char*) * linhas);

    //liberando espaco dinamicamente para a matriz mapa - colunas
    for(int i = 0; i < linhas; i++){
        mapa[i] = malloc(sizeof(char) * (colunas+1));
    }



    for (int i = 0; i <= 4; i++){
        fscanf(f, "%s", mapa[i]);
    }

    for(int j = 0; j <=4; j++){
        printf("%s\n", mapa[j]);
    }    
    fclose(f);

    //liberando espaco das colunas
    for(int i = 0; i < linhas; i++){
        free(mapa[i]);
    }
    //liberando espaco das linhas
    free(mapa);

}