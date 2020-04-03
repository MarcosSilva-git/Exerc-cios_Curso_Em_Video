from datetime import date
M = 0
m = 0
for i in range(1, 8):
    ano = int(input('Digite o ano do Nascimento da {}ª pessoa: '.format(i)))
    hoje = date.today().year
    while hoje - ano < 0:
        ano = int(input('Digite uma data Válida: '))
    if hoje - ano >= 21:
        M += 1
    elif hoje - ano < 21:
        m += 1
print('''Das datas de nascimento enviadas,
{} são maiores de 21
{} são menores de 21'''.format(M, m))
