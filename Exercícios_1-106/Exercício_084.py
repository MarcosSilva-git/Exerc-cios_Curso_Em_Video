# Curso em Vídeo de python 3 #084 simplifica esse script

cadastro = []
peso = [[], []]
cont = 1

while True:
    print('-='*15)
    print(f'{cont:>11}ª PESSOA')
    print('-='*15)
    dados = [input('Nome: '), float(input('Peso: '))]
    cadastro.append(dados[:])
    dados.clear()
    condicao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while condicao not in 'SN':
        print('Desculpe, não entendi...')
        condicao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if condicao == 'N':
        break
    cont += 1


print(f'Foram cadastradas {len(cadastro)} pessoas')


for indice, valor in enumerate(cadastro):
    if indice == 0:
        peso[0].append(valor)
        peso[1].append(valor)
    elif valor[1] == peso[0][0][1] and valor[1] == peso[1][0][1]:
        peso[0].insert(0, valor)
        peso[1].insert(0, valor)

    elif valor[1] < peso[0][0][1]:
        peso[0].clear()
        peso[0].append(valor)
    elif valor[1] == peso[0][0][1]:
        peso[0].append(valor)

    elif valor[1] > peso[1][0][1]:
        peso[1].clear()
        peso[1].append(valor)
    elif valor[1] == peso[1][0][1]:
        peso[1].append(valor)


print(f'O menor peso registrado foi {peso[0][0][1]}KG. Peso de', end=' ')


for i in range(0, len(peso[0])):
    if i == len(peso[0]) - 2:
        print(peso[0][i][0], end=' e ')
    elif i == len(peso[0]) - 1:
        print(peso[0][i][0], end='\n')
    else:
        print(peso[0][i][0], end=', ')


print(f'O maior peso registrado foi {peso[1][0][1]}KG Peso de', end=' ')

for i in range(0, len(peso[1])):
    if i == len(peso[1]) - 2:
        print(peso[1][i][0], end=' e ')
    elif i == len(peso[1]) - 1:
        print(peso[1][i][0], end='\n')
    else:
        print(peso[1][i][0], end=', ')
