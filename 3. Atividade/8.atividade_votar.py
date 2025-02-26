import os
os.system ("clear")

nome = str (input("Digite seu nome: "))
cpf = str (input("Digite seu CPF: "))
idade = int (input("Digite sua idade: "))



print (f"\nSeu nome é: {nome}")
print (f"Seu CPF é: {cpf}")
print (f"Sua idade é: {idade}")

if idade <18 or idade > 65:
    print ("Não pode votar! ")
else:
    print ("É obrigado a votar!")

# if idade >=18 and idade <=65:
#     resultado = "É obrigado a votar"
# else:
#     resultado = "Não é obrigado a votar"
    