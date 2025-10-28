from biblioteca_b4 import biblioteca

class Cadastro_livro():
    def __init__(self):
        if biblioteca:
            self.id_livro = biblioteca[-1]["ID"] + 1
        else:
            self.id_livro = 1

    def __init__(self):
        self.nome_livro = input("Digite o nome do livro: ")
        self.autor_livro = input("Digite o autor do livro: ")
        self.editora_livro = input("Digite a editora do livro: ")
        self.ano_livro = input("Digite o ano do livro: ")
        self.genero_livro = input("Digite o gênero do livro: ")
        self.sinopse_livro = input("Digite uma breve sinopse do livro: ")

    def novo_livro(self):
        return{
        "ID": self.id_livro,
        "Nome": self.nome_livro,
        "Autor": self.autor_livro,
        "Editora": self.editora_livro,
        "Ano": self.ano_livro,
        "Gênero": self.genero_livro,
        "Sinopse": self.sinopse_livro

    }

    def __cadastro__(self):
        add_livro = Cadastro_livro()
        biblioteca.append(add_livro.novo_livro)
        print("Livro cadastrado com sucesso!")