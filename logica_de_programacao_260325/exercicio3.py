import os
os.system ("cls")

contador = 0
soma = 0

while True:
    print ("""

    CÓDIGO | DESCRIÇÃO
    1    ADICIONAR PESSOA
    2    EXIBIR RESULTADOS
    3    SAIR

    """)
    opcao = (input("ESCOLHA 1 | 2 | 3 PARA A OPÇÃO DESEJADA: "))

    match opcao:
        case '1':
            idade = int (input("Digite sua idade: "))
            sexo = (input("Digite 'M' para masculino e 'F' para feminino: ")) .upper()
            salário = float (input("Digite o seu salário: "))
        case '2':
            print ("oi")
        case '3':
            break

