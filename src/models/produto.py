class Produto:
    def __init__(self, id_produto, nome_produto, preco_produto, id_fornecedor):
        self.id = id_produto
        self.nome = nome_produto
        self.preco = preco_produto
        self.id_fornecedor = id_fornecedor # adicionando o atributo id_fornecedor para associar o produto a um fornecedor
        
class ProdutoModel:
    def __init__(self):
        self.produtos = []
        
    def salvar(self, produto: Produto):
        self.produtos.append(produto)
    
    def listar_produto(self):
        return self.produtos