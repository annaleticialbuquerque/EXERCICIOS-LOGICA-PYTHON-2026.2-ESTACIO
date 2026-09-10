# Questão 09 - Geração de tabuada de multiplicação

print("=== TABUADA DE MULTIPLICAÇÃO ===")

numero = int(input("Digite um número inteiro: "))

print(f"\n=== TABUADA DO {numero} ===")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")