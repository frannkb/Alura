#include <stdio.h>
#include <stdlib.h>
#include "fogefoge.h"

// char mapa[5][10+1];
struct mapa m;
 
void    liberamapa(){
    //liberando espaco das colunas
    for(int i = 0; i < m.linhas; i++){
        free(m.matriz[i]);
    }
    //liberando espaco das linhas
    free(m.matriz);
}

void    alocamapa(){
    //liberando espaco dinamicamente para a matriz mapa - linhas
    m.matriz =  malloc(sizeof(char*) * m.linhas);

    //liberando espaco dinamicamente para a matriz mapa - colunas
    for(int i = 0; i < m.linhas; i++){
        m.matriz[i] = malloc(sizeof(char) * (m.colunas+1));
    }
}

void    lemapa(){
    FILE* f;
    f = fopen("mapa.txt","r");
    if (f == 0)
    {
        printf("Erro na leitura do mapa \n");
        exit(1);
    }

    // pega primeira posicao do arquivo txt para trazer a quantidade de linhas e colunas
    fscanf(f, "%d%d", &m.linhas, &m.colunas);
    // printf("Linhas %d colunas %d \n", linhas, colunas);

    alocamapa();

    for (int i = 0; i <= 4; i++){
        fscanf(f, "%s", m.matriz[i]);
    }

    for(int j = 0; j <=4; j++){
        printf("%s\n", m.matriz[j]);
    }    
    fclose(f);
}

void    imprimemapa(){
    for(int i = 0; i <5; i++){
        printf("%s\n", m.matriz[i]);
    }
}

void    move(char direcao){
    int x;
    int y;

    for(int i = 0; i < m.linhas; i++){
        for(int j = 0; j < m.colunas; j++){
            if(m.matriz[i][j] == '@'){
                x = i;
                y = j;
                break;
            }
        }
    }

    switch(direcao){
        case 'a':
            m.matriz[x][y-1] = '@';
            break;
        case 'w':
            m.matriz[x-1][y] = '@';
            break;
        case 's':
            m.matriz[x+1][y] = '@';
            break;
        case 'd':
            m.matriz[x][y+1] = '@';
            break;
    }
    m.matriz[x][y] = '.';
}

int acabou(){
    return (0);
}

int main()
{
    lemapa();
do{
    imprimemapa();

    char comando;
    scanf(" %c", &comando);
    move(comando);
}  while(!acabou());

    liberamapa();
}