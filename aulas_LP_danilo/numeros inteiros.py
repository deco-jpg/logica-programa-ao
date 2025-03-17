import os
os.system ("cls")

soma = 0
for i in range (1, 6):
    numero = int (input("Digite um número: "))
    #soma = soma + numero
    soma += numero
    
print (f"A soma é igual a: {soma}")
    