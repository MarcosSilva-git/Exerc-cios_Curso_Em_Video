v = int(input('Informe a velocidade do carro: '))
if v > 80:
    print('Você está a {:.2f}K/h numa rua de 80K/h.'.format(v))
    v = (v - 80) * 7
    print('Por isso você foi multado em R${:.2f}'.format(v))
else:
    print('Você está dentro do limite de velocidade: ')
