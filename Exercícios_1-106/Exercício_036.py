cores = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[32m',
    'branco': '\033[1;30m',
    'azul': '\033[36m'
}
casaValor = float(input('{}Digite o valor da casa: {}'.format(cores['azul'], cores['limpa'])))
salario = int(input('{}Informe o seu salário: {}'.format(cores['azul'], cores['limpa'])))
anos = int(input('{}Pretende pagar em quantos anos?: {}'.format(cores['azul'], cores['limpa']))) * 12
trintaPorcento = (salario * 30 / 100)
if casaValor / anos > trintaPorcento:
    print('{}Seu empréstimo foi negado!{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('{}A mensalidade da casa será de R${:.2f}.'.format(cores['branco'], casaValor / anos, cores['limpa']))
