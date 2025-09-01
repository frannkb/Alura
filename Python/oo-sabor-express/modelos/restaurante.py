## dir(obj) = Retorna um alista de atributos e metodos disponiveis para aquele objeto, inclui tanto os atributos definidos pela classe quanto os herdados de classes pai e do python por padrão.
## vars(obj) = Retorna um dicionário com os atributos definidos diretamente no objeto(não lista métodos, nem atributos herdados)


class Restaurante:
    restaurantes = [ ]

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

#Restaurante.listar_restaurantes()

print(dir(restaurante_pizza))