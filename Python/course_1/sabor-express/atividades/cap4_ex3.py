#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

chave_especifica = {'chave1':231, 'chave2': 324, 'chave4': 543}

for chave in chave_especifica:
	if chave_especifica[chave] == 231:
		print('chave existente')
	else:
		print('chave nao existente')
