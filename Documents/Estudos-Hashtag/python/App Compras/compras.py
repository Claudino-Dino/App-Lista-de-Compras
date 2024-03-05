import time
import json

compras = {}


def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade


def remover_item(compras, item):
    if item in compras:
        del compras[item]


def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f"{item}: {quantidade}")
    print("\nPressione enter para continuar.")
    # input()


def salvar_compras(compras, nome_arquivo):
    with open("nome_arquivo", "w") as arquivo:
        json.dump(compras, arquivo)


def carregar_compras(nome_arquivo):
    with open("nome_arquivo", "r") as arquivo:
        dicionario_leitura = json.load(arquivo)


def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        print("Adicionar item")
        print("Remover item")
        print("Visualizar lista")
        print("Salvar e sair")
        print("Sair sem salvar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Digite o nome do item: ")
            qtde = int(input("Digite a quantidade"))
            adicionar_item(compras, item, qtde)

        elif escolha == "2":
            item = input("Digite o nome do item: ")
            remover_item(compras, item)
        elif escolha == "3":
            visualizar_compras(compras)
        elif escolha == "4":
            if nome_arquivo is None:
                nome_arquivo = input("Digite o nome do arquivo para salvar: ")
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += ".json"
            salvar_compras(compras, nome_arquivo)

            break
        elif escolha == "5":
            break
        else:
            print("Opção inválida")
            time.sleep(2)


def main():
    while True:
        print("1 Criar uma nova lista de compras")
        print("2 Carregar uma lista existente")
        print("3 Sair")
        escolha = input("- Escolha uma opção: ")
        if escolha == "1":
            compras = {}
            gerenciar_compras(compras)

        elif escolha == "2":
            pass

        elif escolha == "3":
            break

        else:
            print("Opção inválida")
            time.sleep(2)


if __name__ == "__main__":
    main()
