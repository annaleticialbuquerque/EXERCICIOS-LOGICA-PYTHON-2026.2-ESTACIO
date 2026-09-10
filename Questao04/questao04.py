# Questão 04 - Cálculo de média e determinação de situação acadêmica

print("=== SITUAÇÃO ACADÊMICA ===")

notas = []

for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0 a 10): "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: digite uma nota válida.")

media = sum(notas) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n=== RESULTADO ===")
print(f"Nota 1: {notas[0]:.2f}")
print(f"Nota 2: {notas[1]:.2f}")
print(f"Nota 3: {notas[2]:.2f}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")