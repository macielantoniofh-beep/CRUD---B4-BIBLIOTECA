from biblioteca_b4 import biblioteca

def cadastro_livro(biblioteca):
    id_livro = biblioteca[-1]["ID"] + 1
    nome_livro = input("Digite o nome do livro: ")
    autor_livro = input("Digite o autor do livro: ")
    editora_livro = input("Digite a editora do livro: ")
    ano_livro = input("Digite o ano do livro: ")
    genero_livro = input("Digite o gênero do livro: ")
    sinopse_livro = input("Digite uma breve sinopse do livro: ")

    novo_livro = {
        "ID":id_livro,
        "Nome":nome_livro,
        "Autor":autor_livro,
        "Editora":editora_livro,
        "Ano":ano_livro,
        "Gênero":genero_livro,
        "Sinopse":sinopse_livro

    }
    biblioteca.append(novo_livro)
    print("Livro cadastrado com sucesso!")