from random import randint
tupla = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))
print(f'Os números na tupla são: ',end='')
for i in range(0, len(tupla)):
    print(f'{tupla[i]} ', end='')
print(f'\nO maior deles é {max(tupla)}')
print(f'E o menor é {min(tupla)}')