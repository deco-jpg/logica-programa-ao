import os
os.system ("cls")

def saudacao(parametro):
    print(f"Olá, {parametro}. Bem vinda ao nosso site.")

nome_visitante = input ("Digite seu nome: ")

saudacao(nome_visitante)