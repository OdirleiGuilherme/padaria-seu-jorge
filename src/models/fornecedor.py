class Fornecedor: 
    def __init__(self, id_fornecedor, nome_fornecedor, cnpj_fornecedor, telefone_fornecedor):
        self.id = None  # Inicializa o ID como None, será atribuído posteriormente
        self.nome = nome_fornecedor
        self.cnpj = cnpj_fornecedor
        self.telefone = telefone_fornecedor
        
class FornecedorModel:
    def __init__(self):
        self.fornecedores = []
        self.proxima_id = 1  # Inicializa o próximo ID como 1
        
    def salvar(self, fornecedor: Fornecedor):
        fornecedor.id = self.proxima_id # atribui o ID auomaticamente no objeto Fornecedor
        self.fornecedores.append(fornecedor)
        self.proxima_id += 1 # incrementa o próximo ID para o próximo fornecedor
        return fornecedor.id # retorna o ID do fornecedor cadastrado    
    
    def listar_fornecedor(self):
        return self.fornecedores
    
    def remover_fornecedor(self, fornecedor: Fornecedor):
        for f in self.fornecedores:
            if f.nome == fornecedor.nome and f.cnpj == fornecedor.cnpj and f.id == fornecedor.id:
                self.fornecedores.remove(f)
                return True # removido com sucesso
        return False  # Não encontrado forncedor para remoção
        