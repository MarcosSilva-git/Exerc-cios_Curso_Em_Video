salário = float(input('Digite o seu salário: '))
print('VocẼ ganhou um aumento!!')
if salário > 1250:
    salário = ((salário / 100) * 10) + salário
    print('Seu novo salário é de R${}.'.format(salário))
else:
    salário = ((salário / 100) * 15) + salário
    print('Seu novo salário é de R${}.'.format(salário))