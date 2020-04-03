def leiaint(msg=''):
    while True:
        num = input(f'>>{msg}')
        if not (num.isnumeric()):
            print('\033[31;1mERROR. Digite um valor inteiro válido\033[m')
        else:
            return int(num)


x = leiaint('Digite um número: ')
print(f'O número digita foi {x}')
