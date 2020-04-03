def valor(i):
    x = int(input(f'Digite o {i}º valor: '))
    return x


tupla = (valor(1), valor(2), valor(3), valor(4))
par = []
print(f'Você digitou os valores {tupla}')
if tupla.count(9) == 0:
    print('O número 9 não foi digitado')
elif tupla.count(9) == 1:
    print(f'O valor 9 apareceu {tupla.count(9) } vez')
else:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) == 0:
    print('O valor 3 não foi digitado nenhuma vez')
else:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
for i in range(0, 4):
    if tupla[i] % 2 == 0:
        par.append(tupla[i])
if len(par) == 0:
    print('Não foi digitado um único valor par')
elif len(par) == 1:
    print(f'O valor par digitado foi {par[0]}')
else:
    print('Os valores pares digitados foram: ', end='')
    for i in range(0, len(par)):
        print(f'{par[i]} ', end='')
