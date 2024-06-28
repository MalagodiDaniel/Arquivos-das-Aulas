class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):        
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plimplim")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada!")

    def correr(self):
        print("zzzuumm")        

    def troca_marcha(self):
        print("tectectec")
        print("Marcha trocada!")

b1 = Bicicleta("azul", "caloi", 2020, 560)
b1.buzinar()
b1.correr()
b1.troca_marcha()
b1.parar() 
