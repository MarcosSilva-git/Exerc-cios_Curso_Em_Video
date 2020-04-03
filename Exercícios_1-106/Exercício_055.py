maior = 0
menor = 0
for i in range(1, 6):
    x = float(input('Digite o {}º peso: '.format(i)))
    if i == 1:
        menor = i
        maior = 1
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
print('O maior peso é {} e o menor peso é {}.'.format(maior, menor))
