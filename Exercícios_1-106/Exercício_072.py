from time import sleep
numeros = (
  'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
  'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
  'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
  'dezoito', 'dezenove', 'vinte'
)
while True:
    while True:
        x = int(input('Digite um número entre 0 e 20: '))
        if -1 >= x or x >= 21:
            print('Tente novamente. ',end='')
        else:
            break
    print(f'O número digitado foi {numeros[x]}')
    x = input('Deseja continuar? [S/N]: ').capitalize().strip()[0]
    while not x in 'SN':
        x = input('Tente novamente. Deseja continuar? [S/N]').capitalize().strip()[0]
    if x in 'N':
        break
print('Finalizando...')
sleep(1)
print('\033[31;1mVolte Sempre')
