def dobro(n=0):
    return n*2


def metade(n=0):
    return n / 2


def aumentar(n=0, porcentagem=0):
    return n + (n / 100 * porcentagem)


def diminuindo(n=0, porcentagem=0):
    return n - (n / 100 * porcentagem)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
