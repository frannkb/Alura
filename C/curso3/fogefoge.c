#include <stdio.h>
#include <stdlib.h>

// char mapa[5][10+1];
char** mapa;

int linhas;
int colunas;
 
void    liberamapa(){
    //liberando espaco das colunas
    for(int i = 0; i < linhas; i++){
        free(mapa[i]);
    }
    //liberando espaco das linhas
    free(mapa);
}

void    alocamapa(){
    //liberando espaco dinamicamente para a matriz mapa - linhas
    mapa =  malloc(sizeof(char*) * linhas);

    //liberando espaco dinamicamente para a matriz mapa - colunas
    for(int i = 0; i < linhas; i++){
        mapa[i] = malloc(sizeof(char) * (colunas+1));
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
    fscanf(f, "%d%d", &linhas, &colunas);
    // printf("Linhas %d colunas %d \n", linhas, colunas);

    alocamapa();

    for (int i = 0; i <= 4; i++){
        fscanf(f, "%s", mapa[i]);
    }

    for(int j = 0; j <=4; j++){
        printf("%s\n", mapa[j]);
    }    
    fclose(f);
}

void    imprimemapa(){
    for(int i = 0; i <5; i++){
        printf("%s\n", mapa[i]);
    }
}

void    move(char direcao){
    int x;
    int y;

    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            if(mapa[i][j] == '@'){
                x = i;
                y = j;
                break;
            }
        }
    }

    switch(direcao){
        case 'a':
            mapa[x][y-1] = '@';
            break;
        case 'w':
            mapa[x-1][y] = '@';
            break;
        case 's':
            mapa[x+1][y] = '@';
            break;
        case 'd':
            mapa[x][y+1] = '@';
            break;
    }
    mapa[x][y] = '.';
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