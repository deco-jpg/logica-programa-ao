import os
os.system ("cls")

login = 'danilo'
senha = '123'
contador = 0
while True:
    login_um = input ("Digite seu login: ")
    senha_dois = input("Digite sua senha: ")
    if login_um == login and senha_dois == senha:
        print ("Login Correto!")
        break
    else:
        for i in range (3):
            print ("LOGIN INCORRETO, TENTE NOVAMENTE! ")
            login_um = input ("\nDigite seu login: ")
            senha_dois = input("Digite sua senha: ")
            contador += 1
            if i == 3:
                print ("Voce atingiu o maximo de tentativas! ")
                break
            
    
            

            
        
        
      
        
print ("FIM")

