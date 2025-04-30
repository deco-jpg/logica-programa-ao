from dataclasses import dataclass
import os
os.system ("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    def exibir_dados(self):
        print (f"\nNome: {self.nome}\n Idade: {self.idade}")

lista_pacientes = []
QUANTIDADE_PACIENTES = 2

for i in range (QUANTIDADE_PACIENTES):
    paciente = Paciente(
                        nome = input ("Digite seu nome: "),
                        idade = int (input("Digite sua idade: "))   
                        )
    lista_pacientes.append(paciente)
    os.system("cls")

nome_arquivo = "Dados_pacientes.txt"
with open(nome_arquivo, "a") as arquivo_paciente:
     for paciente in lista_pacientes:
          arquivo_paciente.write(f"{paciente.nome}, {paciente.idade}\n")

print ("===Exibindo Resultados===")
for paciente in lista_pacientes:
    paciente.exibir_dados()