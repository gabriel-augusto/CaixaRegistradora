class Produto:
    def __init__(self, identificador, preco, descricao=None):
        self.identificador = identificador
        self.preco = preco
        self.descricao = descricao

    def __str__(self):
        return "\nID: " + str(self.identificador) \
               + "\nPreço: " + str(self.preco) \
               + "\nDescrição: " + str(self.descricao) \
