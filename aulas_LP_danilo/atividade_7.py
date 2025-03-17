import os
os.system ("cls")

soma = 0
for i in range (1, 5):
    nota = int (input("Digite a nota: "))
    soma += nota

media = soma / 4
print (f"Media: {media}")