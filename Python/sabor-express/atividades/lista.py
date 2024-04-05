#Exercicios
# 1 - Crie uma lista para cada informação a seguir:
	# Lista de números de 1 a 10;
	# Lista com quatro nomes;
	# Lista com o ano que você nasceu e o ano atual.

print('Listando os numeros de 1 a 10\n')
for numero in range(1,11):
	print(numero)

print('\nListando os 4 nomes\n')
nomes = ['Teste1','Teste2','Teste3','Teste4']
for nome in nomes:
	print(nome)


print('\nListando o ano de nascimento e o ano atual\n')
ano_nascimento = 1991
ano_atual = 2024
idade = ano_atual - ano_nascimento

print(ano_nascimento)
print(ano_atual)
print(idade)


#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
import random

print('\nLista utilizando um loop for para percorrer os elementos da lista \n')
tamanho_lista = 5
lista_aleatoria = [random.randint(1,100) for _ in range(tamanho_lista)]

for lista in lista_aleatoria:
	print(lista)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
