import os
os.system ("clear")

usuario_cadastrado = "Danilo"
senha_cadastrada = "123"

usuario = input ("Digite seu login: ")
senha = input ("Digite sua senha: ")

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print ("Bem vindo! ")
else:
    print ("Login ou senha inválidos ")