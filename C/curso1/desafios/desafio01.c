#include <stdio.h>

int main(){
	int x;
	int y;
	int resultado;

	printf("Jogo da multiplicacao.\n");
	printf("Digite seu primeiro numero?\n");
	scanf("%d", &x);
	printf("Digite seu segundo numero?\n");
	scanf("%d", &y);

	resultado = x*y;

	printf("A multiplicacao dos numeros e %d * %d = %d\n", x, y, resultado);
	

}
