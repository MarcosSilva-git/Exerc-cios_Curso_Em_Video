listagem = ('Caneta', 2.50, 'Caderno', 11,
            'Lápis', 1, 'Mochila', 129.80,
            'Estojo', 7.99, 'Láspis de cor', 24.06,
            'Camisa', 40.89, 'Calça Jeans', 99.99,
            'Cinto', 9, 'Canetinhas', 20.99)
i = 0
while i != len(listagem):
    contLetras = len(listagem[i])
    print(listagem[i], end=' ')
    i += 1
    preço = listagem[i]
    print(f'{"-"*(22 - contLetras)} R$', end=' ')
    print(f'{preço:>6.2f}')
    i += 1