cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azulClaro': '\033[34m',
}
num = int(input('{}Digite um número: {}'.format(cores['azulClaro'], cores['limpa'])))
print('''- {0}1{1} Para {2}binário{1}
- {0}2{1} Para {2}octal{1}
- {0}3{1} Para {2}hexadecimal{1}'''.format(cores['vermelho'], cores['limpa'], cores['amarelo']))
base = int(input('{}Informe a base de conversão: {}'.format(cores['azulClaro'], cores['limpa'])))
if base == 1:
    base = str(bin(num))
    print('O número {1}{2}{0} em binário é igual a {1}{3}{0}'.format(cores['limpa'], cores['vermelho'], num, base[2:]))
elif base == 2:
    base = str(oct(num))
    print('O número {0}{2}{1} em octal é igual a {0}{3}{1}'.format(cores['vermelho'], cores['limpa'], num, base[2:]))
else:
    base = str(hex(num))
    print('O número {1}{2}{0} em hexadecimal é igual a {1}{3}{0}'.format(cores['limpa'], cores['vermelho'], num, base[2:]))
