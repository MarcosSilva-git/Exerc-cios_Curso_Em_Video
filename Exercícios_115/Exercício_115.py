from Exercícios_115 import menu, registro
from time import sleep

print(rf'''
{'+' * 30}
{'Banco de Dados':^30}
{'+' * 30}
'''
      )

while True:
    opcao = menu.menu()

    if opcao == 1:
        opcao = registro.abrir_documento()
    elif opcao == 2:
        registro.registrar()

    sleep(1)

    if opcao == 3:
        print('Finalizando')
        sleep(1)
        break

print(f'\033[36;1m {"-" * 15} {" Volte Sempre! "} {"-" * 15} \033[m')