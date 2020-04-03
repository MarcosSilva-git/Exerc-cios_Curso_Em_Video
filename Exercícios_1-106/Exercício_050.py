print('Digite 6 números')
soma = 0
cont =  0
for i in range(1, 7):
    n = int(input('Digite o {}º número: '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma de todos os {} números pares é {}.'.format(cont, soma))