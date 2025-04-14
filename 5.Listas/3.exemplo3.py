import os
os.system ("clear")

QUANTIDADE_NOTAS = 4
lista_notas = []

def calculo_media(lista_notas):
    media = sum(lista_notas) / QUANTIDADE_NOTAS
    return media

def mostrar_resultado (media):
    if media > 5:
        resultado = 'Aprovado'
    elif media >= 5:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"
    return resultado
for i in range (QUANTIDADE_NOTAS):
    notas = float (input("DIGITE SUA NOTA: "))
    lista_notas.append (notas)

media = calculo_media (lista_notas)
resultado = mostrar_resultado (media)

print (f"SUA MÉDIA É: {media:.2f}, VOCÊ ESTÁ: {resultado}")





