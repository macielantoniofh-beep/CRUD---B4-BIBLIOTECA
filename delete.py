from biblioteca_b4 import biblioteca
# from cadastro import Cadastro_livro
# from delete import delete_livro
# from update import update_livro
# from busca import Busca
# from opcao import escolha


# class Livro:
#     def __init__(self, id_livro, titulo, autor):
#         self._id = id_livro 
#         self.titulo = titulo
#         self.autor = autor

#     def get_id(self):
#         return self._id

#     def __str__(self):
#         return f"ID: {self.get_id()}, Título: {self.titulo}, Autor: {self.autor}"

# class Del_livro:
#     def __init__(self, dados_biblioteca):
#         self.biblioteca = dados_biblioteca

#     def delete_livro(self):
#         if not self.livros:
#             print("A biblioteca está sem livros.")
#             return

#         try:
#             id_excluido = int(input("Digite o ID do livro que deseja deletar: "))
#         except ValueError:
#             print("**ERRO:** ID inválido. Por favor, digite um número inteiro.")
#             return

#         livro_encontrado = "None"
#         for livro in self.livros:
#             if livro.get_id() == id_excluido:
#                 livro_encontrado = livro
#                 break

#         if livro_encontrado:
#             self.livros.remove(livro_encontrado)
#             print(f"✅ Livro com ID {id_excluido} ('{livro_encontrado.titulo}') removido com sucesso!")
#         else:
#             print(f"❌ Nenhum livro foi encontrado com o ID {id_excluido}.")
            
#     def mostrar_livros(self):
#         if not self.livros:
#              print("A biblioteca está vazia.")
#              return
#         print("\n--- Livros na Biblioteca ---")
#         for livro in self.livros:
#              print(livro) 

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