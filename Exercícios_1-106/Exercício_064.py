num = int(input('Digite um número para somar [999 para parar]: '))
s = 0
cont = 0
print('Caso deseja parar de somar, digite \033[31;1m"999"\033[m\n')
while num != 999:
    s += num
    num = int(input('Digite outro número:'))
    cont += 1
print(f'Você digitou {cont} números.')
print(f'E a soma desses números é {s}')