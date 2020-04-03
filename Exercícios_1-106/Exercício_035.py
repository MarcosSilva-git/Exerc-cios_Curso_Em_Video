print('-=-\033[1;30m'*12)
print('\033[36mDigite 3 lados de um triângulo:\033[m')
print('-=-\033[1;30m'*12)
cores = {
    'azulEscuro':'\033[36m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'limpa':'\033[m'
}
l1 = float(input('{}Digite o 1º lado:{} '.format(cores['azulEscuro'], cores['limpa'])))
l2 = float(input('{}Digite o 2º lado:{} '.format(cores['azulEscuro'], cores['limpa'])))
l3 = float(input('{}Digite o 3º lado:{} '.format(cores['azulEscuro'], cores['limpa'])))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('{}Essas medidas podem formar um triângulo.{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Essas medidas não podem formar um triângulo.{}'.format(cores['vermelho'], cores['limpa'])),
