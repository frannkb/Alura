def espacamento():
	print('\n------------------------------------------------------------')

#Exercicios
# 1 - Crie uma lista para cada informação a seguir:
	# Lista de números de 1 a 10;
	# Lista com quatro nomes;
	# Lista com o ano que você nasceu e o ano atual.
espacamento()
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
espacamento()
print('\n2 -Lista utilizando um loop for para percorrer os elementos da lista \n')
tamanho_lista = 5
lista_aleatoria = [random.randint(1,100) for _ in range(tamanho_lista)]

for lista in lista_aleatoria:
	print(lista)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
espacamento()
print('\n3 - Obtendo os numeros impares de 1 a 10 e somando-os\n')

result = 0

for numbers in range(0,10):
	if numbers % 2 != 0:
		print(numbers)
		result = numbers + result

print(f'A soma dos numeros impares é: {result}')

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
espacamento()
print('\n4 - Imprimindo os numeros de 1 a 10 em ordem decrescente\n')

for number in range(10,0,-1):
	print(number)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
espacamento()
print('\n5 - Tabuada do numero escolhido\n')
number = int(input('Digite um numero:'))
n = number

for number in range(0,11):
	print(f'{n} x {number} = {number * n}')

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

espacamento()
print('\n6 - Somando todos os numeros da lista\n')
# lista_numeros = [random.randint(1,100) for _ in range(tamanho_lista)]

lista_numeros=[1,2,3,'a',6]

soma = 0
for number6 in lista_numeros:
	try:
		soma = number6 + soma
	except:
		print(f'Ha um valor nao correspondente em sua lista: {number6}')

print(f'\nA soma dos numeros e {soma}')

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

espacamento()
print('\n7 - Apresentando a media dos valores apresentados na lista\n')
lista_valores_media= []
media_total = 0
try:
	total = sum(lista_valores_media)
	media_total = total / len(lista_valores_media)
except:
	print('A lista esta vazia\n')

print(f'A media dos valores apresentados e: {media_total}')


