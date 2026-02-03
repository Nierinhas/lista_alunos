def adicionar_aluno(lista):
    nome = input("Digite o nome do aluno: ").lower().strip()

    if nome == "":
        print("Nome inválido.")
        return

    # Evita aluno duplicado
    for aluno in lista:
        if aluno["nome"] == nome:
            print("Aluno já cadastrado.")
            return

    aluno = {
        "nome": nome,
        "notas": []
    }

    lista.append(aluno)
    print("Aluno adicionado.")


def adicionar_nota(lista):
    if len(lista) == 0:
        print("Nenhum aluno adicionado.")
        return

    procurar_aluno = input("Para qual aluno deseja atribuir nota? ").lower().strip()
    encontrou = False

    for aluno in lista:
        if aluno["nome"] == procurar_aluno:
            nota = float(input("Qual nota deseja atribuir? "))

            # Validação de nota
            if nota < 0 or nota > 10:
                print("Nota inválida. Digite um valor entre 0 e 10.")
                return

            aluno["notas"].append(nota)
            encontrou = True
            break

    if not encontrou:
        print("Aluno não encontrado.")
    else:
        print("Nota atribuída com sucesso.")


def mostrar_alunos_notas(lista):
    if len(lista) == 0:
        print("Nenhum aluno adicionado.")
        return

    print("\nLista de alunos:")

    for aluno in lista:
        print("--------------------")
        print("Nome:", aluno["nome"])

        if len(aluno["notas"]) == 0:
            print("Aluno não possui notas.")
        else:
            print("Notas:", aluno["notas"])


def calcular_media(lista):
    if len(lista) == 0:
        print("Nenhum aluno adicionado.")
        return

    procurar_aluno = input("Digite o nome do aluno: ").lower().strip()
    encontrou = False

    for aluno in lista:
        if aluno["nome"] == procurar_aluno:
            if len(aluno["notas"]) == 0:
                print("Não há notas a serem somadas.")
                encontrou = True
                break
            else:
                soma = sum(aluno["notas"])
                media = soma / len(aluno["notas"])
                print(f"A média do aluno {aluno['nome']} é: {media:.2f}")
                encontrou = True
                break

    if not encontrou:
        print("Aluno não encontrado.")


def aluno_aprovado(lista):
    if len(lista) == 0:
        print("Nenhum aluno adicionado.")
        return

    encontrou_aprovado = False

    for aluno in lista:
        if len(aluno["notas"]) == 0:
            continue  # pula alunos sem notas

        soma = sum(aluno["notas"])
        media = soma / len(aluno["notas"])

        if media >= 7:
            print(f"Aluno: {aluno['nome']} | Média: {media:.2f} | Aprovado")
            encontrou_aprovado = True

    if not encontrou_aprovado:
        print("Nenhum aluno aprovado ainda.")


# ---------- Menu -------------

lista = []

while True:
    print("\nMenu:")
    print("1 - Adicionar Aluno")
    print("2 - Adicionar nota a um aluno")
    print("3 - Mostrar alunos e notas")
    print("4 - Calcular média de um aluno")
    print("5 - Mostrar alunos aprovados")
    print("0 - Sair")

    opcao = input("Digite uma opção: ").strip()

    if opcao == "1":
        adicionar_aluno(lista)

    elif opcao == "2":
        adicionar_nota(lista)

    elif opcao == "3":
        mostrar_alunos_notas(lista)

    elif opcao == "4":
        calcular_media(lista)

    elif opcao == "5":
        aluno_aprovado(lista)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
