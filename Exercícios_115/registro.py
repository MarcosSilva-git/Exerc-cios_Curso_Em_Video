def abrir_documento():
    documento = ler_documento()
    if documento == 'não existe':
        print("\033[35mNão há ninguém registrado no momento\033[m")
    elif documento == 3:
        documento.close()
        return documento
    else:
        print('-'*26)
        print(f'{"pessoas.txt":^26}')
        print('-'*26)
        print(documento.read())
        print('\033[35mOperação Realizada com Sucesso!\033[m')

def registrar():
    documento = ler_documento('a')

    while True:
        try:
            nome = str(input("Nome: ")).strip()
        except KeyboardInterrupt:
            documento.close()
            return 3

        if nome.isalpha():
            nome.capitalize()
            break
        else:
            if nome.isspace():
                print('\033[31mError. Digite um valor.\033[m')
            else:
                print('\033[31mError. Digite somente números.\033[m')

    while True:

        try:
            idade = int(input('Idade: '))
            break
        except (TypeError, ValueError):
            print('\033[31mError. Digite um número\033[m')
        except KeyboardInterrupt:
            documento.close()
            return 3

    if documento == 'não existe':
        ler_documento('x')

    documento.write(f"{nome:<15}{idade} anos \n")


def ler_documento(mode = 'r'):

    try:
        documento = open('pessoas.txt', mode=mode)
        return documento

    except (FileNotFoundError):
        return 'não existe'

    except KeyboardInterrupt:
        return 3

