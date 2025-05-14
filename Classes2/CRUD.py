# Lista para armazenar os usuários
usuarios = []

# Função para criar um novo usuário
def criar_usuario(nome, idade):
    usuario = {"nome": nome, "idade": idade}
    usuarios.append(usuario)
    print(f"Usuário '{nome}' adicionado com sucesso!")

# Função para listar todos os usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. Nome: {usuario['nome']}, Idade: {usuario['idade']}")

# Função para atualizar um usuário
def atualizar_usuario(indice, novo_nome, nova_idade):
    if 0 <= indice < len(usuarios):
        usuarios[indice]["nome"] = novo_nome
        usuarios[indice]["idade"] = nova_idade
        print("Usuário atualizado com sucesso!")
    else:
        print("Índice inválido.")

# Função para deletar um usuário
def deletar_usuario(indice):
    if 0 <= indice < len(usuarios):
        removido = usuarios.pop(indice)
        print(f"Usuário '{removido['nome']}' removido com sucesso!")
    else:
        print("Índice inválido.")

# Menu interativo usando match-case
def menu():
    while True:
        print("\nMenu:")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                nome = input("Digite o nome: ")
                idade = input("Digite a idade: ")
                criar_usuario(nome, idade)
            case "2":
                listar_usuarios()
            case "3":
                listar_usuarios()
                indice = int(input("Digite o número do usuário a atualizar: ")) - 1
                novo_nome = input("Novo nome: ")
                nova_idade = input("Nova idade: ")
                atualizar_usuario(indice, novo_nome, nova_idade)
            case "4":
                listar_usuarios()
                indice = int(input("Digite o número do usuário a deletar: ")) - 1
                deletar_usuario(indice)
            case "5":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

# Executa o menu
menu()
