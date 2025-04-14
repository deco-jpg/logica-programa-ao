import os
os.system("cls")
import time
def inflacao (produto):
    if produto < 100:
        valorfinal = produto * 1.10
    if produto >= 100:
        valorfinal = produto * 1.20
    return valorfinal
def desconto (produto):
    if produto < 100:
        return produto * 0.10
    if produto >= 100:
        return produto * 0.20
def valorfinal (produto):
    valor_final = produto - preco_desconto
    return valor_final
def contador ():
    print ("Carregando resultados:\n")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep (2)
    
produto = float (input("Digite o preço do produto: "))

preco_inflacionado = inflacao (produto)
preco_desconto = desconto (produto)
valor_final = valorfinal (produto)
contador ()
print(f"\nPreço inflacionado: R${preco_inflacionado:.2f}")
print (f"O desconto será de R${preco_desconto:.2f}")
print (f"Valor final com desconto: {valor_final:.2f}")
