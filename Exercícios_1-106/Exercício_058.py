from random import randint
num = randint(1, 10)
print('Pensei num número entre 1 e 10.')
n = int(input('Qual número você acha que eu pensei? '))
cont = 1
while num != n:
    if 1 > n or 11 < n:
        print('O número digitado não está dentro do intervalo de 1 até 10.')
        n = int(input('Tente outro número: '))
    else:
        n = int(input('\nErrou. Digite outro número: '))
    cont += 1
print('\n\033[32mAcertou!!'.format(num))
print('Você precisou de {} tentativas para acertar.'.format(cont))
