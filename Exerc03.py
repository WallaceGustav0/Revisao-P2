estoque = []

def adicionar_produto():
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade: "))
    
    produto = {'nome': nome, 'categoria': categoria, 'preco': preco, 'quantidade': quantidade}
    estoque.append(produto)


def atualizar_quantidade():
    nome = input("Nome do produto para atualizar: ")
    for produto in estoque:
        if produto['nome'] == nome:
            quantidade = int(input("Nova quantidade: "))
            produto['quantidade'] = quantidade
            print("Quantidade atualizada.")
            return
    print("Produto não encontrado.")


def listar_produtos():
    for produto in estoque:
        preco_formatado = f"R$ {produto['preco']:.2f}"
        print(f"{produto['nome']} - {produto['categoria']} - {preco_formatado} - {produto['quantidade']} unidades")


def ordenar_produtos():
    criterio = input("Ordenar por 'preco' ou 'quantidade': ").strip()
    ordem = input("Ordem 'crescente' ou 'decrescente': ").strip()
    reverse = True if ordem == 'decrescente' else False
    estoque.sort(key=lambda x: x[criterio], reverse=reverse)


def salvar_estoque():
    try:
        with open('estoque.txt', 'w') as f:
            for produto in estoque:
                f.write(f"{produto['nome']}, {produto['categoria']}, {produto['preco']}, {produto['quantidade']}\n")
        print("Dados salvos no arquivo 'estoque.txt'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


def carregar_estoque():
    try:
        with open('estoque.txt', 'r') as f:
            for line in f:
                nome, categoria, preco, quantidade = line.strip().split(',')
                estoque.append({'nome': nome, 'categoria': categoria, 'preco': float(preco), 'quantidade': int(quantidade)})
        print("Dados carregados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")


while True:
    print("\n1. Adicionar produto\n2. Atualizar quantidade\n3. Listar produtos\n4. Ordenar produtos\n5. Salvar estoque\n6. Carregar estoque\n7. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        atualizar_quantidade()
    elif opcao == '3':
        listar_produtos()
    elif opcao == '4':
        ordenar_produtos()
    elif opcao == '5':
        salvar_estoque()
    elif opcao == '6':
        carregar_estoque()
    elif opcao == '7':
        break
    else:
        print("Opção inválida. Tente novamente.")