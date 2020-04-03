from random import randint
vitorias = soma = cont = jogadorEscolhe = 0

print('Vamos JOGAR?!')
print('Eu te desafio a jogar \"PAR OU ÍMPAR\" comigo')
while True:
    while not (0 < jogadorEscolhe < 3):
        print('Faça a sua escolha:')
        print('[ 1 ] - Par')
        print('[ 2 ] - Ímpar')
        jogadorEscolhe = int(input('Qual você quer? '))

    jogadaUsuario = int(input('Digite um valor: '))
    print('=-='*15)
    jogadaComputador = randint(0, 10)
    soma = jogadaComputador + jogadaUsuario

    if (jogadorEscolhe == 1 and soma % 2 == 0) or (jogadorEscolhe == 2 and soma % 2 != 0) :
        resultado = 'Par'
        ganhador = 'Você GANHOU!'
        print(f'Você jogou {jogadaUsuario} e o computador jogo {jogadaComputador}.')
        print(f'{jogadaUsuario} + {jogadaComputador} = {soma} -->> {resultado} ')
        print('=-='*15)
        print(ganhador)
        print('Vamos jogar novamente...')
        print('=-='*15)
    else:
        resultado = 'Ímpar'
        ganhador = 'Você PERDEU!'
        print(f'Você jogou {jogadaUsuario} e o computador jogo {jogadaComputador}.')
        print(f'{jogadaUsuario} + {jogadaComputador} = {soma} -->> {resultado} ')
        print(('=-='*15))
        print(ganhador)
        print(('=-='*15))
        break
    jogadorEscolhe = 0
    cont += 1
print(f'GAME OVER! Você venceu {cont} vezes.')