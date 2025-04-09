import os
os.system ("cls")
import time
acumulador = 0

def calculo (acumulador):
    media = acumulador / i
    return media
def resultado ():
    if media >= 7:
        print ("APROVADO ✅")
    else:
        print ("REPROVADO ❌")
def limpador ():
    os.system ("cls")
def contador ():
    print ("CARREGANDO RESULTADO", end="...")
    time.sleep (1)
    print (".")
    time.sleep (1)
    print (".")
    time.sleep (1)
    print (".")

while True:
    for i in range (1,4):
        notas = float (input("Digite suas notas: "))
        acumulador += notas
        limpador ()
    permissao = (input("APERTE R PARA VER O RESULTADO:\n ")) .lower() .strip()
    if permissao != 'r':
        print ("COMANDO INVÁLIDO")
        print ("PARA A SEGURANÇA DA SUA NOTA, O SISTEMA SERÁ ENCERRADO")
        break
    else:
        limpador ()
        contador ()
        limpador ()
        media = calculo (acumulador)
        print (f"Sua nota final é: {media:.2f}")
        result_final = resultado ()
        break