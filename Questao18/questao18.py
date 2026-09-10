# Questão 18 - Simulação de lançamento de dados com análise estatística

import random

print("=== LANÇAMENTO DE DOIS DADOS ===")

# Parte 1 - Lançamento único
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("\n=== LANÇAMENTO ÚNICO ===")
print(f"Primeiro dado: {dado1}")
print(f"Segundo dado: {dado2}")
print(f"Soma: {dado1 + dado2}")

# Parte 2 - Múltiplos lançamentos
quantidade_soma_7 = 0

print("\n=== 10 LANÇAMENTOS ===")

for i in range(1, 11):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    print(f"Lançamento {i}: {dado1} + {dado2} = {soma}")

    if soma == 7:
        quantidade_soma_7 += 1

print(f"\nQuantidade de vezes que a soma foi 7: {quantidade_soma_7}")