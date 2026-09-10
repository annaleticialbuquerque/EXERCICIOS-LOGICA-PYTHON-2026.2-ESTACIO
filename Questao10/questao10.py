# Questão 10 - Análise de temperaturas registradas em uma semana

print("=== ANÁLISE DE TEMPERATURAS ===")

temperaturas = []

for i in range(1, 8):
    temperatura = float(input(f"Digite a temperatura do {i}º dia: "))
    temperaturas.append(temperatura)

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / 7

acima_da_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_da_media += 1

print("\n=== RESULTADO ===")
print("Temperaturas registradas:")

for i, temperatura in enumerate(temperaturas, 1):
    print(f"Dia {i}: {temperatura:.2f} °C")

print(f"\nMaior temperatura: {maior:.2f} °C")
print(f"Menor temperatura: {menor:.2f} °C")
print(f"Temperatura média: {media:.2f} °C")
print(f"Quantidade de dias acima da média: {acima_da_media}")