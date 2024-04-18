#Autor = Frank Bruno
#Data = 06/04/2024

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

print('\n5 - Tabuada do numero escolhido\n')
number = int(input('Digite um numero:'))
n = number

for number in range(0,11):
	print(f'{n} x {number} = {number * n}')
