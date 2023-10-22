#include <stdio.h>

// variavel constante
#define NUMERO_DE_TENTATIVAS 5

int main(){
	// imprime o cabecalho do nosso jogo
	printf("**************************************\n");
	printf("Bem vindo ao nosso jogo de adivinhacao\n");
	printf("**************************************\n");	

	int numeroSecreto = 42;
	int chute;

	for(int i=1; i<=NUMERO_DE_TENTATIVAS; i++){
		printf("Numero de tentativas %d de %d\n", i, NUMERO_DE_TENTATIVAS);
		printf("Qual e o seu chute? \n");
		scanf("%d",&chute);
		printf("Seu chute foi %d\n", chute);	

		if(chute == numeroSecreto){
			printf("Voce acertou!\n\n");
			break;
		}else{
			if(chute > numeroSecreto){
				printf("Seu numero foi maior que o numero secreto\n");
			}
			if(chute < numeroSecreto){
				printf("Seu numero foi menor que o numero secreto\n");
			}
		}
	}

	return 0;
}