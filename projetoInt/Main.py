from Candidatos import listar

from Menu import imprimeMenu

from Menu import recebeOpMenu

from Votar import votoGovernador

from Votar import votoPresidente
from apurar import menu


opcaoMenu = 0

while opcaoMenu != 4:

    imprimeMenu()
    opcaoMenu = recebeOpMenu()

    if opcaoMenu == 1:
        listar()  # lista de candidatos

    elif opcaoMenu == 2:
        votoGovernador()
        votoPresidente()

    elif opcaoMenu == 3:
        menu()  # Apuração de votos

    elif opcaoMenu == 4:
        print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna\n")

    else:
        print("\nOpção inválida!")