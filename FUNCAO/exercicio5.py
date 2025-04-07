import os
os.system ("cls")
acumulador = 0
def nota_media (acumulador):
    media = acumulador / 2
    return media
def media_resultado (media):
    if media >= 7:
        print ("Aprovado")
    else:
        print ("Reprovado")
for i in range (2):
    notas = int (input("Digite sua nota: "))
    acumulador += notas
media = nota_media (acumulador)
resultado = media_resultado (media)
print (f"A sua média é: {media}")
