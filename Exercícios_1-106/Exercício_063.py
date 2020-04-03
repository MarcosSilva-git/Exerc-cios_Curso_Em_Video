n = int(input('Digite a quantidade de números que deseja exibir: '))
cont = 0
f = 1
m = 0
print(f'{m} -> ', end='')
cont += 1
print(f'{f} -> ', end='')
cont += 1
while cont < n:
    print('{} -> '.format(f + m), end='')
    t = f
    f = m + f
    m = t
    cont += 1
print(f"\nACABOU. Você exibiu {cont} termos.")
