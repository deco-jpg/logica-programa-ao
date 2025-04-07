import os
os.system ("cls")

def parimpar (numero):
    if numero % 2 == 0:
        print (f"{numero} é Par")
    else:
        print (f"{numero} é Ímpar")

numero = int (input("Digite um numero: "))

parimpar (numero)
