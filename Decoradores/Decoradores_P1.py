def calcular(operacao):
    def soma(a, b):
        return a + b
    
    def multiplicacao(a, b):
        return a * b


    def subtrair(a, b):
        return a - b
    
    
    def divisao(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtrair
        case "*":
            return multiplicacao
        case "/":
            return divisao
    


    


resultado1 = calcular("/")(200, 2)
resultado2 = calcular("-")(12, 7)
resultado3 = calcular("*")(200, 5)
resultado4 = calcular("+")(500, 200)

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)