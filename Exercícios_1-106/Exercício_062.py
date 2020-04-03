t = int(input('Informe o primeiro valor da PA: '))
r = int(input('Informe a razão da PA: '))
n = 9
i = 1
print('({}, '.format(t), end='')
cont = 1
while i != 0:
    while i <= n:
        t += r
        print('{}, '.format(t), end='')
        i += 1
        cont += 1
    n = int(input('\nGostaria de adicionar quantos elementos a mais nessa PA? '))
    if n == 0:
        i = 0
    else:
        i = 1
print('Progressão finalizada com {} termos mostrados.'.format(cont))