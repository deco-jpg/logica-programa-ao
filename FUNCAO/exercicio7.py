import os
os.system("cls")

def metros_para_cm (metros):
    return metros * 100
metros = float (input("Digite o valor em metros: "))
valor_cm = metros_para_cm (metros)
print (f"{metros} metros é equivalente a: {valor_cm} centimetros")
