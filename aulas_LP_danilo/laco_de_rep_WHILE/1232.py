import os
os.system ("cls")

login_cadastrado = 'danilo'
senha_cadastrada = '123'
contador = 0

for i in range (3):
    login = input ("Digite seu login: ")
    senha = input ("Digite sua senha: ")

    if login == login_cadastrado and senha == senha_cadastrada:
        print ("Login Correto")
        break
    else:
        print ("Acesso negado. \n")
        contador +=1
    if contador == 3:
        print ("Numero de tentativas excedidas!")
        break