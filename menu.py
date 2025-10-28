from biblioteca_b4 import biblioteca
from cadastro import Cadastro_livro
from delete import delete_livro
from update import update_livro
from busca import Busca
from opcao import escolha

class Menu_biblioteca:
    def __init__(self):
        self.biblioteca = biblioteca

    def menu(self):
        while True:
            print("*-*-" * 10)
            print("Bem-vindo(a) a Biblioteca B4!")
            print("*-*-" * 10)
            opcao = input("Escolha uma opção: \n"
                        "1 - Adicionar um livro \n"
                        "2 - Editar informações de um livro \n"
                        "3 - Pesquisar um livro \n"
                        "4 - Remover um livro \n"
                        "0 - sair\n")
            match opcao:
                case "1":
                    self.adicionar_livro()
                case "2":
                    self.atualiza_livro()
                case "3":
                    self.busca_livro()
                case "4":
                    self.deleta_livro()
                case "0":
                    print("Sistema Finalizado!")
                    break
                case _:
                    print("Opção invalido")

    def adicionar_livro(self):
        while True:
            Cadastro_livro().cadastro()
            if not escolha():
                break

    def atualiza_livro(self):
        while True:
            update_livro(biblioteca)
            if not escolha():
                break

    def busca_livro(self):
        while True:
            Busca(biblioteca).buscar_livro()
            if not escolha():
                break

    def deleta_livro(self):
        while True:
            delete_livro(biblioteca)
            if not escolha():
                break

if __name__ == "__main__":
    sistema = Menu_biblioteca()
    sistema.menu()