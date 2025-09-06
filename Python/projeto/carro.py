from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, portas, marca, modelo):
        super().__init__(marca, modelo)
        self.portas = portas
        
    def __str__(self):
        return f'{self.portas} | {super().__str__()}'