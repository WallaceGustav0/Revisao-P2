biblioteca = []

def adicionar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano = int(input("Ano de publicação: "))
    paginas = int(input("Número de páginas: "))
    

    livro = {'titulo': titulo, 'autor': autor, 'ano': ano, 'paginas': paginas}
    biblioteca.append(livro)


def listar_livros():
    for livro in biblioteca:
        print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) - {livro['paginas']} páginas")


def ordenar_livros():
    criterio = input("Ordenar por 'ano' ou 'paginas': ").strip()
    ordem = input("Ordem 'crescente' ou 'decrescente': ").strip()
    reverse = True if ordem == 'decrescente' else False
    biblioteca.sort(key=lambda x: x[criterio], reverse=reverse)


def salvar_livros():
    try:
        with open('biblioteca.txt', 'w') as f:
            for livro in biblioteca:
                f.write(f"{livro['titulo']}, {livro['autor']}, {livro['ano']}, {livro['paginas']}\n")
        print("Dados salvos no arquivo 'biblioteca.txt'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


def carregar_livros():
    try:
        with open('biblioteca.txt', 'r') as f:
            for line in f:
                titulo, autor, ano, paginas = line.strip().split(',')
                biblioteca.append({'titulo': titulo, 'autor': autor, 'ano': int(ano), 'paginas': int(paginas)})
        print("Dados carregados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")


while True:
    print("\n1. Adicionar livro\n2. Listar livros\n3. Ordenar livros\n4. Salvar livros\n5. Carregar livros\n6. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_livro()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        ordenar_livros()
    elif opcao == '4':
        salvar_livros()
    elif opcao == '5':
        carregar_livros()
    elif opcao == '6':
        break
    else:
        print("Opção inválida. Tente novamente.")