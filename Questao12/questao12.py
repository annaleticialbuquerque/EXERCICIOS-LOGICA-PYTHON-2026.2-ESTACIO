# Questão 12 - Cadastro e inventário de produtos em estoque

print("=== CADASTRO DE PRODUTOS ===")

produtos = []

for i in range(1, 6):
    print(f"\nProduto {i}")

    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

# Cálculo do valor total do estoque
valor_total = 0

for produto in produtos:
    valor_total += produto["preco"] * produto["quantidade"]

# Identificação do produto com maior preço
produto_maior_preco = produtos[0]

for produto in produtos:
    if produto["preco"] > produto_maior_preco["preco"]:
        produto_maior_preco = produto

# Exibição dos produtos
print("\n=== PRODUTOS CADASTRADOS ===")

for produto in produtos:
    print(f"Nome: {produto['nome']}")
    print(f"Preço unitário: R$ {produto['preco']:.2f}")
    print(f"Quantidade em estoque: {produto['quantidade']}")
    print("-" * 30)

print(f"\nValor total do estoque: R$ {valor_total:.2f}")
print(f"Produto com maior preço unitário: {produto_maior_preco['nome']}")
print(f"Maior preço unitário: R$ {produto_maior_preco['preco']:.2f}")