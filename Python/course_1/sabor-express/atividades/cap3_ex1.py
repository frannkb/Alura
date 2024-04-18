#Autor = Frank Bruno
#Data = 06/04/2024

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
