cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31;1m',
    'verde': '\033[32;1m',
    'azul': '\033[34;1m'
}

palavras = ('Viver', 'Estudar', 'Harmônico', 'Vencer', 'Conviver',
            'Resultado', 'Avaliar', 'Comer', 'Sentir', 'Proparoxítona',
              'Paralelepípedo', 'Otorrinolaringologista'
            )

i = letras = x = 0

for i in range(len(palavras)):
    palavra = str(palavras[i]).capitalize()
    letras = len(palavras[i])
    print('A palavra "{1}{3}{0}" tem {2}{4}{0} letras'.format(cores['limpa'], cores['azul'], cores['vermelho'], palavra,
                                                              letras))
    palavra = palavra.lower()
    print(f'As vogais dessa palavra são: ', end='')
    for x in range(0, letras):
        if palavra[x] in 'aáãeéêiíoóôõuú':
            print('{}{}{} '.format(cores['azul'], palavra[x], cores['limpa']), end='')
    print(end='\n\n')
