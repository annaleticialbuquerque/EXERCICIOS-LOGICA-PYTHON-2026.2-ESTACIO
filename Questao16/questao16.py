# Questão 16 - Sistema interativo com menu de opções

numeros = []

while True:
    print("\n================================")
    print(" GERENCIAMENTO DE NÚMEROS")
    print("================================")
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = float(input("Digite um número: "))
        numeros.append(numero)
        print("Número cadastrado com sucesso.")

    elif opcao == "2":
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print("\nNúmeros cadastrados:")
            for numero in numeros:
                print(numero)

    elif opcao == "3":
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            maior = max(numeros)
            print(f"Maior número: {maior}")

    elif opcao == "4":
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            menor = min(numeros)
            print(f"Menor número: {menor}")

    elif opcao == "5":
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            media = sum(numeros) / len(numeros)
            print(f"Média: {media:.2f}")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Digite uma opção de 0 a 5.")