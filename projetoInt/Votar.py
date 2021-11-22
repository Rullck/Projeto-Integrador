
import Candidatos
import Confirmar
import apurar
import nulo

#Votos para presidentes
def votoPresidente():
    votoPres = input("\nDigite o número do candidato à Presidente (ou B para Em Branco): ").upper()

    if votoPres == 'B':
        print("Voto em Branco registrado!")

        if Confirmar.confirmarVoto():
            apurar.votoEmBrancoPres += 1

    elif votoPres == '1':
        print(f"\nCandidato escolhido: {Candidatos.nomePres1}")

        if Confirmar.confirmarVoto():
            apurar.votoPres1 += 1

    elif votoPres == '2':
        print(f"\nCandidato escolhido: {Candidatos.nomePres2}")

        if Confirmar.confirmarVoto():
            apurar.votoPres2 += 1

    elif votoPres == '3':
        print(f"\nCandidato escolhido: {Candidatos.nomePres3}")

        if Confirmar.confirmarVoto():
            apurar.votoPres3 += 1

    elif votoPres == '4':
        print(f"\nCandidato escolhido: {Candidatos.nomePres4}")

        if Confirmar.confirmarVoto():
            apurar.votoPres4 += 1

    elif votoPres == '5':
        print(f"\nCandidato escolhido: {Candidatos.nomePres5}")

        if Confirmar.confirmarVoto():
            apurar.votoPres5 += 1

    else:
        nulo.nuloPres()

#Votos para governadores
def votoGovernador():
    votoGov = input("\nDigite o número do candidato à governador (ou B para Em Branco): ").upper()

    if votoGov == 'B':
        print("\nVoto em Branco Registrado!")

        if Confirmar.confirmarVoto():
            apurar.votoEmBrancoGov += 1

    elif votoGov == '1':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov1}")

        if Confirmar.confirmarVoto():
            apurar.votoGov1 += 1

    elif votoGov == '2':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov2}")

        if Confirmar.confirmarVoto():
            apurar.votoGov2 += 1

    elif votoGov == '3':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov3}")

        if Confirmar.confirmarVoto():
            apurar.votoGov3 += 1

    elif votoGov == '4':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov4}")

        if Confirmar.confirmarVoto():
            apurar.votoGov4 += 1

    elif votoGov == '5':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov5}")

        if Confirmar.confirmarVoto():
            apurar.votoGov5 += 1

    else:
        nulo.nuloGov()