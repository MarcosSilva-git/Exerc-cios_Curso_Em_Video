distancia = int(input('Qual é a distância de viagem?: '))
if distancia <= 200:
    valor = distancia * 0.5
    print('O valor da viagem será de {} Reais.'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da viagem será de {} Reais.'.format(valor))
