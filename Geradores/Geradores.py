def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for d in meu_gerador(numeros=[1, 2, 3]):
    print(d)