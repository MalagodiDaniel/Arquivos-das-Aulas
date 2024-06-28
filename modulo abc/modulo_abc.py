from abc import ABC, abstractmethod

### Classe abstrata###


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando Tv...")
        print("Ligada")
    
    def desligar(self):
        print("Desligando TV...")
        print("Desligada")



 
controle = ControleTV()
controle.ligar()
controle.desligar()

