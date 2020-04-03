coordenadas = []
for i in range(0, 3):
    for n in range(0, 3):
        coordenadas.append(int(input(f'Digite um valor para [{i}, {n}]: ')))
print('-='*15)
cout = 1
somaPar = terceiraColum = segMaior = 0
for i in range(0, 9):
    print(f'[ {coordenadas[i]} ]', end='')
    if coordenadas[i] % 2 == 0:
        somaPar += coordenadas[i]
    if 2 < i < 6:
        if i == 3 or coordenadas[i] > segMaior:
            segMaior = coordenadas[i]
    if cout == 3:
        print()
        terceiraColum += coordenadas[i]
        cout = 0
    cout += 1
print('-='*15)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceora colunca é {terceiraColum}')
print(f'E o maior valor da segunda coluna é {segMaior}')
