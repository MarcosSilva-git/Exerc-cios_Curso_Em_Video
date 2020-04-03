num = []
valor = 0
while True:
    valor = int(input('Digite um número: '))
    if num.count(valor) == 0:
        num.append(valor)
        print(f'\033[34;1mNumero novo!\033[m Número {valor} foi cadastrado com sucesso. ')
    else:
        print(f'\033[31;1mNúmero repetido!\033[m Número {valor} não foi cadastro. ')
    valor = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while not (valor in 'SN'):
        valor = str(input('Não entendi. Deseja continuar? [S/N] ')).strip().upper()[0]
    if valor in 'N':
        break
print(f'\033[33;1mOs valores digitados foram: \033[m', end='')
num.sort()
for i in range(0, len(num)):
    print(num[i], end=' ')
