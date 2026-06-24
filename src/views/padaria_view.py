class PadariaView:
    def __init__(self, controller):
        self.controller = controller

    def mostrar_menu(self):
        print("Bem-vindo a Padaria Seu Jorge!")
        print("1. Cadastrar Fornecedores")
        print("2. Listar Fornecedores")
        print("3. Remover Fornecedores")
        print("4. Cadastrar Produtos")
        print("5. Listar produtos")
        print("6. Remover Produtos")
        print("0. Sair")

    def get_escolha_usuario(self):
        escolha = input("Selecione uma opção: ")
        return escolha
    
    def get_dados_fornecedor(self): # Cadastrar dados fornecedores
        nome = input("Digite o nome do fornecedor: ")
        cnpj = input("Digite o CNPJ do fornecedor: ")
        telefone = input("Digite o telefone do fornecedor: ")
        return nome, cnpj, telefone
    
    def exibir_fornecedores(self, fornecedores): # Exibir fornecedores cadastrados
        if not fornecedores:
            print("Sem fornecedores disponíveis.")
            return
        print("Fornecedores Disponíveis:")
        for fornecedor in fornecedores:
            print(f"- {fornecedor}")
    
    def get_nome_fornecedor_remover(self): # Remove fornecedores cadastrados
        nome = input("Digite o nome do fornecedor a ser removido: ")
        cnpj = input("Digite o CNPJ do fornecedor a ser removido: ")
        return nome, cnpj
  

    def get_dados_produto(self): # Cadastrar produtos adquiridos
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        return nome, preco
    
    
    def exibir_produtos(self, produtos): # Exibir produtos cadastrados
            if not produtos:
                print("Sem produtos disponíveis.")
                return
            print("Produtos Disponíveis:")
            for produto in produtos:
                print(f"- {produto}")
                
    def get_nome_produto_remover(self): # Remove produtos cadastrados
         nome = input("Digite o nome do produto que deseja remover: ")
         return nome

    def mostrar_mensagem(self, mensagem):
        print(mensagem)