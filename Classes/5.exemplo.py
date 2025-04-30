from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Informacao ():
    nome: str
    data: str
    rg: int
    cpf: int
    def exibir_dados (self):
        print (f"\nNome: {self.nome}\nData de Nascimento: {self.data}\nRG: {self.rg}\nCPF: {self.cpf}")
lista_pessoas = []
QUANTIDADE_PESSOAS = 5

for i in range (QUANTIDADE_PESSOAS):
    usuario = Informacao (
                            nome = input ("DIGITE SEU NOME: "),
                            data = input ("DIGITE SUA DATA DE NASCIMENTO: "),
                            rg = int (input("DIGITE SEU RG: ")),
                            cpf = int (input("DIGITE SEU CPF: "))
                        )
    lista_pessoas.append(usuario)
    os.system("cls")

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_funcionarios:
    for usuario in lista_pessoas:
        arquivo_funcionarios.write(f"Nome: {usuario.nome} | Nascimento: {usuario.data} | RG: {usuario.rg} | CPF: {usuario.cpf}\n")

for usuario in lista_pessoas:
    usuario.exibir_dados()