class MeuIterador:
    def __init__(self, numero: list[int]):
        self.numero = numero
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numero[self.contador] 
            self.contador += 1 
            return numero * 2
        except IndexError:    
            raise StopIteration


for i in MeuIterador(numero=[50, 30, 120]):
    print(i)