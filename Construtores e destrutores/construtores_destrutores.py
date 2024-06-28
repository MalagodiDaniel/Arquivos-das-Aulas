class curitia:
    def __init__(self, nome, camisa, contrato=True):
        print("Defesa 2012...")
        self.nome = nome
        self.camisa = camisa
        self.contrato = contrato

    def falar(self):
        print("Meu nome é Gigante Cássio")

    def nro_camisa(self):
        print("E eu usava a camisa 12 do cortinas")

    def temp_contrato(self):
        print("Mas não aceitei ser reserva do time")
        print("Vou sair desse time merda e pobre")
        print("Adeus filé torcida")


    def __del__(self):
        print("Cassião meuteu o pé para o Cruzeiro")
        

c = curitia("Cássio", 12)
c.falar()
c.nro_camisa()
c.temp_contrato()
