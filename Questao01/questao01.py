# Questão 01 - Cadastro e apresentação de perfil pessoal

print("=== CADASTRO DE PERFIL PESSOAL ===")

nome = input("Digite seu nome completo: ")
cidade = input("Digite a cidade onde reside: ")

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade >= 0:
            break
        else:
            print("A idade não pode ser negativa.")
    except ValueError:
        print("Digite um número inteiro válido.")

while True:
    try:
        altura = float(input("Digite sua altura em metros: "))

        if altura > 0:
            break
        else:
            print("A altura deve ser maior que zero.")
    except ValueError:
        print("Digite um valor válido para a altura.")

print("\n===================================")
print("       CARTÃO DE IDENTIFICAÇÃO")
print("===================================")
print(f"Nome completo : {nome}")
print(f"Idade         : {idade} anos")
print(f"Altura        : {altura:.2f} m")
print(f"Cidade        : {cidade}")
print("===================================")