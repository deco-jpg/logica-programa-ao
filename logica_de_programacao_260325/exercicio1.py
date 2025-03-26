import os
os.system("cls")
contador = 0
soma = 0
while True:
        numero = int (input("Digite uma nota: "))
        if numero > 0:
            soma += numero
            contador += 1
        else:
             break

        
        
media = soma / contador
print (f"media: {media}")

