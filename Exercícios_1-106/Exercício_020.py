from random import sample
aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
sorteio = sample([aluno4, aluno3, aluno2, aluno1], k=4)
print('A ordem das apresentações é:')
print('1º - {}\n2º - {}\n3º - {}\n4º - {}'.format(sorteio[0], sorteio[1], sorteio[2], sorteio[3]))