#1 Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
def opcao_invalida():
	print('Opcao invalida!')


dados_pessoais = {'nome': 'Frank',
				  'idade': '32',
				  'cidade': 'Sao Paulo'}

print(dados_pessoais)

#Modificando a idade
resposta = input('Voce quer alterar sua idade? Responda S/N:')
if resposta == 's'or resposta == 'S':
	dados_pessoais.update({'idade': input('Digite uma nova idade: ')})
else:
	opcao_invalida()

#Adicionando um campo ao indice
add_campo = input('Deseja adicionar um novo campo ao indice S/N: ')
if add_campo == 'S' or add_campo == 's':
	novo_item = input('Digite uma novo item:')
	novo_valor = input('Digite um valor para o novo item:')
	dados_pessoais[novo_item] = novo_valor
else:
	opcao_invalida()

	# dados_pessoais['Profissao'] = 'ti'

#Removendo um campo do indice
remover_dado = input('Deseja remover algum item S/N: ')
if remover_dado == 'S' or remover_dado == 's':
	item = int(input('Escolha uma opcao \n 1 - nome \n 2 - idade \n 3 - cidade\n:'))
	if item == 1:
		del dados_pessoais['nome']
	elif item == 2:
		del dados_pessoais['idade']
	elif item == 3:
		del dados_pessoais['cidade']
	else:
		opcao_invalida()
else:
	opcao_invalida()

print(dados_pessoais)
