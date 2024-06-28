class veiculo:
    def __init__(self, cor, placa, nro_rodas, marca):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
        self.marca = marca

    def ligar_motor(self):
        print("Ligando motor")
    pass

class motocicleta(veiculo):
    def corte_giro(self):
        print("RANDANDANDAN")
    pass

class carro(veiculo):
    pass


class caminhao(veiculo):
    def acelerando(self):
        print("vrrruuuumm")
    pass

moto = motocicleta("preta", "bfg123", 2, "Honda")
moto.ligar_motor()
moto.corte_giro()

Carro = carro("azul", "xdd456", 4, "Chevrolet")
Carro.ligar_motor()


Caminhao = caminhao("lilas", "vcx789", 12, "Volvo")
Caminhao.ligar_motor()
Caminhao.acelerando()