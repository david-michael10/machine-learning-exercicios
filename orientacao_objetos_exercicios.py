class Aluno:
    def __init__(self,nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def mostrar_notas(self):
        return f"{self.nome} tirou {self.nota1} e {self.nota2}"

    def resultado(self):
        if self.calcular_media() >= 6:
            resul = "Aprovado"
        else:
            resul = "Reprovado"
        return (f"Soma Total = {self.nota1 + self.nota2}\n"
                f"Média = {(self.nota1 + self.nota2) / 2}\n"
                f"Resultado = {resul}\n")

pedro = Aluno("Pedro", 8, 7)
print(pedro.mostrar_notas())
print(pedro.resultado())

alicia = Aluno("Alicia", 5, 6)
print(alicia.mostrar_notas())
print(alicia.resultado())