def main():

    livros = {}

    emprestimo = {}

    print("Bem vindo ao gerenciamento de livros")

    while True:
        
        print('1 - Listar livros\n' 
        '2 - Remover livros\n' 
        '3 - Atualizar quantidade de livros\n' 
        '4 - Registrar empréstimo\n' 
        '5 - Exibir histórico de empréstimos\n'
        '6 - Sair do programa')

        try:
            opcao = int(input("Digite o numero correspondente a opção desejada\n"))

        except ValueError:
            print("Erro. Digite apenas numeros")
            continue

        if opcao == 1:
            listar_livros(livros)

        elif opcao == 2:
            remover_livros(livros)

        elif opcao == 3:
            atualizar_quantidade(livros)

        elif opcao == 4:
            registrar_emprestimo()

        elif opcao == 5:
            exibir_historico_emprestimo()

        elif opcao == 6:
            print("Finalizando programa.")
            return

        else:
            print("Opção inválida")

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