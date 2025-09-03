## dir(obj) = Retorna um alista de atributos e metodos disponiveis para aquele objeto, inclui tanto os atributos definidos pela classe quanto os herdados de classes pai e do python por padrão.
## vars(obj) = Retorna um dicionário com os atributos definidos diretamente no objeto(não lista métodos, nem atributos herdados)


class Restaurante:
    restaurantes = [ ]

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property #Modifica o atributo
    def ativo(self):
        return '▣' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Express', 'Italiana')


Restaurante.listar_restaurantes()