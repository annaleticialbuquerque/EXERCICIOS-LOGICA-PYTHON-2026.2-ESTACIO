# Questão 08 - Estatística descritiva de conjunto numérico

print("=== RELATÓRIO ESTATÍSTICO ===")

soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))

    soma += numero

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

media = soma / 10

print("\n=== RESULTADO ===")
print(f"Soma dos números: {soma}")
print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Média aritmética: {media:.2f}")