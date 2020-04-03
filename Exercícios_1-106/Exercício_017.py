from math import hypot
catetoOposto = float(input('Digiite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(hipotenusa))
