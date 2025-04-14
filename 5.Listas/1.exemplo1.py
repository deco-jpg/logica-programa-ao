import os
os.system("clear")

#Criando uma lista:
lista_notas = []

#Adicionando 3 notas em uma lista:
for i in range (3):
    nota = float (input("DIGITE SUA NOTA: "))
    lista_notas.append(nota)

#Exibindo resultados: #ForEach
for nota in lista_notas:
    print (nota)
