import os
os.system ("clear")

nome = str (input("Digite seu nome: "))
nota_um = float (input("Digite a primeira nota: "))
nota_dois = float (input("Digite a segunda nota: "))
media = (nota_um + nota_dois) /2

print (f"Seu nome é: {nome}")
print (f"Primeira nota: {nota_um}")
print (f"Segunda nota: {nota_dois}")
print (f"Media: {media}")

if media >= 9:
    print ("Conceito A: Aprovado! ")
elif media >= 7.5 and media <9:
    print ("Conceito B: Aprovado! ")
elif media >=6 and media <7.5:
    print ("Conceito C: Aprovado! ")
elif media >= 4 and media <6:
    print ("Conceito D: Reprovado! ")
elif media <4:
    print ("Conceito E: Reprovado! ")


