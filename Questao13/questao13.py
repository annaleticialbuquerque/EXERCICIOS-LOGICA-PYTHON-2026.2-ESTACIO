# Questão 13 - Agenda de contatos com funcionalidade de consulta

print("=== AGENDA DE CONTATOS ===")

contatos = []

for i in range(1, 6):
    print(f"\nContato {i}")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

nome_consulta = input("\nDigite o nome do contato que deseja consultar: ")

encontrado = False

for contato in contatos:
    if contato["nome"].lower() == nome_consulta.lower():
        print("\n=== CONTATO ENCONTRADO ===")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        encontrado = True
        break

if not encontrado:
    print("Contato não encontrado.")