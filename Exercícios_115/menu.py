cores = {
    "limpa": "\033[m",
    "vermelho": "\033[31m"
}


def menu():
    print('--------')
    print('[ 1 ] Vizualizar Pessoas Cadastradas')
    print('[ 2 ] Cadastrar')
    print('[ 3 ] Sair')
    print('--------')

    while True:
        try:
            opcao = int(input('Digite uma opção: '))
            if not (0 < opcao <= 3):
                print(f'{cores["vermelho"]}Error. Digite uma das três opções acima.{cores["limpa"]}')
            else:
                break
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}Error. Digite uma das três opções acima.{cores["limpa"]}')
        except KeyboardInterrupt:
            return 3

    return opcao
