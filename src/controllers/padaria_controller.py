from models.fornecedor import Fornecedor, FornecedorModel
from models.produto import Produto, ProdutoModel
from views.padaria_view import PadariaView

class PadariaController:
    def __init__(self):
        self.view = PadariaView()
        self.fornecedor_model = FornecedorModel()
        self.produto_model = ProdutoModel()
    
    def iniciar(self):
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
                self.view.show_invalid_choice_message()