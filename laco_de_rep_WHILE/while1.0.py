import os
os.system ("cls")
contador = 0
continua = 's'

while continua == 's':
    #comandos a serem repetidos
    print ("Repetindo...")

    continua = input ("Tecle 's' se deseja continuar: ") .strip() .lower()
    contador += 1

if contador == 0:
    print ("O bloco nao foi repetido.")
else:
    print (f"O bloco foi repetido {contador} vezes")