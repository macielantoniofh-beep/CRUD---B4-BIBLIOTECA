from biblioteca_b4 import biblioteca

def update_livro(biblioteca):
 
    try:
        livro_id = int(input("Digite o ID do livro que você quer atualizar: "))
    except ValueError:
        print("Erro: Por favor, digite um ID válido (um número inteiro).")
        return

    livro_encontrado = None
    for livro in biblioteca:
        if livro["ID"] == livro_id:
            livro_encontrado = livro
            break

    if livro_encontrado:
        for chave, valor in livro_encontrado.items():
            print(f"{chave}:{valor}") 

        print("\nDigite o novo valor para cada campo. Se não quiser alterar, apenas pressione Enter.")

        for chave in livro_encontrado:
            if chave == "ID":
                continue

            novo_valor = input(f"Novo valor para '{chave}' (atual: '{livro_encontrado[chave]}'): ")
            
            if novo_valor:
                if chave == "Ano" and novo_valor.isdigit():
                    livro_encontrado[chave] = int(novo_valor)
                else:
                    livro_encontrado[chave] = novo_valor
        
        print("\nLivro atualizado com sucesso!")
        print(f"Confira as novas informações do livro com ID {livro_id}:")
        for chave, valor in livro_encontrado.items():
            print(f"{chave}: {valor}")
    else:
        print(f"\nErro: Livro com ID '{livro_id}' não encontrado na biblioteca.")


update_livro(biblioteca)