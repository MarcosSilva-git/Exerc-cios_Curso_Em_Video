aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: ')).strip()
aluno['Média'] = float(input('Média do aluno: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-'*30)
print(f'O nome do(a) aluno(a) é {aluno["Nome"]}')
print(f'A média dele(a) é {aluno["Média"]}')
print(f'A situação dele(a) é {aluno["Situação"]}')