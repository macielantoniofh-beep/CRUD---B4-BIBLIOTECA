from biblioteca_b4 import biblioteca
from cadastro import cadastro_livro
from delete import delete_livro

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
                cadastro_livro(biblioteca)
                continuar = input("Deseja cadastrar outro livro? (s/n)")
                if continuar != "s" or "S":
                    break
        case "2":
            print("Livro editado")
        case "3":
            print("Livro pesquisado")
        case "4":
            while True:
                delete_livro(biblioteca)
                continuar = input("Deseja deletar outro livro? (s/n)")
                if continuar != "s" or "S":
                    break
        case "0":
            print("Sistema Finalizado!")
            break
        case _:
            print("Opção invalida, tente novamente")