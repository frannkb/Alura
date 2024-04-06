#Autor = Frank Bruno
#Data = 06/04/2024

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
import random
print('\n2 - Lista utilizando um loop for para percorrer os elementos da lista \n')
tamanho_lista = 5
lista_aleatoria = [random.randint(1,100) for _ in range(tamanho_lista)]

for lista in lista_aleatoria:
	print(lista)
