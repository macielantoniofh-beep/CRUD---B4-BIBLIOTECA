from biblioteca_b4 import biblioteca

def delete_livro(biblioteca):
    if not biblioteca:
        print("A biblioteca está sem livros")
        return

    try:
        id_excluido = int(input("Digite o ID do livro que deseja deletar: "))

        for livro in biblioteca:
            if livro["ID"] == id_excluido:
                biblioteca.remove(livro)
                print(f"Livro com ID {id_excluido} removido com sucesso!")
                return

        print(f"Nenhum livro foi encontrado com o ID {id_excluido}.")
    except ValueError:
        print("ID inválido")
