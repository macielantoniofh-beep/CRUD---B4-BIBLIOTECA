from biblioteca_b4 import biblioteca
import sys

class Opcao:

   def escolha():
       while True:
           continuar = str(input("Deseja repetir a operação? (s/n)"))
           match continuar:
               case "s" | "S":
                   print("Você escolheu continuar:")
                   return True
               case "n" | "N":
                   print("Você escolheu finalizar.")
                   sys.exit()
               case _:
                   print("Opção inválida, digite apenas 's' ou 'n'.")