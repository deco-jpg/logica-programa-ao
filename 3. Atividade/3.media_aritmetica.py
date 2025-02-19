import os
os.system ("clear")
#Dê 3 notas de um aluno, some e tire a média dele. Se a nota for >= a 7, então: aprovado, se não: reprove


nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))

soma = nota_um + nota_dois + nota_tres
media = soma / 3

print (f"Media: {media}")
if media < 7:
    print ("Reprovado")
else:
    print ("Aprovado!")

