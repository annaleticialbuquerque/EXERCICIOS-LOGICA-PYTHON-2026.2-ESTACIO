# Questão 05 - Classificação etária com validação de entrada

print("=== CLASSIFICAÇÃO ETÁRIA ===")

while True:
    try:
        idade = int(input("Digite a idade: "))

        if idade >= 0:
            break
        else:
            print("Erro: a idade não pode ser negativa.")
    except ValueError:
        print("Erro: digite uma idade válida.")

if idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"\nA idade informada é {idade} anos.")
print(f"Classificação etária: {classificacao}")