print('Digite os lados de um triângulo')
l1 = int(input('Primeiro lado: '))
l2 = int(input('Segundo lado: '))
l3 = int(input('Terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Essas medidas formam um triângulo ', end='')
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('{}EQUILÁTERO{}'.format('\033[1;30m', '\033[m'))
    elif (l1 == l2 or l1 == l3 or l2 == l3) and (l1 != l3 or l1 != l2 or l2 != l3):
        print('{}ISÓCELES{}'.format('\033[1;30m', '\033[m'))
    else:
        print('{}ESCALENO{}'.format('\033[1;30m', '\033[m'))
else:
    print('Essas medidas não formam um triângulo')