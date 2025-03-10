import os
os.system ("clear")

matricula = input("Digite sua matrícula: ")
nascimento = int (input("Digite o ano em que nasceu: "))
tempo_trab = int (input("Digite o tempo de trabalho: "))

idade = 2025 - nascimento

if idade > 65 or tempo_trab >= 30:
    resultado = "Requerer aposentadoria!"
else:
    resultado = "Não requerer aposentadoria!"

print (f"\nMatricula: {matricula}")
print (f"Idade: {idade}")
print (f"Tempo de trabalho: {tempo_trab}")
print (f"Resultado: {resultado}")