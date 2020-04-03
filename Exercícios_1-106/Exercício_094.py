pessoas = []
dadosPessoais = {}
media = 0
cont = 1

while True:
    dadosPessoais['Nome'] = str(input('Nome: ')).strip()
    dadosPessoais['Idade'] = int(input('Idade: '))
    media += dadosPessoais['Idade']
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]

    while not (sexo in 'FM'):
        print('Valor ínválido.')
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]

    dadosPessoais['Sexo'] = sexo
    pessoas.append(dadosPessoais.copy())
    condicao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    while not (condicao in 'SN'):
        print('Valor ínválido.')
        condicao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if condicao == 'N':
        break

    cont += 1
    print('='*15)

print('-='*30)
print(f'Foram cadastradas {cont} pessoas')
media //= cont
print(f'A média de idade do grupo foi de {media} anos')
print('As mulheres cadastradas foram: ',end='')

for valor in pessoas:
    if valor['Sexo'] == 'F':
        print(valor['Nome'], end=' ')

print()
print(f'As pessoas cuja idade está acima da média são: ', end='')

for valor in pessoas:
    if valor['Idade'] > media:
        print(valor['Nome'], end=' ')
