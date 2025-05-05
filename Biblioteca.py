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
            adicionar_livros(livros)

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

def adicionar_livros(livros):
    
    print("Você está no menu de adicionar livros")

    while True:
         
        print("Digite a opção desejada")
        print('1 - Adicionar livro\n'
              '2 - Voltar ao menu principal')

        try:
            opcao = int(input())
        except ValueError:
            print("Erro. Digite apenas números")
            continue

        while True:

            if opcao == 1:
                titulo = input("Digite o titulo do livro\n")
                autor = input("Digite o nome do autor\n")
                
                try:
                    exemplares = int(input("Digite a quantidade de exemplares\n"))
                except ValueError:
                    print("Erro. Apenas números são permitidos nos exemplares")
                    continue

                if titulo not in livros:
                    livros[titulo] = {"Autor": autor, "Exemplares": exemplares}
                    print(f"o livro {titulo} foi adicionado com sucesso ao sistema!")
                else:
                    print("Esse livro ja existe no sistema")

            elif opcao == 2:
                return
            
            else:
                print("Opção inválida")

            while True:

                try:
                    opcao = int(input("Deseja adicionar outro livro?\nDigite 1 para sim\nDigite 2 para voltar ao menu principal\n"))
                except ValueError:
                    print("Erro. Digite apenas números")
                    continue

                if opcao == 1:
                    break

                elif opcao ==2:
                    return
                
                else:
                    print("Opção inválida")

def listar_livros(livros):
    
    while True:

        print('1 - Listar livros\n'
        '2 - Voltar ao menu principal')

        try:
            opcao = int(input("Digite a opção desejada\n"))
        except ValueError:
            print("Erro. Digite apenas numero")

        if opcao == 1:
            for livro in sorted(livros):
                print(livro, livros[livro])
            return

        elif opcao == 2:
            return
        
        else:
            print("Opção indisponivel")

def remover_livros(livros):
    
     while True:

        print('1 - Remover livro\n'
        '2 - Voltar ao menu principal')

        try:
            opcao = int(input("Digite a opção desejada\n"))
        except ValueError:
            print("Erro. Digite apenas numero")

        while True:
            if opcao == 1:
                nome_livro = input("Digite o nome do livro que deseja remover\n")
                if nome_livro in livros:
                    livros.pop(nome_livro)
                    print(f"O livro '{nome_livro}' foi removido com sucesso.")
                else:
                    print("Livro não encontrado.")

            elif opcao == 2:
                return
            
            else:
                print("Opção indisponivel")

            while True:

                try:
                    repetir = int(input("Deseja remover outro livro?\n1 - sim\n2 - não\n"))
                except ValueError:
                    print("Erro. Digite apenas numeros")

                if repetir == 1:
                    break

                elif repetir == 2:
                    return

                else: 
                    print("Opção inválida")

def atualizar_quantidade(livros):
    print("Teste")
    pass

def registrar_emprestimo():
    print("Teste")
    pass

def exibir_historico_emprestimo():
    print("Teste")
    pass

main()