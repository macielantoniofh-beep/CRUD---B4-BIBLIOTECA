from biblioteca_b4 import biblioteca

class Busca:
    def __init__(self, dados_biblioteca):
        self.biblioteca = dados_biblioteca

    def buscar_livro(self):
        buscar = input("Digite o nome do livro que deseja pesquisar: ").lower()

        livro_encontrado = False

        for livro in self.biblioteca:
            if buscar in livro["Nome"].lower():
                self.exibir_livro(livro)
                livro_encontrado = True
                break
        if not livro_encontrado:
            print("Livro não localizado")

    def exibir_livro(self, livro):
        print(f"O livro pesquisado é ID: {livro["ID"]}, \nNome: {livro["Nome"]}, \nAutor: {livro["Autor"]}, \nAno: {livro["Ano"]}, \nEditora: {livro["Editora"]}, \nGênero: {livro["Gênero"]}, \nSinopse: {livro["Sinopse"]}!")