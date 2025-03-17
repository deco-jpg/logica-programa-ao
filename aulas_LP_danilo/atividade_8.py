import os
os.system ("cls")
soma = 0
for i in range (1, 4):
    nota = int (input("Digite a nota: "))
    soma += nota
    
media = soma / 3
if media >= 7:
    resultado = "Aprovado"
elif media < 4:
    resultado = "Reprovado"
print (f"Media: {media}")
print (resultado)
