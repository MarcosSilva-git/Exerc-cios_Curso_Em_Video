from datetime import date
nascimento = input('Digite sua data de nascimento: ').strip().split('/')
ano = date.today().year - int(nascimento[2])
if ano < 18:
    ano = 18 - ano
    print('Falta(m) {} ano(s) para você se apresentar no exército.'.format(ano))
elif ano == 18:
    print('Está na hora de se apresentar no exército.'.format(ano))
else:
    ano = ano - 18
    print('Vocẽ devia ter se alistado a {} anos atrás!!'.format(ano))

