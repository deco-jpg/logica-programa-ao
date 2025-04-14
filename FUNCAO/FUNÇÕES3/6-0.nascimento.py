import os
os.system ("cls")


def idade (nascimento):
    calculo_idade = nascimento - 2025
    return calculo_idade

nascimento = int (input("Qual ano você nasceu? "))

idade_final = idade (nascimento)

print (f"Sua idade é: {idade_final}")