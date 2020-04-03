from time import sleep
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31;1m',
    'azul': '\033[34;1m',
    'verde': '\033[32;1m'
}

n1 = int(input('{}Digite um número: {}'.format(cores['azul'], cores['limpa'])))
n2 = int(input('{}Digite outro número: {}'.format(cores['azul'], cores['limpa'])))
m = 0
while m != 5:
    print('''{1}[1]{2} Somar
{1}[2]{2} Multiplicar
{1}[3]{2} Maior
{1}[4]{2} Novos Números
{1}[5]{2} Sair do Programa{0}'''.format(cores['limpa'], cores['vermelho'], cores['verde']))
    m = int(input('Escolha a ação que você deseja executar: '))
    if m == 1:
        resultado = n1 + n2
        print('O resultado da soma de {1}{2}{0} + {1}{3}{0} é igual a {1}{4}{0}.'.format(cores['limpa'],cores['vermelho'], n1, n2, resultado))
    elif m == 2:
        resultado = n1 * n2
        print('O resultado da multiplicação de {1}{2}{0} X {1}{3}{0} é igual a {1}{4}{0}.'.format(cores['limpa'],cores['vermelho'],n1,  n2, resultado))
    elif m == 3:
        if n1 > n2:
            print('O maior entre os dois números é {1}{2}{0}.'.format(cores['limpa'], cores['vermelho'], n1))
        else:
            print('O maior entre os dois números é {1}{2}{0}.'.format(cores['limpa'], cores['vermelho'], n2))
    elif m == 4:
        n1 = int(input('{1}Digite um número: {0}'.format(cores['limpa'], cores['azul'])))
        n2 = int(input('{1}Digite um número:{0} '.format(cores['limpa'], cores['azul'])))
    elif m == 5:
        print('Finalizando...')
    while not (1 <= m <= 5):
        m = int(input('Selecione uma ação válida: '))
    sleep(1)
print('{}Obrigado por usar o programa'.format(cores['vermelho']))