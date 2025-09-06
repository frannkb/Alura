from carro import Carro
from moto import Moto

Argo = Carro(3,'Fiat','Argo')
Fastback = Carro(4,'Fiat', 'Fastback')
Honda = Moto ('2 rodas','Honda','Honda 1000c')


if Argo._ligado == False and Argo.marca == 'Fiat':
    Argo._ligado == True

def main():
    print(Argo)
    print(Fastback)
    print(Honda)

if __name__ == '__main__':
    main()