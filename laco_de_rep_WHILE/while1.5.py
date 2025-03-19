import os
os.system ("cls")
contador = 0
continua = "s"

while True:
    print ("Repetindo...")

    continua = input ("Tecle 's' para repetir: ") .strip() .lower ()
    contador += 1

    if continua != "s":
        break

if contador == 0:
    print ("O bloco nao foi repetido.")
else:
    print (f"o bloco foi repetido {contador} vezes")
