from time import sleep

def maior(*x):
    print('-=' * 20)
    print('Analisando os valores passados...')
    for e in x:
        print(e, end=' ', flush=True)
        sleep(0.3)

    print(f'Foram informados {len(x)} valores ao todo.')
    print(f'O maior valor informado foi {(max(x) if (len(x) > 0) else 0)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
