from time import sleep
print('Digite números a ser somados')
print('Caso deseje parar de executar o programa, Digite \033[31;1m"Stop"\033[m.')
num = 1
s = 0
cont = 0
menor = 0
maior = 0
x = ''
while x != 'N':
    while num != 'STOP':
        num = input('Digite um número: ')
        if num.isnumeric():
            num = int(num)
            if cont == 0:
                maior = num
                menor = num
            if num > maior:
                maior = num
            if num < menor:
                menor = num
            s += num
            cont += 1
        elif num.isalpha():
            num = num.strip().upper()
            while num != 'STOP' and not (num.isnumeric()):
                num = input('Digite um valor VÁLIDO: ')
        else:
            num = input('Digite um valor VÁLIDO: ')

    print('A média de todos os valores digitados é {},'.format(s / cont))
    print('O menor número digitado foi {},'.format(menor))
    print('E o maior número digitado foi {}.'.format(maior))
    print(f'E, ao todo, foram digitados {cont} valores.')
    x = input('Deseja continuar incluindo valores? [S/N]').upper()
    while x != 'N' and x != 'S':
        x = input('Deseja continuar incluindo valores? [S/N]').upper()
    if x == 'S':
        num = '0'
print('Finalizando...')
sleep(1)
print('O programa acabou!')
