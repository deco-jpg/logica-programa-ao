import os
os.system ("cls")

#Entrada
valor = float (input("Digite o valor do produto: "))
forma_pagar = int (input("""
1- A vista
2- A prazo
Digite a opção do pagamento Pagamento: """))

match forma_pagar:
    case 1:
        desconto = valor * 0.10
        valor_total = valor - desconto  
        print ("Pagamento à vista")
        print (f"Valor do produto: {valor}")
        print (f"Forma de pagamento: A vista")
        print (f"Valor do desconto: {desconto}")
        print (f"Total a pagar: {valor_total}")
    case 2:
        desconto = 0
        parcelas = int (input("Escolha a quantidade de parcelas: "))
    case _:
        print ("Opção inválida!")


if 'parcelas' in locals() or 'parcelas' in globals():
    div_parcela = valor/parcelas


    match parcelas:    
        case 1:
            print ("Pagamento de uma parcela")
            print (f"Valor do produto: {valor}")
            print (f"Forma de pagamento: A prazo")
            print (f"Quantidade de parcelas: {parcelas}")
            print (f"Valor por parcela: {div_parcela}")
            print (f"Total a pagar: {valor}")
        case 2:
            print ("Pagamento de duas parcelas")
            print (f"Valor do produto: {valor}")
            print (f"Forma de pagamento: A prazo")
            print (f"Quantidade de parcelas: {parcelas}")
            print (f"Valor por parcela: {div_parcela}")
            print (f"Total a pagar: {valor}")
        case 3:
            print ("Pagamento de três parcelas")
            print (f"Valor das parcelas: {div_parcela}")
            print (f"Valor do produto: {valor}")
            print (f"Forma de pagamento: A prazo")
            print (f"Quantidade de parcelas: {parcelas}")
            print (f"Valor por parcela: {div_parcela}")
            print (f"Total a pagar: {valor}")
        case 4:
            print ("Pagamento de quatro parcelas")
            print (f"Valor das parcelas: {div_parcela}")
            print (f"Valor do produto: {valor}")
            print (f"Forma de pagamento: A prazo")
            print (f"Quantidade de parcelas: {parcelas}")
            print (f"Valor por parcela: {div_parcela}")
            print (f"Total a pagar: {valor}")
        case 5:
            print ("Pagamento de cinco parcelas")
            print (f"Valor das parcelas: {div_parcela}")
            print (f"Valor do produto: {valor}")
            print (f"Forma de pagamento: A prazo")
            print (f"Quantidade de parcelas: {parcelas}")
            print (f"Valor por parcela: {div_parcela}")
            print (f"Total a pagar: {valor}")
        case 6:
            print ("Pagamento de seis parcelas")
            print (f"Valor das parcelas: {div_parcela}")
            print (f"Valor do produto: {valor}")
            print (f"Forma de pagamento: A prazo")
            print (f"Quantidade de parcelas: {parcelas}")
            print (f"Valor por parcela: {div_parcela}")
            print (f"Total a pagar: {valor}")
        case _:
            print ("Opção inválida!")
else:
     print("Número de parcelas não definido.")
