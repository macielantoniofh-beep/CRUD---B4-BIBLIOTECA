from biblioteca_b4 import biblioteca

def escolha():
    while True:
        continuar = str(input("Deseja repetir a operação? (s/n)"))
        match continuar:
            case "s" | "S":
                print("Você escolheu continuar:")
                return True
            case "n" | "N":
                print("Você escolheu finalizar.")
                return False
            case _:
                print("Opção inválida, digite apenas 's' ou 'n'.")