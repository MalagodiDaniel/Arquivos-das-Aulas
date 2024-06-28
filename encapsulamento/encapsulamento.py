#class conta:
    #def __init__(self, banco, saldo= 0):
        #self._saldo = saldo
        #self.banco = banco


    #def depositar(self, valor):
        #...
        #self._saldo += valor


    #def sacar(self, valor):
        #...
        #self._saldo -= valor

### Jeito de mostrar uma variável privada ###
    #def mostrar_saldo(self):
        #return self._saldo
### Jeito de mostrar uma variável privada ###


#Conta = conta("bradesco", 1000) 
#Conta.depositar(200)

#print(Conta._saldo)
#print(Conta.banco)
#print(Conta.mostrar_saldo())



####### Properties ######


class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)

        