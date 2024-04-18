#Autor = Frank Bruno
#Data = 06/04/2024

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

print('\n7 - Apresentando a media dos valores apresentados na lista\n')
lista_valores_media= []
media_total = 0
try:
	total = sum(lista_valores_media)
	media_total = total / len(lista_valores_media)
except:
	print('A lista esta vazia\n')

print(f'A media dos valores apresentados e: {media_total}')
