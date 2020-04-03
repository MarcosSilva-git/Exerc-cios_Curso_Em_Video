jogador = dict()
partidas = list()
gols = 0
jogador['Nome'] = str(input('Nome do jogador: ')).strip()
jogador['Partidas Jogadas'] = int(input('Quantidade de partidas jogadas: '))

for i in range(1, jogador['Partidas Jogadas'] + 1):
    partidas.append(int(input(f'QTD de gols feitos na {i}ª partida: ')))
    gols += partidas[-1]

jogador['Gols'] = gols
del gols
jogador['Gols Por Partida'] = partidas
del partidas
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas Jogadas"]} partidas.'
      f'')

for i, gols in enumerate(jogador['Gols Por Partida']):
    print(f'    => Na {i + 1}ª partida, fez {gols} gols.')
print(f'Foi um total de {jogador["Gols"]} gols!')
