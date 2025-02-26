import os
os.system ("clear")

#Faça um algoritmo que solicite ao usuário dois numeros
#e um caractere que calcula as operações basicas
#e mostre os numeros, a operação escolhida e o resultado
# Processamento

# Entrada
primeiro_numero = int (input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
segundo_numero = int (input("Digite o segundo numero: "))

match operador:
    case "+":
        resultado= primeiro_numero + segundo_numero
    case "-":
        resultado= primeiro_numero - segundo_numero
    case "*":
        resultado= primeiro_numero * segundo_numero
    case "/":
        resultado= primeiro_numero / segundo_numero
    case _:
        resultado= "Opção inválida."

# Print

print (f"Primeiro número: {primeiro_numero}")
print (f"Operação: {operador} ")
print (f"Segundo número: {segundo_numero} ")
print (f"Resultado: {resultado}")