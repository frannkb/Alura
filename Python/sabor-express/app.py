import os

#Funcao para exibir nome do progama
def exibir_nome_do_programa():
	print('\nSᴀʙᴏʀ Exᴘʀᴇss \n')

#Funcao para exibir as opceos
def exibir_opcoes():
	print('1. Cadastrar Restaurante')
	print('2. Listar Restaurante')
	print('3. Ativar Restaurante')
	print('4. Sair \n')

#Funcao para finalizar app
def finalizar_app():
	os.system('clear')
	print('Finalizando o app\n')

#Funcao para quando o programa receber um valor invalido
def opcao_invalida():
	print('Opcao invalida\n')
	input('Digite uma tecla para voltar ao menu principal')
	main()

#Funcao para escolher a opcao
def escolher_opcao():
	try:
		opcao_escolhida = int(input('Escolha uma opcao: '))
		print(f'voce escolheu a opcao: {opcao_escolhida}')
		if opcao_escolhida == 1:
			print('\nCadastrar Restaurante')
		elif opcao_escolhida == 2:
			print('\nListar Restaurante')
		elif opcao_escolhida == 3:
			print('\nAtivar Restaurante')
		elif opcao_escolhida == 4:
			finalizar_app()
		else:
			opcao_invalida()
	except:
		opcao_invalida()

#Funcao main onde puxara todas as opcoes
def main():
	os.system('clear')
	exibir_nome_do_programa()
	exibir_opcoes()
	escolher_opcao()

#Definindo como o programa principal
if __name__ == '__main__':
	main()
