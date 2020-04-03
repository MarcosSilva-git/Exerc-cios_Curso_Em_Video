idade = int(input('Informe-nos a sua idade: '))
if idade <= 9:
    print('Sua categoria é {}MIRIM'.format('\033[34m'))
elif idade <= 14:
    print('Sua categoria é {}INFANTIL'.format('\033[34m'))
elif idade <= 19:
    print('Sua categoria é {}JÚNIOR'.format('\033[34m'))
elif idade <= 20:
    print('Sua categoria é {}SÊNIOR'.format('\033[34m'))
else:
    print('Sua categoria é {}MASTER'.format('\033[34m'))
print('{}Boa Competição!'.format('\033[m'))
