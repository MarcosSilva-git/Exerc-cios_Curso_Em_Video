num = list()
cont = 0
while True:
    num.append(int(input('Digite um número: ')))
    x = str(input('Deseja continuar? [S/N]  ')).strip().upper()[0]
    while not (x in 'SN'):
        x = str(input('Tente novamente. Deseja continuar? [S/N]  ')).strip().upper()[0]
    cont += 1
    if x in 'N':
        break
print('-='*15)
print(f'Foram digitados {cont} números.')
num.sort(reverse=True)
print(num)
if num.count(5) == 0:
    print('O valor 5 não foi encontrado na lista')
else:
    print('O valor 5 foi digitado nessa lista')
