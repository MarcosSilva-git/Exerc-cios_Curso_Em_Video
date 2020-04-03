from random import randint
from time import sleep
from operator import itemgetter
Jogo = {}
print(f'{"Valores Sorteados":-^30}')
for i in range(1, 5):
    valor = randint(1, 6)
    Jogo[f'jogador{i}'] = valor
    print(f'O jogador{i} tirou {valor} no dado')
    sleep(0.5)
ranking = sorted(Jogo.items(), key=itemgetter(1), reverse=True)
print('<<< Ranking >>> ')
for i, v in enumerate(ranking):
    print(f'  - {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
