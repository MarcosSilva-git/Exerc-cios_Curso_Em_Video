def dobro(n=0, formatado=False):
    n *= 2
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, str(formatado))
    return n


def metade(n=0, formatado=False):
    n /= 2
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, str(formatado))
    return n


def aumentar(n=0, porcentagem=0, formatado=False):
    n += n / 100 * porcentagem
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, str(formatado))
    return n


def diminuindo(n=0, porcentagem=0, formatado=False):
    n -= n / 100 * porcentagem
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, str(formatado))
    return n


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)

    print(f'{"Preço analisado:":<20} {moeda(n)}')
    print(f'{"Dobro do preço:":<20} {dobro(n, True)}')
    print(f'{"Metade do preço:":<20} {metade(n, True)}')
    print(f'{"80% de aumento:":<20} {aumentar(n, 80, True)}')
    print(f'{"35% de redução:":<20} {diminuindo(n, 35, True)}')
    print('-'*30)
    return n
