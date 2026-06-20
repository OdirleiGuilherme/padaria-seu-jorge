class Fornecedor: 
    def __init__(self, id_fornecedor, nome_fornecedor, cnpj_fornecedor, telefone_fornecedor):
        self.id = id_fornecedor
        self.nome = nome_fornecedor
        self.cnpj = cnpj_fornecedor
        self.telefone = telefone_fornecedor
        
class FornecedorModel:
    def __init__(self):
        self.fornecedores = []
        
    def salvar(self, fornecedor: Fornecedor):
        self.fornecedores.append(fornecedor)
        
    def listar_fornecedor(self):
        return self.fornecedores
        