class PadariaView:
    def __init__(self, controller):
        self.controller = controller

    def mostrar_menu(self):
        print("Bem-vindo a Padaria Seu Jorge!")
        print("1. Ver produtos")
        print("2. Adicionar Produtos")
        print("3. Remover Produtos")
        print("4. Sair")

    def get_escolha_usuario(self):
        escolha = input("Selecione uma opção: ")
        return escolha

    def mostrar_produtos(self, produtos):
        if not produtos:
            print("No products available.")
            return
        print("Produtos Disponíveis:")
        for produto in produtos:
            print(f"- {produto}")

    def get_detalhe_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        return nome, preco

    def mostrar_mensagem(self, mensagem):
        print(mensagem)