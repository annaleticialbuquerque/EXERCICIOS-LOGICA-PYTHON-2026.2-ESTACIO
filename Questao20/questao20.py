# Questão 20 - Sistema completo de gerenciamento acadêmico

print("========================================")
print("        SISTEMA ACADÊMICO")
print("========================================")

estudantes = []


def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))

            if idade > 0:
                return idade
            else:
                print("Erro: a idade deve ser um número inteiro positivo.")
        except ValueError:
            print("Erro: digite uma idade válida.")


def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0 a 10): "))

            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: digite uma nota válida.")


def calcular_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    return media, situacao


def exibir_estudante(estudante):
    print("\n----------------------------------------")
    print(f"Nome: {estudante['nome']}")
    print(f"Idade: {estudante['idade']} anos")
    print(f"Curso: {estudante['curso']}")
    print(f"Nota 1: {estudante['notas'][0]:.2f}")
    print(f"Nota 2: {estudante['notas'][1]:.2f}")
    print(f"Nota 3: {estudante['notas'][2]:.2f}")
    print(f"Média final: {estudante['media']:.2f}")
    print(f"Situação: {estudante['situacao']}")
    print("----------------------------------------")


def cadastrar_estudante():
    print("\n=== CADASTRAR ESTUDANTE ===")

    nome = input("Nome: ")
    idade = ler_idade()
    curso = input("Curso: ")

    nota1 = ler_nota(1)
    nota2 = ler_nota(2)
    nota3 = ler_nota(3)

    notas = (nota1, nota2, nota3)

    media, situacao = calcular_situacao(nota1, nota2, nota3)

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    estudantes.append(estudante)

    print("\nEstudante cadastrado com sucesso!")


def listar_estudantes():
    print("\n=== LISTA DE ESTUDANTES ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    for estudante in estudantes:
        exibir_estudante(estudante)


def consultar_estudante():
    print("\n=== CONSULTAR ESTUDANTE ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca = input("Digite o nome do estudante: ")

    encontrado = False

    for estudante in estudantes:
        if estudante["nome"].lower() == nome_busca.lower():
            exibir_estudante(estudante)
            encontrado = True
            break

    if not encontrado:
        print("Estudante não encontrado.")


def alterar_dados():
    print("\n=== ALTERAR DADOS ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca = input("Digite o nome do estudante que deseja alterar: ")

    estudante_encontrado = None

    for estudante in estudantes:
        if estudante["nome"].lower() == nome_busca.lower():
            estudante_encontrado = estudante
            break

    if estudante_encontrado is None:
        print("Estudante não encontrado.")
        return

    print("\nEstudante encontrado.")
    exibir_estudante(estudante_encontrado)

    print("\nO que deseja alterar?")
    print("1 - Nome")
    print("2 - Idade")
    print("3 - Curso")
    print("4 - Nota 1")
    print("5 - Nota 2")
    print("6 - Nota 3")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Digite o novo nome: ")
        estudante_encontrado["nome"] = novo_nome

    elif opcao == "2":
        nova_idade = ler_idade()
        estudante_encontrado["idade"] = nova_idade

    elif opcao == "3":
        novo_curso = input("Digite o novo curso: ")
        estudante_encontrado["curso"] = novo_curso

    elif opcao == "4":
        nova_nota = ler_nota(1)
        notas = list(estudante_encontrado["notas"])
        notas[0] = nova_nota
        estudante_encontrado["notas"] = tuple(notas)

    elif opcao == "5":
        nova_nota = ler_nota(2)
        notas = list(estudante_encontrado["notas"])
        notas[1] = nova_nota
        estudante_encontrado["notas"] = tuple(notas)

    elif opcao == "6":
        nova_nota = ler_nota(3)
        notas = list(estudante_encontrado["notas"])
        notas[2] = nova_nota
        estudante_encontrado["notas"] = tuple(notas)

    else:
        print("Opção inválida.")
        return

    notas_atualizadas = estudante_encontrado["notas"]

    media, situacao = calcular_situacao(
        notas_atualizadas[0],
        notas_atualizadas[1],
        notas_atualizadas[2]
    )

    estudante_encontrado["media"] = media
    estudante_encontrado["situacao"] = situacao

    print("\nDados alterados com sucesso!")


def remover_estudante():
    print("\n=== REMOVER ESTUDANTE ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca = input("Digite o nome do estudante que deseja remover: ")

    estudante_encontrado = None

    for estudante in estudantes:
        if estudante["nome"].lower() == nome_busca.lower():
            estudante_encontrado = estudante
            break

    if estudante_encontrado is None:
        print("Estudante não encontrado.")
        return

    exibir_estudante(estudante_encontrado)

    confirmacao = input("Deseja realmente remover este estudante? (s/n): ")

    if confirmacao.lower() == "s":
        estudantes.remove(estudante_encontrado)
        print("Estudante removido com sucesso.")
    else:
        print("Remoção cancelada.")


def gerar_relatorio():
    print("\n=== RELATÓRIO DA TURMA ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    total_estudantes = len(estudantes)

    maior_media = estudantes[0]
    menor_media = estudantes[0]

    soma_medias = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:
        soma_medias += estudante["media"]

        if estudante["media"] > maior_media["media"]:
            maior_media = estudante

        if estudante["media"] < menor_media["media"]:
            menor_media = estudante

        if estudante["situacao"] == "Aprovado":
            aprovados += 1
        elif estudante["situacao"] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1

    media_geral = soma_medias / total_estudantes

    print(f"Total de estudantes: {total_estudantes}")
    print(
        f"Maior média: {maior_media['nome']} - "
        f"{maior_media['media']:.2f}"
    )
    print(
        f"Menor média: {menor_media['nome']} - "
        f"{menor_media['media']:.2f}"
    )
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")


while True:
    print("\n========================================")
    print("        SISTEMA ACADÊMICO")
    print("========================================")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")
    print("========================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_estudante()

    elif opcao == "2":
        listar_estudantes()

    elif opcao == "3":
        consultar_estudante()

    elif opcao == "4":
        alterar_dados()

    elif opcao == "5":
        remover_estudante()

    elif opcao == "6":
        gerar_relatorio()

    elif opcao == "0":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida. Escolha uma opção de 0 a 6.")