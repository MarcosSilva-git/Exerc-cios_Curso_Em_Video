def celudas(n, x):
    cont = 0
    while True:
        if n < x:
            break
        n -= x
        cont += 1
    if cont > 0:
        print(f'{cont:>2} notas de R${x}')
    return n


def main():
    valor = int(input('Digite o valor a ser sacado: R$'))
    print('Serão retiradas:')
    valor = celudas(valor, 50)
    valor = celudas(valor, 20)
    valor = celudas(valor, 10)
    celudas(valor, 1)


main()
