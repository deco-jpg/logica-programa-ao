import os
os.system ("clear")

#Entrada
genero = str (input("Digite M para masculino ou F para feminino: ")).upper()
altura = float (input("Digite sua altura: "))

#Processamento
match genero:
    case "M":
       peso_ideal = (72.7 * altura) -58
       print (f"Seu peso ideal é: {peso_ideal:.2f}")
    case "F":
        peso_ideal = (62.1 * altura) -44.7
        print (f"Seu peso ideal é: {peso_ideal:.2f}")
    case _:
        print ("Opção Invalida")