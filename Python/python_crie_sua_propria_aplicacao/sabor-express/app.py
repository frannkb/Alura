import os

#Criacao de lista para os cadastros dos restaurantes
# restaurantes = ['Pizza', 'Sushi']
restaurantes = [{'nome': 'Praca', 'categoria': 'Japonesa', 'ativo': False},
				{'nome': 'Pizza Suprema', 'categoria': 'pizza', 'ativo': True},
				{'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

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

#Funcao para retornar ao menu principal
def voltar_ao_menu():
	input('\nDigite uma tecla para voltar ao menu principal ')
	main()

def exibir_subtitulo(texto):
	os.system('clear')
	print(texto)
	print()

#Funcao para quando o programa receber um valor invalido
def opcao_invalida():
	print('Opcao invalida\n')
	voltar_ao_menu()

#Funcao para cadastar um novo restaurante
def cadastrar_novo_restaurante():
	exibir_subtitulo('Cadastros de novos restaurantes\n')
	nome_do_restaurante = input('Digite o nome para cadastro do restaurante: ')
	categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
	dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
	restaurantes.append(dados_do_restaurante)
	print(f'O restaurante {nome_do_restaurante} foi cadastrado!')
	voltar_ao_menu()

#Funcao para listar os restaurantes
def listar_restaurantes():
	exibir_subtitulo('Listando os restaurantes\n')
	for restaurante in restaurantes:
		nome_restaurante = restaurante['nome']
		categoria = restaurante['categoria']
		ativo = restaurante['ativo']
		print(f'.{nome_restaurante} | {categoria} | {ativo}')
	voltar_ao_menu()

#Ativando os restaurantes
def alternar_estado_restaurante():
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


#Funcao para escolher a opcao
def escolher_opcao():
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

#Funcao main onde puxara todas as opcoes
def main():
	os.system('clear')
	exibir_nome_do_programa()
	exibir_opcoes()
	escolher_opcao()

#Definindo como o programa principal
if __name__ == '__main__':
	main()
