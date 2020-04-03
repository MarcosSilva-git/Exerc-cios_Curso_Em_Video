from time import sleep
while True:
    n = int(input('>>>>> Digite um número: '))
    print('-'*20)
    print('-'*20)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{i:^2} X {n} = {n * i}')
    print('-'*20)
    print('-'*20)
print('Finalizando...')
sleep(1)
print('\033[31;1mVolte Sempre!')