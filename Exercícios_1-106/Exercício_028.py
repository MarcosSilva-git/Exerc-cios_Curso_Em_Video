from pygame import time, init
from random import randint
x = randint(0, 5)
num = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
init()
time.wait(2000)
if num == x:
    print('PARABÉNS! Você venceu!!')
    print('Você acertou o número que eu pensei.')
else:
    print('GANHEI!!')
    print('Eu pensei em {} e não {}'.format(x, num))
