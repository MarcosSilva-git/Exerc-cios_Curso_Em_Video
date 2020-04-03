dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valorDias = dias * 60
valorKm = km * 0.15
total = valorDias + valorKm

print('O total a pagar é de R${:.2f}'.format(total))

