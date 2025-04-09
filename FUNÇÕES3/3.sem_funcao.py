import os
os.system ("cls")
acumulador = 0
continuar = ""

def mediafinal (acumulador):
    media = acumulador / i
    return media

while True:
    for i in range (2):
        algarismo = int (input("Digite um número: "))
        acumulador += algarismo
        continuar = input ("DESEJA CONTINUAR? SIM | NÃO\n ") .lower()
        if continuar == 'nao' or continuar == 'não' or continuar == 'n':
            media = mediafinal (acumulador)
            print (media)
            break
        
    


        