lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    x = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while not (x in 'SN'):
        x = str(input('Não entendi. Deseja continuar? [S?N]')).strip().upper()[0]
    if x in 'N':
        break
pares = list()
impares = list()
for pos, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(lista[pos])
    else:
        impares.append(lista[pos])
print('-='*15)
print(f'Os valores digitados foram: {lista}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')