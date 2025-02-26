import os
os.system ("clear")

dia = int (input("Digite um número: "))


match dia:
    case 1:
        print ("\nDomingo \t Fim de semana")
    case 2:
        print ("\nSegunda \t Dia útil")
    case 3:
        print ("\nTerça \t Dia útil")
    case 4:
        print ("\nQuarta \t Dia útil")
    case 5:
        print ("\nQuinta \t Dia útil")
    case 6:
        print ("\nSexta \t Dia útil")
    case 7:
        print ("\nSábado \t Fim de semana")
    case _:
        print ("\nOpção Inválida")