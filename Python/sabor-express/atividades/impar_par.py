#Programa para verificar se o numero e par ou impar
print('Digite um valor para identifcar se é impar ou par!\n')
valor = int(input('Digite um valor: '))

#Condicao
if valor % 2 == 0:
		print(f'O numero digitado: {valor} é par!')
else:
	print(f'Valor digitado {valor} é impar!')
