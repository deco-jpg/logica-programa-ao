import os
os.system ("cls")
media = 0

nota_um = float (input("Digite o primeiro numero: "))
nota_dois = float (input("Digite o segundo numero: "))
nota_tres = float (input("Digite a terceira nota: "))

while True:
    if nota_um < 0 or nota_um > 10:
        print ("Digite novamente: ")
    if nota_dois < 0 or nota_dois > 10:
        print ("Digite novamente: ")
    if nota_tres < 0 or nota_tres > 10:
        print ("Digite novamente: ")
    else:
        break

media = (nota_um + nota_dois + nota_tres) / 3

if media < 5:
    resultado = "Reprovado"
elif media < 7:
    resultado = "Recuperação" 
else:
    resultado = "Aprovado"

print (f"Sua média é: {media}")
print (f"Você está: {resultado}")




        
