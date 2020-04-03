def fatorial(num, show=False):
    """
    -> Retorna o fatorial de um número
    :param num: número que deseja calcular o fatorial
    :param show: "True" caso deseje mostrar a conta
    :return: fatorial do número
    """
    fat = 1
    if show == True:
        while num > 1:
            print(f'{num}x', end='')
            fat *= num
            num -= 1
        print(f'1 =', fat)
    else:
        print(num, end=' ')
        while num > 1:
            fat *= num
            num -= 1
        print('=', fat)
    return fat


print('-='*12)
fatorial(7, show=True)
fatorial(7)
print('-='*12)
help(fatorial)
