from dataclasses import dataclass
import os
os.system("clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: int
    matricula: str
    endereco: str
    #def dados_funcionarios (self):
        #print (f"Nome: {self.nome}\nData de Admissão: {self.data_admissao}\nMatrícula: {self.matricula}\nEndereço: {self.endereco}")


@dataclass
class Clientes:
    nome: str
    data_nascimento: int
    endereco: str
    #def dados_clientes (self):
        #print (f"Nome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nEndereço: {self.endereco}")

lista_funcionarios = []
lista_clientes = []
QNT_PESSOAS = 2

for i in range (QNT_PESSOAS):
    print (f"Digite o {i+1}° funcionário: ")
    funcionario1 = Funcionario (
                                nome = input ("Digite seu nome: "),
                                data_admissao = input ("Data de admissão: "),
                                matricula = input ("Digite sua matricula: "),
                                endereco = input ("Digite seu endereço: "))
    lista_funcionarios.append(funcionario1)
    os.system ("clear")

for i in range (QNT_PESSOAS):
    print (f"Digite o {i+1}° cliente")
    cliente = Clientes (
                        nome = input ("Digite seu nome: "),
                        data_nascimento = input ("Data de nascimento: "),
                        endereco = input ("Digite seu endereço: "))
    lista_clientes.append(cliente)
    os.system ("clear")

    arquivo1 = 'dadosFuncionario.txt'
    arquivo2 = 'dadosCliente.txt'

    with open (arquivo1, 'a') as grava_dados:
        for funcionario1 in lista_funcionarios:
            grava_dados.write (f"{funcionario1.nome} | {funcionario1.data_admissao} | {funcionario1.matricula} | {funcionario1.endereco}")
    
    with open (arquivo2, 'a') as grava_dados2:
        for cliente in lista_clientes:
            grava_dados2.write (f"{cliente.nome} | {cliente.data_nascimento} | {cliente.endereco}")
    
    os.system("clear")
    print ("==DADOS SALVOS==")