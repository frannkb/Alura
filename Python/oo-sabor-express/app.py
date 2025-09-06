from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'Pao Frances')
# prato_italiano = Prato('Espaguete', 38.0, 'Prato italiano')


restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()