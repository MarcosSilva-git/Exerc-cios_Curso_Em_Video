from time import sleep
lista_de_jogadores = []
jogador = dict()
partidas = list()
gols = 0

while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    jogador['Partidas Jogadas'] = int(input('Quantidade de partidas jogadas: '))
    for i in range(1, jogador['Partidas Jogadas'] + 1):
        partidas.append(int(input(f'QTD de gols feitos na {i}ª partida: ')))
        gols += partidas[-1]
    jogador['Gols'] = gols
    condicao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    while not (condicao in 'SN'):
        print('Opção inválida.')
        condicao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    print('-'*20)
    gols = 0
    jogador['Gols Por Partida'] = partidas[:]
    partidas.clear()
    lista_de_jogadores.append(jogador.copy())

    if condicao == 'N':
        break

print('-='*15)
print(f'{"ID":<4}{"NOME":<20}{"Gols"}')
print('-='*15)

for i, valor in enumerate(lista_de_jogadores):
    print(i, end='  ')
    print(f'{valor["Nome"]:<23}', end='')
    print(f'{valor["Gols"]:>2}')
print('-='*15)

while True:
    exibir = int(input('Mostrar dados de qual jogador? (nº de ID e 999 para parar): '))

    if exibir == 999:
        print('Finalizando...')
        break

    if exibir >= len(lista_de_jogadores) or exibir < 0:
        print(f'EROOR. Não existe jogador com código {exibir}')

    else:
        print(f'<<<  Mostrando dados de {lista_de_jogadores[exibir]["Nome"]}  >>>')
        for i, gols in enumerate(lista_de_jogadores[exibir]['Gols Por Partida']):
            print(f'    => Na {i + 1}ª partida, fez {gols} gols.')
        print(f'Foi um total de {lista_de_jogadores[exibir]["Gols"]} gols!')

    print('-='*15)

sleep(1)
print('<< VOLTE SEMPRE >>')