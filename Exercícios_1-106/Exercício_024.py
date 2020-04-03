city = input('Digite o nome de uma cidade: ').upper().strip()
city = city.split()
city = city[0]
if city == 'SANTO':
    print('A cidade informada começa com a palavra "Santo"')
else:
    print('A cidade informada não começa com a palavra "Santo"')
