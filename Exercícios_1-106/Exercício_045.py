import emoji
from random import choice
from time import sleep
cores = {
    'limpa': '\033[m',
    'branco': '\033[1;30m',
    'vermelho': '\033[31m',
    'verde': '\033[1;32m',
    'azul': '\033[36m',
    'roxo': '\033[1;35m'
}
print('{}=-='.format(cores['branco'])*12)
print('           VAMOS JOGAR!')
print('{}=-={}'.format(cores['branco'], cores
['limpa'])*12)
print(emoji.emojize('{0}1{1} {3}para{1} {2}pedra{1} :punch:'.format(cores['verde'],cores['limpa'], cores['roxo'], cores['branco']), use_aliases=True))
print(emoji.emojize('{0}2{1} {3}para{1} {2}papel{1} :raised_hand:'.format(cores['verde'], cores['limpa'], cores['roxo'], cores['branco']), use_aliases=True))
print(emoji.emojize('{0}3{1} {3}para{1} {2}tesoura{1} :v:'.format(cores['verde'], cores['limpa'], cores['roxo'], cores['branco']), use_aliases=True))
jogador = int(input('{0}Qual você quer escolher? {1}'.format(cores['branco'], cores['limpa'])))
computador = choice(['pedra', 'papel', 'tesoura'])
if jogador == 1:
    jogador = 'pedra'
elif jogador == 2:
    jogador = 'papel'
else:
    jogador = 'tesoura'
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('{}Jogada do Computador - {}{}{}'.format(cores['azul'], cores['roxo'], computador, cores['limpa']))
print('{}Sua jogada - {}{}{}'.format(cores['azul'], cores['roxo'], jogador, cores['limpa']))
if jogador == computador:
    print('{}UAU! {}EMPATOU{}!!'.format(cores['branco'], cores['azul'], cores['limpa']))
elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
    print('{}PARABÈNS!! Você venceu!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}GANHEI! Tente de novo na proxima{}'.format(cores['vermelho'], cores['limpa']))
