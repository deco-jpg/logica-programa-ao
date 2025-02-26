import os
os.system ("clear")

opcao = int (input("""""
Código \t Prato \t\t\t Valor                                      
1 \t Picanha \t\t 25,00                                      
2 \t Lasanha \t\t 20,00                                      
3 \t Strogonoff \t\t 18,00                                      
4 \t Bife acebolado \t 15,00
5 \t Pão com ovo \t\t 5,00
        Digite o que você deseja:
"""))

#processamento
match opcao:
    case 1:
        print ("Opção desejada: Picanha - 25 -00")
    case 2:
        print ("Opção desejada: Lasanha - 20,00")
    case 3:
        print ("Opção desejada: Strogonoff - 18,00")
    case 4:
        print ("Opção desejada: Bife Acebolado - 15,00")
    case 5:
        print ("Opção desejada: Pão com ovo - 05,00")