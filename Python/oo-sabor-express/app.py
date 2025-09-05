from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
prato_italiano = Prato('Espaguete', 38.0, 'Prato italiano')


def main():
    print(bebida_suco)
    print(prato_italiano)  

if __name__ == '__main__':
    main()