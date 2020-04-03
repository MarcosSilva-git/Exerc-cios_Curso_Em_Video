num = []
for i in range(0, 5):
    x = int(input('Digite um número: '))
    if len(num) == 0 or num[-1] < x:
        num.append(x)
        print('Adicionado ao final da lista.')
    for pos, valor in enumerate(num):
        if valor > x:
            num.insert(pos, x)
            print(f'Adicionado na posição {pos} da lista.')
            break
print(num)
