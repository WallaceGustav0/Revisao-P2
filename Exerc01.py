alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    notas = []
    while len(notas) < 2 or len(notas) > 5:
        notas = list(map(float, input("Digite as notas do aluno separadas por espaço (mínimo 2, máximo 5): ").split()))
    
    media = sum(notas) / len(notas)
    
    aluno = {'nome': nome, 'notas': notas, 'media': media}
    alunos.append(aluno)


def ordenar_alunos():
    criterio = input("Ordenar por 'media' ou 'nota' específica? ").strip().lower()
    if criterio == 'media':
        alunos.sort(key=lambda x: x['media'], reverse=True)

    elif criterio == 'nota':
        nota_index = int(input(f"Escolha a nota para ordenar (1 a {len(alunos[0]['notas'])}): ")) - 1
        alunos.sort(key=lambda x: x['notas'][nota_index] if nota_index < len(x['notas']) else 0, reverse=True)
    else:
        print("Critério inválido. Ordenação não realizada.")


def salvar_em_arquivo():
    try:
        with open('alunos.txt', 'w') as f:
            for aluno in alunos:
                notas_str = ", ".join(f"{nota:.1f}" for nota in aluno['notas'])
                f.write(f"{aluno['nome']}, Média: {aluno['media']:.2f}, Notas: {notas_str}\n")
        print("Dados salvos no arquivo 'alunos.txt'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


while True:
    print("\n1. Adicionar aluno\n2. Listar alunos ordenados\n3. Salvar em arquivo\n4. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        ordenar_alunos()
        for aluno in alunos:
            notas_str = ", ".join(f"{nota:.1f}" for nota in aluno['notas'])
            print(f"{aluno['nome']} - Notas: {notas_str} - Média: {aluno['media']:.2f}")
    elif opcao == '3':
        salvar_em_arquivo()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")