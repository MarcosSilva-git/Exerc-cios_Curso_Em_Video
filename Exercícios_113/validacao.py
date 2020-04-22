def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except (ValueError):
            print('\033[31mERROR. Digite um valor inteiro válido\033[m')
        except (KeyboardInterrupt):
            print('\033[31m\nO usuário preferiu não digitar esse número\033[m')
            num = 0
            break
    return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            break
        except (ValueError):
            print('\033[31mERROR. Digite um valor monetário válido\033[m')
        except (KeyboardInterrupt):
            print('\033[31m\nO usuário preferiu não digitar esse número\033[m')
            num = 0
            break
    return num
