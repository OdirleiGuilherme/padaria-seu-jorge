from models.fornecedor import Fornecedor, FornecedorModel
from models.produto import Produto, ProdutoModel
from views.padaria_view import PadariaView

class PadariaController:
    def __init__(self):
        self.view = PadariaView()
        self.fornecedor_model = FornecedorModel()
        self.produto_model = ProdutoModel()