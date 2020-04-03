num = []
for pos in range(1, 6):
    num.append(int(input(f'Digite o valor da {pos}ª posição: ')))
menor = min(num)
maior = max(num)
print('-='*15)
print(f'Você digitou os valores: {num}')
print(f'O menor número digitado foi "{menor}" localizado nas posições:', end=' ')
for pos, valor in enumerate(num):
    if valor == menor:
        print(f'{pos + 1}... ', end='')
print(f'\nO maior número digitado foi "{maior}" localizado nas posiçõoes:', end=' ')
for pos, valor in enumerate(num):
    if valor == maior:
        print(f'{pos + 1}... ', end='')