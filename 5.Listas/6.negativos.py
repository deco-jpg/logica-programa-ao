import os
os.system ("cls | clear")

negativo = 0
lista = []
QUANTIDADE_NUMEROS = 5

for i in range (QUANTIDADE_NUMEROS):
    algarismo = int (input(f"DIGITE O {i+1}° número: "))
    if algarismo < 0:
        algarismo = 0
    lista.append(algarismo)

for algarismo in lista:
    print (f"Numero: {algarismo}")
    


