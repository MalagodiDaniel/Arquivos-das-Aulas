def exibir_mensagem():
    print("ola mundo")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")


def exibir_mensagem_3(nome="Malagodi"):
  print(f"Seja bem vindo {nome}!")



exibir_mensagem()
exibir_mensagem_2(nome="José")
exibir_mensagem_3()
exibir_mensagem_3(nome= "Lucas")


##RETURN

def calculo(numeros):
    return sum(numeros)

print(calculo([10,25,157]))



##ARGUMENTOS NOMEADOS


def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro ("Lamborghini", "Aventador", 2022, "FGB-856")


salvar_carro(marca="BMW", modelo= "325i" , ano= 2023, placa="JHC-653")


##POSITIONAL ONLY 

def criar_carros(modelo, ano, placa, / ,  marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    

criar_carros("Civic", 2007, "DVB-1548", marca= "Honda", motor= 2.0, combustivel="gasolina") 









