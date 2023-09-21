# Resposta
class Aluno:
  nome = None
  nota1 = None
  nota2 = None
  def __init__ (self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2

  def calculoMedia (self):
    resultado = (self.nota1 + self.nota2)/2
    return resultado

  def __str__(self):
    return f"{self.nome} {self.nota1} {self.nota2}"

  def resultado(self):
    resultado_media = self.calculoMedia()
    if resultado_media >= 0 and resultado_media < 6:
      return("O ALUNO foi reprovado")
    else:
      return("O ALUNO foi aprovado")

aluno1 = Aluno("Jhone", 10, 10)
print("A media do aluno(a) foi de: ",aluno1.calculoMedia())
print("Os valores do atributos são: ",aluno1.__str__())
print(aluno1.resultado())
print("")
aluno2 = Aluno("Larissa",9,8)
print("A media do aluno(a) foi de: ",aluno2.calculoMedia())
print("Os valores do atributos são: ",aluno2.__str__())
print(aluno2.resultado())
