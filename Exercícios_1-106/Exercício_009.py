x = int(input('Digite um número: '))
y = 1

while y <= 10:
    soma = x *  y
    print('{} + {:2} = {}'.format(x, y, soma))
    y = y + 1
print('='*12)