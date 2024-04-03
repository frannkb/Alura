
print('Quadrante do plano cartesiano\n')
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

if x > 0 and y > 0:
	resultado = 'Primeiro quadrante'
elif x < 0 and y > 0:
	resultado = 'Segundo quadrante'
elif x < 0 and y < 0:
	resultado = 'Terceiro quadrante'
elif x > 0 and y < 0:
	resultado = 'Quarto quadrante'
else:
	resultado = 'O Ponto esta localizado no eixo ou origem'

print(f'O plano cartesiano se encontra no: {resultado}')
