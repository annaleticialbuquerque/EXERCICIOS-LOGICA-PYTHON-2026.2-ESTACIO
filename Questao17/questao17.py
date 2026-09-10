# Questão 17 - Cálculos matemáticos com o módulo math

import math

print("=== CÁLCULOS MATEMÁTICOS ===")

numero = float(input("Digite um número real: "))

print("\n=== RESULTADOS ===")

if numero >= 0:
    print(f"Raiz quadrada: {math.sqrt(numero):.2f}")
else:
    print("Raiz quadrada: não é possível calcular para número negativo.")

print(f"Valor absoluto: {math.fabs(numero):.2f}")
print(f"Arredondamento para cima: {math.ceil(numero)}")
print(f"Arredondamento para baixo: {math.floor(numero)}")

if numero.is_integer() and numero >= 0:
    print(f"Fatorial: {math.factorial(int(numero))}")
else:
    print("Fatorial: disponível somente para números inteiros não negativos.")