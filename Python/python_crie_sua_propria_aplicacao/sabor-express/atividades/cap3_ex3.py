#Autor = Frank Bruno
#Data = 06/04/2024

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
print('\n3 - Obtendo os numeros impares de 1 a 10 e somando-os\n')

result = 0

for numbers in range(0,10):
	if numbers % 2 != 0:
		print(numbers)
		result = numbers + result

print(f'A soma dos numeros impares é: {result}')
