from random import randint

numeros = []


def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        al = randint(1, 10)
        numeros.append(al)
        print(al, end=' ')
    print()


def somaPar(lista):
    print(f'Somando os valores pares de {lista} temos: ', end='')
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(s)


sorteio()
somaPar(numeros)
