import os

def logo_senai():
    os.system("cls")
    print ("==SENAI==")

logo_senai()
nome = input ("Digite seu nome: ")

logo_senai()
idade = int (input("Digite sua idade: "))

logo_senai()
print (f"Seu nome: {nome}")
print (f"Sua idade: {idade}")