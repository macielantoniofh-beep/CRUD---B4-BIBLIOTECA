from biblioteca_b4 import biblioteca
from cadastro import Cadastro_livro
from delete import delete_livro
from update import update_livro
from busca import Busca
from opcao import escolha


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
            while True:
                Cadastro_livro().cadastro()
                if not escolha():
                    break
        case "2":
            while True:
                update_livro(biblioteca)
                if not escolha():
                    break
        case "3":
            while True:
                Busca(biblioteca).buscar_livro()
                if not escolha():
                    break
        case "4":
            while True:
                delete_livro(biblioteca)
                if not escolha():
                    break
        case "0":
            print("Sistema Finalizado!")
            break
        case _:
            print("Opção invalido")