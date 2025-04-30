from dataclasses import dataclass
import os
os.system ("cls")

@dataclass
class Usuario:
    nome: str
    idade: int
    peso: float
    altura: float
    def dados_finais(self):
        print (f"\nNome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura: {self.altura}")

lista_pessoas = []
QUANTIDADE_PESSOAS = 4

for i in range (QUANTIDADE_PESSOAS):
      pessoa = Usuario(
                        nome = input ("Digite seu nome: "),
                        idade = int (input("Digite sua idade: ")),
                        peso = float (input("Digite seu peso: ")),
                        altura = float (input("Digite sua altura: "))
                        )
      lista_pessoas.append(pessoa)
      os.system("cls")  


print ("===EXIBINDO RESULTADOS===")
for pessoa in lista_pessoas:
      pessoa.dados_finais()


