largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura
tintaNecessaria = area / 2

print('A área da parede é de {}m² quadrados'.format(area))
print('Será necessário de {}l de tinta para pintar'.format(tintaNecessaria))
