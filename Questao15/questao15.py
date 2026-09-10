# Questão 15 - Cadastro e análise populacional de cidades

print("=== CADASTRO DE CIDADES ===")

cidades = []

for i in range(1, 6):
    print(f"\n=== CIDADE {i} ===")

    nome = input("Nome da cidade: ")
    estado = input("Estado (sigla): ")
    populacao = int(input("População estimada: "))

    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }

    cidades.append(cidade)

# Identificação da maior e menor população
maior_populacao = cidades[0]
menor_populacao = cidades[0]

for cidade in cidades:
    if cidade["populacao"] > maior_populacao["populacao"]:
        maior_populacao = cidade

    if cidade["populacao"] < menor_populacao["populacao"]:
        menor_populacao = cidade

# Cálculo da população total e média
populacao_total = 0

for cidade in cidades:
    populacao_total += cidade["populacao"]

media_populacional = populacao_total / len(cidades)

# Exibição dos resultados
print("\n=== RESULTADO ===")

print(
    f"Maior população: {maior_populacao['nome']} - "
    f"{maior_populacao['populacao']} habitantes"
)

print(
    f"Menor população: {menor_populacao['nome']} - "
    f"{menor_populacao['populacao']} habitantes"
)

print(f"População total: {populacao_total} habitantes")
print(f"Média populacional: {media_populacional:.2f} habitantes")

print("\n=== CIDADES CADASTRADAS ===")

for cidade in cidades:
    print(f"Nome: {cidade['nome']}")
    print(f"Estado: {cidade['estado']}")
    print(f"População: {cidade['populacao']} habitantes")
    print("-" * 30)