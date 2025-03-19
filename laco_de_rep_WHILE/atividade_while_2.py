import os
os.system ("cls")

login = 'danilo'
senha = 123

while True:
    login_um = input ("Digite seu login: ")
    senha_dois = int (input("Digite sua senha: "))
    if login_um == login and senha_dois == senha:
        print ("Login Correto!")
        break
    else:
        print ("Acesso negado!\n")
        print ("Tente novamente")
        
print ("FIM")

