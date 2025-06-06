from catalogo import CatalogoFarmacia

# Função que exibe o menu
def menu():
    print("\n===== Catálogo da Farmácia de Hormônios =====")
    print("1. Listar Produtos")
    print("2. Adicionar Produto")
    print("3. Remover Produto")
    print("4. Editar Produto")
    print("5. Sair")  # Agora "Sair" é a opção 5

# Cria uma instância do catálogo
catalogo = CatalogoFarmacia()

# Funções de validação de entrada:
def input_codigo():
    while True:
        codigo = input("Código (número): ")
        if codigo.isdigit():
            return codigo
        print("Código inválido. Digite apenas números.")

def input_nome():
    while True:
        nome = input("Nome: ")
        if nome.replace(" ", "").isalpha():
            return nome
        print("Nome inválido. Use apenas letras.")

def input_categoria():
    while True:
        categoria = input("Categoria: ")
        if categoria.replace(" ", "").isalpha():
            return categoria
        print("Categoria inválida. Use apenas letras.")

def input_preco():
    while True:
        preco = input("Preço (ex: 99.99): ")
        try:
            float(preco)
            return preco
        except ValueError:
            print("Preço inválido. Digite um número válido.")

# Loop principal do menu
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        catalogo.listar_produtos()

    elif opcao == '2':
        codigo = input_codigo()
        nome = input_nome()
        categoria = input_categoria()
        preco = input_preco()
        catalogo.adicionar_produto(codigo, nome, categoria, preco)

    elif opcao == '3':
        codigo = input("Código do produto a remover: ")
        catalogo.remover_produto(codigo)

    elif opcao == '4':
        codigo = input("Código do produto a editar: ")
        nome = input_nome()
        categoria = input_categoria()
        preco = input_preco()
        catalogo.editar_produto(codigo, nome, categoria, preco)

    elif opcao == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")