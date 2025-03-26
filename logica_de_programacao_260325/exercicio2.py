import os
os.system ("cls")

media_pares = 0
contador = 0
soma = 0
pares = 0
impares = 0
while True:
    numero = int (input(f"Digite o número: "))
    if numero == 0:
        break
    else:
        soma += numero
        contador += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares +=1

media = pares / contador
media_pares = pares / (pares -1)
print (f"Pares: {pares}")
print (f"Impares: {impares}")
print (f"Média: {media:.2f}")
print (f"Média pares: {media_pares}")


