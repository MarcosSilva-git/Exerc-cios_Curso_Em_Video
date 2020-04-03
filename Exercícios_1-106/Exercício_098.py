from time import sleep


def contador(i, f, p):
    if p < 0:
        p = -p

    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ', flush=True)
            sleep(0.3)

    else:
        while True:
            if p < 0:
                for c in range(i, f - 1, p):
                    print(c, end=' ', flush=True)
                    sleep(0.3)
                break
            else:
                p = -p
    print('FIM!')


print('-=' * 20)
contador(1, 10, 1)
print('-=' * 20)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem')
inicio = int(input('Início: '))
fim    = int(input('Fim:    '))
passo  = int(input('Passo:  '))
contador(inicio, fim, passo)
