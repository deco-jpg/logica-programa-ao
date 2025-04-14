import os
os.system ("cls")

nota = 0
for i in range (2):
    nota += int (input("Digite sua nota: "))

media = nota / 2
while True:
    if media > 4:
        print ("Aprovado")
    else:
        print ("Reprovado")

   