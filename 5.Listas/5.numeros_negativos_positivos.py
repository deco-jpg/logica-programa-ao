import os
os.system("cls |clear ")

positivos = 0
negativos = 0
lista = []
QUANTIDADE_NUMERO = 5
for i in range (QUANTIDADE_NUMERO):
    algarismo = int (input("DIGITE UM NÚMERO: "))
    lista.append (algarismo)

for algarismo in lista:
    if algarismo < 0:
        negativos += 1
    else:
        positivos += 1
print (f"Quantidade de negativos: {negativos}")
print (f"SOMA DOS POSITIVOS: {positivos}")


