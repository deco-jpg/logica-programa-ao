from dataclasses import dataclass

import os
os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados (self):
        print (f"\nNome: {self.nome}, \nIdade: {self.idade}")

paciente1 = Paciente(
                    nome = input ("Digite seu nome: "),
                    idade = int (input("Digite sua idade: "))
                    )
print ("\n===Exibindo dados===")
paciente1.exibir_dados()