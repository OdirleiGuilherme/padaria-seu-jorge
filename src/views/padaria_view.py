class PadariaView:
    def __init__(self, controller):
        self.controller = controller

    def display_menu(self):
        print("Bem-vindo a Padaria Seu Jorge!")
        print("1. Ver produtos")
        print("2. Adicionar Produtos")
        print("3. Remover Produtos")
        print("4. Sair")

    def get_escolha_usuario(self):
        escolha = input("Selecione uma opção: ")
        return escolha

    def display_products(self, products):
        if not products:
            print("No products available.")
            return
        print("Available Products:")
        for product in products:
            print(f"- {product}")

    def get_product_details(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        return name, price

    def display_message(self, message):
        print(message)