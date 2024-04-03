print('\nSᴀʙᴏʀ Exᴘʀᴇss \n')

print('1. Cadastrar Restaurante')
print('2. Listar Restaurante')
print('3. Ativar Restaurante')
print('4. Sair \n')

opcao_escolhida = int(input('Escolha uma opcao: '))
print(f'voce escolheu a opcao: {opcao_escolhida}')

if opcao_escolhida == 1:
	print('\nCadastrar Restaurante')
elif opcao_escolhida == 2:
	print('\nListar Restaurante')
elif opcao_escolhida == 3:
	print('\nAtivar Restaurante')
else:
	print('\nEncerrando o programa')
