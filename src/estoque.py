class Estoque:
    def __init__(self):
        self.estoque = []

    def add_produto(self, produto):
        self.estoque.append(produto)

    def remove_produto(self, identificador):
        for produto in self.estoque:
            if produto.identificador == identificador:
                self.estoque.remove(produto)

    def consultar_estoque(self):
        resultado_da_consulta = ""
        for produto in self.estoque:
            resultado_da_consulta += "\n----------------------------"
            resultado_da_consulta += produto.__str__()
        resultado_da_consulta += "\n----------------------------"
        return resultado_da_consulta
