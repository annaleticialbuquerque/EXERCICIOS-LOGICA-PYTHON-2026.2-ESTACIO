# Questão 14 - Sistema de gerenciamento de notas de turma

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


def cadastrar_estudantes():
    estudantes = []

    for i in range(1, 6):
        print(f"\n=== ESTUDANTE {i} ===")

        nome = input("Nome: ")

        nota1 = ler_nota(1)
        nota2 = ler_nota(2)
        nota3 = ler_nota(3)

        media = (nota1 + nota2 + nota3) / 3

        estudante = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "media": media
        }

        estudantes.append(estudante)

    return estudantes


def analisar_turma(estudantes):
    maior_media = estudantes[0]
    menor_media = estudantes[0]

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:
        if estudante["media"] > maior_media["media"]:
            maior_media = estudante

        if estudante["media"] < menor_media["media"]:
            menor_media = estudante

        if estudante["media"] >= 7:
            aprovados += 1
        elif estudante["media"] >= 5:
            recuperacao += 1
        else:
            reprovados += 1

    print("\n=== RESULTADO DA TURMA ===")

    for estudante in estudantes:
        print(f"{estudante['nome']} - Média: {estudante['media']:.2f}")

    print(f"\nMaior média: {maior_media['nome']} - {maior_media['media']:.2f}")
    print(f"Menor média: {menor_media['nome']} - {menor_media['media']:.2f}")
    print(f"Quantidade de aprovados: {aprovados}")
    print(f"Quantidade em recuperação: {recuperacao}")
    print(f"Quantidade de reprovados: {reprovados}")


print("=== SISTEMA DE NOTAS DA TURMA ===")

estudantes = cadastrar_estudantes()
analisar_turma(estudantes)