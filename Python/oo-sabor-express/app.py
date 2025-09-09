from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'Pao Frances')
# prato_italiano = Prato('Espaguete', 38.0, 'Prato italiano')
sobremesa_premium = Sobremesa('Pudim', 5.00, 'Doces', 'Médio', 'Melhor pudim da cidade' )


restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(sobremesa_premium)

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
sobremesa_premium.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()