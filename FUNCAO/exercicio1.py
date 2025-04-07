import os
os.system("cls")

def posinega (numero):
    if numero < 0:
        print (f"O número {numero} é negativo! ")
    else:
        print (f"O número {numero} é positivo! ")

numero = int (input("Digite um numero: "))

posinega (numero)