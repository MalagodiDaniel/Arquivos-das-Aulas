class Estudante:
    escola = "DIO"


    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

aluno1 = Estudante("Daniel", 5)
aluno2 = Estudante("Talita", 22)

print(aluno1)
print(aluno2)
