def dobro(n=0, formatado=False):
    n *= 2
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, formatado)
    return n


def metade(n=0, formatado=False):
    n /= 2
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, formatado)
    return n


def aumentar(n=0, porcentagem=0, formatado=False):
    n += n / 100 * porcentagem
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, formatado)
    return n


def diminuindo(n=0, porcentagem=0, formatado=False):
    n -= n / 100 * porcentagem
    if formatado:
        if formatado == True:
            n = moeda(n)
        else:
            n = moeda(n, formatado)
    return n


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
