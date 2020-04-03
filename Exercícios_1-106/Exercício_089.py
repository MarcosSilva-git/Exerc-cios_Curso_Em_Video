from time import sleep
alunos = []
dados = []
while True:
    # Cadastro de alunos e notas deles
    dados.append(str(input('Nome do aluno: ')).strip())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()

    # Continuar ou para de cadastrar alunos
    condicao = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    while not(condicao in 'SN'):
        print('Não Entendi...')
        condicao = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if condicao == 'N':
        break

print(f'{"BOLETIM":=^36}')
print(f'{"Nº"}    {"Aluno"} {"MÉDIA":>23}')
for i, valor in enumerate(alunos):
    print(i, end='     ')
    print(f'{valor[0]:<25}', end='')
    media = (valor[1] + valor[2]) / 2
    print(f'{media:>5.2f}')
print('='*36)

while True:
    x = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if x == 999:
        break
    else:
        print(f'Notas de {alunos[x][0]} são ', end='')
        print(alunos[x][1:])
    print('='*36)
print('Finalizando...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')