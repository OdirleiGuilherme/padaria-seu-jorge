from models.fornecedor import Fornecedor, FornecedorModel
from models.produto import Produto, ProdutoModel
from views.padaria_view import PadariaView

class PadariaController:
    def __init__(self):
        self.view = PadariaView()
        self.fornecedor_model = FornecedorModel()
        self.produto_model = ProdutoModel()
    
    def iniciar(self): # opções de escolha do usuário.
        while True:
            self.view.mostrar_opcoes() 
            escolha = self.view.get_escolha_usuario()

            if escolha == 1:
                self.cadastrar_fornecedores()
            elif escolha == 2:
                self.listar_fornecedores()
            elif escolha == 3:
                self.remover_fornecedores()
            elif escolha == 4:
                self.cadastrar_produtos()                
            elif escolha == 5:
                self.listar_produtos()
            elif escolha == 6:
                self.remover_produtos()
            elif escolha == 0:
                self.view.mostrar_mensagem("Saindo do sistema. Até logo!")
                break
            else:
                self.view.show_invalid_choice_message("Opção inválida. Por favor, selecione uma opção válida.")
                
    def cadastrar_fornecedores(self):
        nome, cnpj, telefone = self.view.get_dados_fornecedor()
        fornecedor = Fornecedor(nome, cnpj, telefone)
        self.fornecedor_model.adicionar_fornecedor(fornecedor)
        self.view.mostrar_mensagem("Fornecedor cadastrado com sucesso!")
        
    def listar_fornecedores(self):
        fornecedores = self.fornecedor_model.listar_fornecedores()
        self.view.exibir_fornecedores(fornecedores)
    
    def remover_fornecedores(self):
        nome, cnpj = self.view.get_nome_fornecedor_remover()
        fornecedor = Fornecedor(nome, cnpj, "")
        if self.fornecedor_model.remover_fornecedor(fornecedor):
            self.view.mostrar_mensagem("Fornecedor removido com sucesso!")
        else:
            self.view.mostrar_mensagem("Fornecedor não encontrado.")