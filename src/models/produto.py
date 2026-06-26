class Produto:
    def __init__(self, id_produto, nome_produto, preco_produto, id_fornecedor):
        self.id = None
        self.nome = nome_produto
        self.preco = preco_produto
        self.id_fornecedor = id_fornecedor # adicionando o atributo id_fornecedor para associar o produto a um fornecedor
        
class ProdutoModel:
    def __init__(self):
        self.produtos = []
        self.proxima_id = 1  # Inicializa o próximo ID como 1
    
    def salvar(self, produto: Produto):
        produto.id = self.proxima_id # atribui o ID auomaticamente no objeto Produto
        self.produtos.append(produto)
        self.proxima_id += 1 # incrementa o próximo ID para o próximo produto
        return produto.id # retorna o ID do produto cadastrado
    
    def listar_produto(self):
        return self.produtos