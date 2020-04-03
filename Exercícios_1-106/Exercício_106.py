cores = {
    "limpa": "\033[m",
    "vermelho": "\033[31;1m",
    "verde": "\033[32;1m",
    "azul": "\033[34;1m",
    "branco": "\033[36;1m"
}


def main():
    titulo('Bem-Vindo ao Interactive Help!', p=True)
    while True:
        func = str(input(f'{cores["azul"]}>> Digite a Função ou Biblioteca que deseja pesquisar: {cores["limpa"]}')).strip().lower()
        if func != 'fim':
            helper(func)
        else:
            break
    print('<< CONTE SEMPRE CONOSCO ;) >>')


def titulo(msg, p=False):

    print('~'*(len(msg) + 4))
    if p:
        print(f'{cores["verde"]}  {msg}  {cores["limpa"]}')
    else:
        print(f'{cores["azul"]}  {msg}  {cores["limpa"]}')
    print('~'*(len(msg) + 4))


def helper(func):
    from time import sleep
    titulo(f'Pesquisando a função {func}', p=True)
    sleep(0.5)
    help(func)


main()



