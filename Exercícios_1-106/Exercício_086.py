coordenadas = list()
for i in range(0, 3):
    for s in range(0, 3):
        coordenadas.append(int(input(f'Digite um valor para [{i}, {s}]: ')))

print('-='*15)

cout = 1
for i in range(0, 9):
    print(f'[ {coordenadas[i]:^3} ]', end='')
    if cout == 3:
        print()
        cout = 1
        continue
    cout += 1