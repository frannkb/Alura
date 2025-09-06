from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, tipo,marca, modelo):
        self._tipo = tipo
        super().__init__(marca, modelo)

    def __str__(self):
        return f'{super().__str__()} | {self._tipo}'