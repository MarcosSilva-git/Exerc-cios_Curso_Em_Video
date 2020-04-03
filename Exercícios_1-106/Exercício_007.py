nota1 = float(input('Digite a nota do 1º semestre: '))
nota2 = float(input('Digite a nota do 2º semestre:  '))

notaTotal = nota1 + nota2
media = notaTotal / 2

print('A nota acumulada do aluno foi {}'.format(notaTotal))
print('E sua média foi {:.1f}'.format(media))