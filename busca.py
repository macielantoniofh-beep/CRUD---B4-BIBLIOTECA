from biblioteca_b4 import biblioteca

def buscar_livro(biblioteca):
    buscar = input("Digite o nome do livro que deseja pesquisar: ").lower()
    for livro in biblioteca:
        if buscar in livro["Nome"].lower():
            print(f"O livro pesquisado é ID: {livro["ID"]}, \nNome: {livro["Nome"]}, \nAutor: {livro["Autor"]}, \nAno: {livro["Ano"]}, \nEditora: {livro["Editora"]}, \nGênero: {livro["Gênero"]}, \nSinopse: {livro["Sinopse"]}!")
            break
    else:
        print("Livro não localizado")