# Questão 19 - Análise linguística completa de uma frase

print("=== ANÁLISE DA FRASE ===")

frase = input("Digite uma frase: ")

# Remove espaços no início e no final
frase = frase.strip()

# Separa as palavras, ignorando espaços extras
palavras = frase.split()

# Junta as palavras com apenas um espaço
frase_organizada = " ".join(palavras)

letra = input("Digite uma letra para pesquisar: ").strip()

# Conta as ocorrências da letra, sem diferenciar maiúsculas e minúsculas
ocorrencias = frase_organizada.lower().count(letra.lower())

print("\n=== RESULTADO ===")
print(f"Quantidade total de caracteres: {len(frase_organizada)}")
print(f"Quantidade de palavras: {len(palavras)}")
print(f"Primeira palavra: {palavras[0]}")
print(f"Última palavra: {palavras[-1]}")
print(f"Quantidade de ocorrências de '{letra}': {ocorrencias}")
print(f"Frase em maiúsculas: {frase_organizada.upper()}")
print(f"Frase em minúsculas: {frase_organizada.lower()}")