# Questão 11 - Relatório analítico de lista numérica

print("=== RELATÓRIO DE LISTA NUMÉRICA ===")

numeros = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(numero)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("\n=== RESULTADO ===")
print(f"Números informados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")