from src.produto import Produto
from src.estoque import Estoque


class Main:
    def __init__(self):
        self.estoque = Estoque()
        self.executa_menu()

    def executa_menu(self):
        print("O que você deseja fazer?\n"
              "1 - Cadastrar produto \n"
              "2 - Remover produto \n"
              "3 - Verificar estoque\n"
              "4 - Sair")
        valor = int(input(":: "))
        if valor == 1:
            self.cadastrar_produto()
        elif valor == 2:
            self.remover_produto()
        elif valor == 3:
            self.verificar_estoque()
        else:
            exit(0)

    def cadastrar_produto(self):
        identificador = int(input("\nDigite o número do código de barras do produto que deseja cadastrar: "))
        preco = float(input("Digite o preço do produto que deseja cadastrar: "))
        descricao = input("Escreva uma breve descrição do produto que deseja cadastrar: ")
        prod = Produto(identificador, preco, descricao)
        self.estoque.add_produto(prod)
        print("\nProduto cadastrado com sucesso\n")
        self.executa_menu()

    def remover_produto(self):
        identificador = int(input("\nDigite o código de barras do produto que deseja remover do estoque: "))
        self.estoque.remove_produto(identificador)
        print("\nProduto removido com sucesso\n")
        self.executa_menu()

    def verificar_estoque(self):
        print(self.estoque.consultar_estoque())
        print("\n")
        self.executa_menu()


main = Main()
