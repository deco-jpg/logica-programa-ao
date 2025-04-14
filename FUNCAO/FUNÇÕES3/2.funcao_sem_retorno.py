import os

#Função sem retorno
def logo_senai():
    os.system("cls")
    print ("==SENAI==")

logo_senai() #chamando a função
nome = input ("Digite seu nome: ")

logo_senai() #chamando a função
idade = int (input("Digite sua idade: "))

logo_senai() #chamando a função
print (f"Seu nome: {nome}")
print (f"Sua idade: {idade}")