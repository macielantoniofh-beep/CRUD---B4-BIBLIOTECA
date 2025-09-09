from biblioteca_b4 import biblioteca

def update_livro(biblioteca, ID, novos_dados):
    id_busca = input("Digite o ID do livro que deseja alterar: ")
    for id_busca in biblioteca:
        if id_busca["ID"] == ID:
            id_busca.update(novos_dados)
            print(f"Livro com ID {ID} atualizado com sucesso!")
            return 
    print(f"Erro: Livro com ID {ID} não encontrado.")