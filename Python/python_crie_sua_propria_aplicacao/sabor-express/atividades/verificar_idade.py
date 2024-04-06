#Programa para verificar sua idade
print('Iremos classificar sua faixa etaria\n')
idade = int(input('Digite sua idade: '))

if  idade >= 0 and idade <= 12:
	print('Voce é uma crianca')
elif idade >= 13 and idade <=18:
	print('Voce e um adolescente')
else:
	print('Voce e um adulto')
