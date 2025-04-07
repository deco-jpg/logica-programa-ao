import os
os.system ("cls")


def tabuada (number):
    for i in range (1, 11):
        print (f"{number} x {i} = {number * i}")

print ("TABUADA")
numero = int (input("Digite um numero: "))
tabuada(numero)
