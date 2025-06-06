# 🏥 Catálogo da Farmácia de Hormônios

Este é um sistema simples de **gerenciamento de produtos** de uma farmácia especializada em hormônios. Ele foi feito com **Python**, usando **Orientação a Objetos**, **validação de dados** e **manipulação de arquivos `.txt`** para guardar os dados.

---

## 📌 Funcionalidades

- 📋 **Listar produtos** salvos no catálogo
- ➕ **Adicionar** novo produto com validação
- ❌ **Remover** produto por código
- ✏️ **Editar** informações de um produto
- 🔍 **<s>Buscar** produtos por nome</s>
- 🔍 **<s>Buscar** produtos por categoria</s>
- 💾 **Salvar e carregar** os dados em um arquivo `produtos.txt`
- ✅ **Verificação automática** de entrada correta (números e letras)

---

## 🧠 Como funciona?

O sistema tem **duas partes principais**:

### 🔹 `main.py`
É o **menu principal**. Mostra as opções para o usuário e usa funções de `catalogo.py`.

### 🔹 `catalogo.py`
Contém a **classe `CatalogoFarmacia`**, onde estão todas as funções para:

- Ler e escrever no arquivo `.txt`
- Adicionar, editar, remover e buscar produtos
- Garantir que o catálogo fique sempre salvo

---

## ✅ Regras de cadastro

| Campo     | Tipo esperado | Validação feita                     |
|-----------|----------------|--------------------------------------|
| Código    | Número         | Só aceita dígitos (`isdigit()`)     |
| Nome      | Texto          | Só aceita letras e espaços          |
| Categoria | Texto          | Só aceita letras e espaços          |
| Preço     | Número         | Aceita `float`, como 10.50 ou 99.99 |

---

## 🧪 Exemplo de uso

```bash
$ python main.py

===== Catálogo da Farmácia de Hormônios =====
1. Listar Produtos
2. Adicionar Produto
3. Remover Produto
4. Editar Produto
5. <s>Buscar por Nome</s>
6. <s>Buscar por Categoria</s>
7. Sair
Escolha uma opção: 2
