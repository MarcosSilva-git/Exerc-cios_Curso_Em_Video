def leiaDinheiro(n=''):
    while True:
        n = str(n).strip()
        if n.isspace():
            print('\033[31;1mERROR. Você digitou espaços.\033[m')
        elif n.isalpha():
            print('\033[31;1mERROR. Você digitou'
                  ' letras e não números\033[m')


print(leiaDinheiro('l'))
