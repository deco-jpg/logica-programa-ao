import os
os.system("cls")

def calculo_imc (peso, altura):
    imc = peso / (altura * altura)
    return imc

def resultado_imc ():
    if imc < 18.5:
        return "Abaixo do peso", "Consulte um nutricionista para orientação"
    elif imc < 25:
        return "Peso normal", "Mantenha hábitos saudáveis!"
    elif imc < 30:
        return "Sobrepeso", "Considere uma dieta balanceada e atividade física"
    elif imc < 35:
        return "Obesidade grau 1", "Procure orientação de um profissional de saúde"
    elif imc < 40:
        return "Obesidade grau 2", "Consulte um médico para avaliação e orientação"
    else:
        return "Obesidade grau 3", "Busque assistência médica imediatamente"

peso = int (input("DIGITE SEU PESO EM KG: "))
altura = float (input("DIGITE SUA ALTURA EM METROS: "))

imc = calculo_imc (peso, altura)
classificacao, recomendacao = resultado_imc ()

print (f"Seu IMC é: {imc:.2f}")
print (f"Classificação: {classificacao}")
print (f"Recomendação: {recomendacao}")
