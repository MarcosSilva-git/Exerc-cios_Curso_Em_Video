from random import randint
from time import sleep
jogos = []
nums = []
print('-'*32)
print(f'{"JOGO DA MEGA SENA":^32}')
print('-'*32)
qtd_de_jogos = int(input('Quantos jogos você quer sortear? '))
for i in range(0, qtd_de_jogos):
    for n in range(0, 6):
        x = randint(0, 60)
        if n == 0:
            nums.append(x)
        while True:
            if nums.count(x) == 1:
                x = randint(0, 60)
            else:
                nums.append(x)
                break
    nums.sort()
    jogos.append(nums[:])
    nums.clear()
print('-='*4, end='  ')
print(f'Sorteando {qtd_de_jogos} jogos   ', end='')
print('-='*4)
for qtdJogos in range(1, qtd_de_jogos + 1):
    print(f'{qtdJogos}º Jogo: ', end='')
    print(f'{jogos[qtdJogos - 1]}')
    sleep(1)
print('-='*5, end='- < ')
print('BOA SORTE!', end= ' > ')
print('-='*5, end='-')
