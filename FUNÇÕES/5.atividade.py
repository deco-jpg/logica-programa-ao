import os

# faça uma função sem retorno com o nome>:logo senai()
#limpando o terminal, o inserindo o: === SENAI DENDEZEIROS ===

#Solicitando ao usuario dois numeros
#cada um em uma variavel diferente
#crie uma função com retorno para somar os dois numeros informados pelo usuario.

def limpar_terminal (): #Criando função
    os.system ("cls")
    print ("===SENAI===")

def calculo_soma (numero_um, numero_dois): #Criando função
    soma = numero_um + numero_dois
    return soma
def subtrair (numero_um, numero_dois):
    return numero_um - numero_dois
def mult (numero_um, numero_dois):
    return numero_um * numero_dois
def dividir (numero_um, numero_dois):
    return numero_um / numero_dois

limpar_terminal () #Chamando função
nota_um = int (input("Digite o primeiro numero: "))
limpar_terminal () #Chamando função
nota_dois = int (input("Digite o segundo numero: "))

soma = calculo_soma (nota_um, nota_dois)
subtracao = subtrair (nota_um, nota_dois)
multiplicacao = mult (nota_um, nota_dois)
divisao = dividir (nota_um, nota_dois)
limpar_terminal () #Chamando função
print (f"Soma: {soma}")
print (f"Subtração: {subtracao}")
print (f"Multiplicação: {multiplicacao}")
print (f"Divisão: {divisao}")



