import os
os.system ("clear")

#Entrada
valor = float (input("Digite o valor do produto: "))
forma_pagar = int (input("""
1- A vista
2- A prazo
Digite a opção do pagamento Pagamento: """))
#Processamento
match forma_pagar:
    case 1:
        desconto = valor * 0.10
        print ("Pagamento à vista")
        
    case 2:
        parcela = int (input("Digite a quantidade de parcelas: "))
        match parcela:
            case 1:
                print ("1 parcela")
            case 2:
                print ("2 parcelas")
            case 3:
                print ("3 parcelas")
            case 4:
                print ("4 parcelas")
            case 5:
                print ("6 parcelas")
            case _:
                print ("Opção Inválida")

