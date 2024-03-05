import json
import os
import time

compras = {}
teste = {}


def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade


def remover_item(compras, item):
    if item in compras:
        del item


def visualizar_lista(compras):
    for item, quantidade in compras.items():
        print(f"{item}: {quantidade}")
    input("\nPressione enter para continuar\n")


def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(compras, arquivo)


def carregar_compras(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        return json.load(arquivo)


def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 - adicionar item")
        print("2 - remover item")
        print("3 - visualizar lista")
        print("4 - Salvar e sair")
        print("5 - Sair sem salvar")
        escolha = input("\nDigite uma opção: ")
        if escolha == "1":
            item = input("\nDigite o nome do item: ")
            qtde = input("Digite a quantidade: ")
            adicionar_item(compras, item, qtde)
        elif escolha == "2":
            item = input("\nDigite o nome do item: ")
            remover_item(compras, item)
        elif escolha == "3":
            print()
            visualizar_lista(compras)
        elif escolha == "4":
            if nome_arquivo is None:
                nome_arquivo = input("\nDigite o nome do arquivo para salvar: ")
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += ".json"
            salvar_compras(compras, nome_arquivo)
            break
        elif escolha == "5":
            break
        else:
            print("Opção inválida")
            time.sleep(1)


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 - Criar uma nova lista")
        print("2 - Gerenciar listas")
        print("3 - Sair")
        escolha = input("Digite uma opção: ")

        if escolha == "1":
            compras = {}
            gerenciar_compras(compras)
        elif escolha == "2":
            print("Listas disponíveis:\n")
            arquivos = [arquivo for arquivo in os.listdir()
                        if arquivo.endswith(".json")]
            if not arquivos:
                print("Sem listas salvas...")
                time.sleep(2)
            for i, arquivo in enumerate(arquivos, 1):
                print(f"{i} - {arquivo}")
            escolha = int(
                input("Digite o numero da lista para carregar (0 se nenhuma): "))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print("Opção inválida")
                time.sleep(1)
                continue
            nome_arquivo = arquivos[escolha - 1]
            compras = carregar_compras(nome_arquivo)
            gerenciar_compras(compras, nome_arquivo)
        
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")
            time.sleep(1)


if __name__ == "__main__":
    main()
