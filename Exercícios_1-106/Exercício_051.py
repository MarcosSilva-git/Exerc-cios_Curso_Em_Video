pa = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa pa: '))
print('({}, '.format(pa), end='')
for i in range(1, 10):
    pa += r
    print('{}, '.format(pa), end='')
print('...)')