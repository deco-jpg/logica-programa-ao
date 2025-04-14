import os
os.system ("cls")

while True:
    idade = int (input("Digite sua idade: "))
    if idade <18:
        print ("Somente para maiores de 18 anos. \n")
    else:
        break
print ("Fim")