import os
os.system ("clear")
#Elabore um algoritmo para solicitar dois números e ao final mostre
#na tela: A média, a soma, o produto, o menor valor e o maior valor.
#Usando uma linha para cada resultado.


numero_um=float(input("Digite o primeiro número:"))
numero_dois=float(input("Digite o segundo número:"))

media = (numero_um + numero_dois) / 2
produto = numero_um * numero_dois

if numero_um > numero_dois:
    maior = numero_um
    menor = numero_dois
else:
    maior = numero_dois
    menor = numero_um

print (f"\nA média é: {media}") #Contrabarra + n serve para quebrar linha
print (f"\nO produto é: {produto}") #Contrabarra + n serve para quebrar linha
print (f"\nMaior: {maior}") #Contrabarra + n serve para quebrar linha
print (f"\nMenor: {menor}") #Contrabarra + n serve para quebrar linha