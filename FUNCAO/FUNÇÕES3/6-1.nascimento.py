import os
from datetime import date 
from datetime import time
os.system ("cls")

def idade (nascimento):
    calculo_idade = date.today().year - nascimento
    return calculo_idade

nascimento = int (input("Qual ano você nasceu? "))

idade_final = idade (nascimento)

print (f"Sua idade é: {idade_final}")
time()