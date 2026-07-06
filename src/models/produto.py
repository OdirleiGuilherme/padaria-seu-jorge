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
    
    def remover_produto(self, produto: Produto):
        for p in self.produtos:
            if p.nome == produto.nome and p.id_fornecedor == produto.id_fornecedor and p.id == produto.id:
                self.produtos.remove(p)
                return True # removido com sucesso
        return False  # Não encontrado produto para remoção
    
    def remover_produto_por_fornecedor(self, id_fornecedor):
        produtos_removidos = []
        for p in self.produtos:
            if p.id_fornecedor == id_fornecedor:
                produtos_removidos.append(p)
        for p in produtos_removidos:
            self.produtos.remove(p)
        return len(produtos_removidos)  # Retorna a quantidade de produtos removidos
    
    def listar_produto(self):
        return self.produtos
    