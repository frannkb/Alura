from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao
    
    def __str__(self):
        return f'{self._nome.ljust(20)} | {str(self._preco).ljust(20)} | {self.descricao.ljust(20)}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)