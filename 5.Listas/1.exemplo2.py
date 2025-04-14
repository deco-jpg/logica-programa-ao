import os
os.system ("clear")

QUANTIDADE_NOTAS = 3
lista_nota = []
for i in range (QUANTIDADE_NOTAS):
    nota = float (input("DIGITE A NOTA: "))
    lista_nota.append(nota)
media = sum (lista_nota) / QUANTIDADE_NOTAS
print (f"SUAS NOTAS FORAM: {lista_nota}")
print (f"\nSUA MÉDIA É: {media:.2f}")



