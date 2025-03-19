import os
os.system ("cls")

nota_1 = float (input("Digite a primeira nota: "))
nota_2 = float (input("Digite a segunda nota: "))
while True:
    
    if nota_1 < 0 or nota_1 > 10:
        print ("Digite novamente: ")
        
    if nota_2 < 0 or nota_2 > 10:
        print ("Digite novamente: ")
        
    else:
        break
        
    
media = (nota_1 + nota_2) / 2
print (f"Sua media é: {media}")
print ("FIM")