t = int(input('Informe o 1º termo da PA: '))
r = int(input('Informe a razão da PA: '))
print('({}, '.format(t), end='')
i = 1
while i < 10:
    t += r
    print('{}, '.format(t), end='')
    i += 1
print('...)')