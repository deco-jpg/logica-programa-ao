import os
os.system ("clear")
comanda = 0
while True:
    opcao = int (input("""""
    Código \t Prato \t\t\t Valor                                      
    1 \t Picanha \t\t 25,00                                      
    2 \t Lasanha \t\t 20,00                                      
    3 \t Strogonoff \t\t 18,00                                      
    4 \t Bife acebolado \t 15,00
    5 \t Pão com ovo \t\t 5,00
            Digite o que você deseja:
    """))

    match opcao:
        case 1: 
            refeicao = 25
        case 2:
            refeicao = 20
        case 3:
            refeicao = 18
        case 4:
            refeicao = 15
        case 5:
            refeicao = 5
        case _:
            print ("Errado ")
    comanda += refeicao

    repetir = input ("\nDigite 'S' se quiser adicionar mais algum prato e 'N' se não quiser: ") .upper ()
    if repetir == 'N':
        print ("Vou pegar a maquininha rs")
        print (f"O total é: {comanda}")
        break
    


        


    

        

    
