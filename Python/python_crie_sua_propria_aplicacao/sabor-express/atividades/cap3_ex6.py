#Autor = Frank Bruno
#Data = 06/04/2024

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

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
