import os

#Criacao de lista para os cadastros dos restaurantes
# restaurantes = ['Pizza', 'Sushi']
restaurantes = [{'nome': 'Praca', 'categoria': 'Japonesa', 'ativo': False},
				{'nome': 'Pizza Suprema', 'categoria': 'pizza', 'ativo': True},
				{'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
	''' Esta funçao apresenta o nome do programa '''
	print('\nSᴀʙᴏʀ Exᴘʀᴇss \n')

def exibir_opcoes():
	''' Esta funçao apresenta a lista de açoes para a usabilidade do app '''
	print('1. Cadastrar Restaurante')
	print('2. Listar Restaurante')
	print('3. Alternar estado do Restaurante')
	print('4. Sair \n')

def finalizar_app():
	''' Esta funçao limpa a tela do terminal e finaliza as açoes do app '''
	os.system('clear')
	print('Finalizando o app\n')

def voltar_ao_menu():
	''' Esta funçao retorna ao menu de açoes para usabilidade do app '''
	input('\nDigite uma tecla para voltar ao menu principal...')
	main()

def exibir_subtitulo(texto):
	''' Esta funçao realiza uma limpeza na tela e apresenta o titulo de cada item no app'''
	os.system('clear')
	linha = '*' * (len(texto))
	print(linha)
	print(texto)
	print(linha)
	print()

def opcao_invalida():
	''' Esta opcao valida se o valor da entrada e uma opcao valida '''
	print('Opcao invalida\n')
	voltar_ao_menu()

def cadastrar_novo_restaurante():
	''' Essa funçao e responsavel por cadastrar um novo restaurante
	
	Inputs:
	- Nome do restaurante
	- Categoria

	Outputs:
	- Adiciona um novo restaurante da lista de restaurantes

	'''
	exibir_subtitulo('Cadastros de novos restaurantes\n')
	nome_do_restaurante = input('Digite o nome para cadastro do restaurante: ')
	categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
	dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
	restaurantes.append(dados_do_restaurante)
	print(f'O restaurante {nome_do_restaurante} foi cadastrado!')
	voltar_ao_menu()

def listar_restaurantes():
	''' Esta funcao lista os restaurantes cadastrados '''
	exibir_subtitulo('Listando os restaurantes\n')
	print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
	for restaurante in restaurantes:
		nome_restaurante = restaurante['nome']
		categoria = restaurante['categoria']
		ativo = 'ativado' if restaurante['ativo'] else 'desativado'
		print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
	voltar_ao_menu()

def alternar_estado_restaurante():
	''' Esta funcao alterna o estado do restaurante ativo/inativo '''
	exibir_subtitulo('Alternando o estado do restaurante\n')
	#listar restaurantes para visualizar antes de editar
	for restaurante in restaurantes:
		nome_restaurante = restaurante['nome']
		ativo = restaurante['ativo']
		print({nome_restaurante},{ativo})

	nome_restaurante = input('\nDigite o nome do restaurante que deseja alternar o estado: ')
	restaurante_encontrado = False
	for restaurante in restaurantes:
		if nome_restaurante == restaurante['nome']:
			restaurante_encontrado = True
			restaurante['ativo'] = not restaurante ['ativo']
			mensagem = f'O Restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
			print(mensagem)
	if not restaurante_encontrado:
		print('O restaurante nao foi encontrado')

	voltar_ao_menu()

def escolher_opcao():
	''' Esta funcao apresenta as funcoes disponiveis para selecao no app '''
	try:
		opcao_escolhida = int(input('Escolha uma opcao: '))
		print(f'voce escolheu a opcao: {opcao_escolhida}')
		if opcao_escolhida == 1:
			cadastrar_novo_restaurante()
		elif opcao_escolhida == 2:
			listar_restaurantes()
		elif opcao_escolhida == 3:
			alternar_estado_restaurante()
		elif opcao_escolhida == 4:
			finalizar_app()
		else:
			opcao_invalida()
	except:
		opcao_invalida()

def main():
	''' Esta funcao define as chamadas das outras funcoes no app '''
	os.system('clear')
	exibir_nome_do_programa()
	exibir_opcoes()
	escolher_opcao()

''' A condicao abaixo define o programa como sendo o principal '''
if __name__ == '__main__':
	main()
