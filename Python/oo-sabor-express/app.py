from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'japones')

restaurante_mexicano.alternar_estado()
restaurante_japones.receber_avaliacao('Frank', 10)
restaurante_japones.receber_avaliacao('Frank', 4)
restaurante_japones.receber_avaliacao('Frank', 2)


def main():
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()