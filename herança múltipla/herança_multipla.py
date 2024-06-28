class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

class Mamifero(Animal):
    pass


class Gato(Mamifero):
    pass


class Ave(Animal):
    pass

class qroqro(Ave):
    pass



gato = Gato(4)
print(gato)


