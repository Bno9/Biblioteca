def main():

    livros = {}

    emprestimo = {}

    print("Bem vindo ao gerenciamento de livros")

    while True:
        
        print('1 - Adicionar livros\n'
        '2 - Listar livros\n' 
        '3 - Remover livros\n' 
        '4 - Atualizar quantidade de livros\n' 
        '5 - Registrar empréstimo\n' 
        '6 - Exibir histórico de empréstimos\n'
        '7 - Sair do programa')

        try:
            opcao = int(input("Digite o numero correspondente a opção desejada\n"))

        except ValueError:
            print("Erro. Digite apenas numeros")
            continue

        if opcao == 1:
            registrar_livros(livros)

        elif opcao == 2:
            listar_livros(livros)

        elif opcao == 3:
            remover_livros(livros)

        elif opcao == 4:
            atualizar_quantidade(livros)

        elif opcao == 5:
            registrar_emprestimo()

        elif opcao == 6:
            exibir_historico_emprestimo()

        elif opcao == 7:
            print("Finalizando programa.")
            return

        else:
            print("Opção inválida")

def registrar_livros():
    print("Teste")
    pass

def listar_livros():
    print("Teste")
    pass

def remover_livros():
    print("Teste")
    pass

def atualizar_quantidade():
    print("Teste")
    pass

def registrar_emprestimo():
    print("Teste")
    pass

def exibir_historico_emprestimo():
    print("Teste")
    pass



main()