maiores = idade = mulheresNovas = homens = 0
pessoa = 1
sexo = ''
while True:
    print('=-='*15)
    print(f'{pessoa:>18}ª PESSOA')
    print('=-='*15)
    idade = int(input('Informe a Idade: '))
    sexo = input('Iforme o sexo [F/M]: ').strip().upper()[0]
    while not (sexo in 'FfMm'):
        sexo = input('Informe o sexo [F/M]: ').strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheresNovas += 1
    x = ' '
    while not (x in 'SsNn'):
        x = input('Deseja cadastrar mais alguém [S/N]? ').strip().upper()[0]
    if x in 'Nn':
        break
    pessoa += 1
print('\033[31m')
print(f'No total, foram cadastradas {pessoa}.')
print(f'{maiores} são maiores de idade.')
print(f'{homens} são homens.')
print(f'{mulheresNovas} são mulheres que tem menos de 20 anos')

