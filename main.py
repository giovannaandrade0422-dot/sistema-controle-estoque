
import json

# 1. Carregar os produtos salvos
try:
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

except FileNotFoundError:
    produtos = []


# 2. Salvar os produtos no arquivo JSON
def salvar_produtos():
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            produtos,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# 3. Cadastrar um produto
def cadastrar_produto():
    while True:
        # Validar o nome
        while True:
            nome = input("Digite o nome do produto: ").strip()

            if nome:
                break
            else:
                print("O nome do produto não pode ficar vazio.")

        # Validar a quantidade
        while True:
            try:
                quantidade = int(input("Digite a quantidade: "))

                if quantidade >= 0:
                    break
                else:
                    print("A quantidade não pode ser negativa.")

            except ValueError:
                print("Digite um número inteiro válido.")

        # Validar o preço
        while True:
            try:
                preco = float(input("Digite o preço: "))

                if preco >= 0:
                    break
                else:
                    print("O preço não pode ser negativo.")

            except ValueError:
                print("Digite um preço numérico válido.")

        # Criar o produto
        produto = {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }

        produtos.append(produto)
        salvar_produtos()

        print("Produto cadastrado com sucesso!")

        continuar = input(
            "Deseja cadastrar outro produto? (s/n): "
        ).strip().lower()

        if continuar != "s":
            break


# 4. Listar o estoque e calcular os valores
def listar_estoque():
    print("\n===== CONTROLE DE ESTOQUE =====")

    if not produtos:
        print("O estoque está vazio.")
        return

    valor_total_estoque = 0

    for produto in produtos:
        print(f"\nProduto: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")

        valor_produto = (
            produto["quantidade"] * produto["preco"]
        )

        valor_total_estoque += valor_produto

        print(f"Valor total do produto: R$ {valor_produto:.2f}")
        print("-----------------------------")

    print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")


# 5. Consultar um produto pelo nome
def consultar_produto():
    busca = input(
        "Digite o nome do produto que deseja consultar: "
    ).strip()

    for produto in produtos:
        if produto["nome"].lower() == busca.lower():
            print("\n===== PRODUTO ENCONTRADO =====")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: R$ {produto['preco']:.2f}")

            valor_produto = (
                produto["quantidade"] * produto["preco"]
            )

            print(f"Valor total: R$ {valor_produto:.2f}")
            return

    print("Produto não encontrado.")


# 6. Editar um produto
def editar_produto():
    busca = input(
        "Digite o nome do produto que deseja editar: "
    ).strip()

    produto_encontrado = None

    for produto in produtos:
        if produto["nome"].lower() == busca.lower():
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Produto não encontrado.")
        return

    print("\n===== PRODUTO PARA EDIÇÃO =====")
    print(f"Nome: {produto_encontrado['nome']}")
    print(f"Quantidade: {produto_encontrado['quantidade']}")
    print(f"Preço: R$ {produto_encontrado['preco']:.2f}")

    print("\nO que deseja editar?")
    print("1 - Quantidade")
    print("2 - Preço")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        while True:
            try:
                nova_quantidade = int(
                    input("Digite a nova quantidade: ")
                )

                if nova_quantidade < 0:
                    print("A quantidade não pode ser negativa.")
                    continue
                 
                produto_encontrado["quantidade"] = nova_quantidade
                break
            
            except ValueError:
                print("Digite uma quantidade válida.")

    elif opcao == "2":
        while True:
            try:
                novo_preco = float(
                    input("Digite o novo preço: ")
                )

                if novo_preco < 0:
                    print("O preço não pode ser negativo.")
                    continue
                
                produto_encontrado["preco"] = novo_preco
                break

            except ValueError:
                print("Digite um preço válido.")

    else:
        print("Opção inválida.")
        return

    salvar_produtos()
    print("Dados do estoque atualizados com sucesso!")


# 7. Excluir um produto
def excluir_produto():
    busca = input(
        "Digite o nome do produto que deseja excluir: "
    ).strip()

    for produto in produtos:
        if produto["nome"].lower() == busca.lower():
            print(f"Produto encontrado: {produto['nome']}")

            confirmacao = input(
                "Deseja realmente excluir? (s/n): "
            ).strip().lower()

            if confirmacao == "s":
                produtos.remove(produto)
                salvar_produtos()
                print("Produto excluído com sucesso!")
            else:
                print("Exclusão cancelada.")

            return

    print("Produto não encontrado.")


# 8. Menu principal
def menu_principal():
    while True:
        print("\n===== SISTEMA DE CONTROLE DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Consultar produto")
        print("3 - Editar produto")
        print("4 - Excluir produto")
        print("5 - Listar estoque")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            consultar_produto()

        elif opcao == "3":
            editar_produto()

        elif opcao == "4":
            excluir_produto()

        elif opcao == "5":
            listar_estoque()

        elif opcao == "6":
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida. Escolha de 1 a 6.")


# 9. Iniciar o programa
if __name__ == "__main__":
    menu_principal()


