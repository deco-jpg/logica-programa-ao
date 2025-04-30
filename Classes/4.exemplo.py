from dataclasses import dataclass
import os
os.system ("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def dados_livro(self):
        print (f"\nNome: {self.nome}\n Autor: {self.autor} \nCategoria: {self.categoria} \nPreço: {self.preco}")

lista_livros = []
QUANTIDADE_LIVROS = 3

for i in range (QUANTIDADE_LIVROS):
    informacao = Livro(
                        nome = input ("Digite o nome do livro: "),
                        autor = input ("Digite o nome do autor do livro: "),
                        categoria = input ("Digite a categoria do livro: "),
                        preco = float (input("Digite o preço do livro: "))
                        )
    lista_livros.append(informacao)
    os.system ("cls")

nome_arquivo = "Dados_Livros.txt"
with open(nome_arquivo, "a", encoding= "utf-8") as arquivo_livros:
    for informacao in lista_livros:
        arquivo_livros.write(f"\n{informacao.nome},\n{informacao.autor},\n{informacao.categoria},\n{informacao.preco}")

for informacao in lista_livros:
    informacao.dados_livro()
