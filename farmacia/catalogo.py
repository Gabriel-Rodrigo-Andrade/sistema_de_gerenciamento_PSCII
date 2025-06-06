class Produto:
    def __init__(self, codigo, nome, categoria, preco):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def __str__(self):
        return f"{self.codigo};{self.nome};{self.categoria};{self.preco}"


class CatalogoFarmacia:
    def __init__(self, arquivo='catalogo.txt'):
        self.arquivo = arquivo
        self.produtos = []
        self.carregar_produtos()

    def carregar_produtos(self):
        try:
            with open(self.arquivo, 'r') as file:
                for linha in file:
                    dados = linha.strip().split(';')
                    if len(dados) == 4:
                        codigo, nome, categoria, preco = dados
                        self.produtos.append(Produto(codigo, nome, categoria, float(preco)))
        except FileNotFoundError:
            with open(self.arquivo, 'w'):  # Cria o arquivo vazio
                pass

    def salvar_produtos(self):
        with open(self.arquivo, 'w') as file:
            for produto in self.produtos:
                file.write(str(produto) + '\n')

    def adicionar_produto(self, codigo, nome, categoria, preco):
        if any(p.codigo == codigo for p in self.produtos):
            print("Código já existe. Produto não adicionado.")
            return
        try:
            preco = float(preco)
            novo = Produto(codigo, nome, categoria, preco)
            self.produtos.append(novo)
            self.salvar_produtos()
            print("Produto adicionado com sucesso!")
        except ValueError:
            print("Preço inválido!")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto no catálogo.")
            return
        print("\nCatálogo Atual:")
        for produto in self.produtos:
            print(f"Código: {produto.codigo} | Nome: {produto.nome} | Categoria: {produto.categoria} | Preço: R${produto.preco:.2f}")

    def remover_produto(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                self.produtos.remove(p)
                self.salvar_produtos()
                print("Produto removido com sucesso!")
                return
        print("Produto não encontrado.")

    def editar_produto(self, codigo, novo_nome, nova_categoria, novo_preco):
        for p in self.produtos:
            if p.codigo == codigo:
                try:
                    p.nome = novo_nome
                    p.categoria = nova_categoria
                    p.preco = float(novo_preco)
                    self.salvar_produtos()
                    print("Produto editado com sucesso!")
                    return
                except ValueError:
                    print("Preço inválido!")
                    return
        print("Produto não encontrado.")