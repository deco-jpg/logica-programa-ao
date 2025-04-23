import os
os.system ("cls | clear")

comanda = 0
cardapio = []

while True:
    print ("""

    CÓDIGO | PRATO        | VALOR
        1   PICANHA         25,00
        2   LASANHA         20,00
        3   STROGONOFF      18,00
        4   BICE ACEBOLADO  15,00
        5   PÃO C/ OVO      5,00

        """)
    opcao = int (input("ESCOLHA A OPÇÃO DESEJADA DIGITANDO O CÓDIGO: "))

    os.system ("cls | clear")
    match opcao:
        case 1:
            prato = "PICANHA | 25.00"
            cardapio.append (prato)
            comanda += 25.00
            
        case 2:
            prato = "LASANHA | 20.00"
            cardapio.append (prato)
            comanda += 20.00
            
        case 3:
            prato = "STROGONOFF | 18.00"
            cardapio.append (prato)
            comanda += 18.00
            
        case 4:
            prato = "BIFE ACEBOLADO | 15.00"
            cardapio.append (prato)
            comanda += 15.00
            
        case 5:
            prato = "PÃO C/ OVO | 5.00"
            cardapio.append (prato)
            comanda += 5.00
            
        case _:
            print ("OPÇÃO INVÁLIDA! ")

    escolha = (input("QUER ESCOLHER MAIS ALGUM PRATO? S/N: ")) .upper()
    if escolha == 'N':
        break

os.system ("clear")
for prato in cardapio:
    print (prato)

print (f"TOTAL A PAGAR: {comanda:.2f}")

    

