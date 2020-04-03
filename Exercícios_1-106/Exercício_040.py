nota1 = int(input('Digite a nota do primeiro semestre: '))
nota2 = int(input('Digite a nota do segundo semestre: '))
média = (nota1 + nota2) / 2
if média < 5:
    print('Você está {}REPROVADO{}'.format('\033[1;31m', '\033[m'))
    print('Tente mais uma vez ano que vem')
    print('Sua média foi de {:.1f}'.format(média))
elif média == 5:
    print('Você está em {}RECUPERAÇÂO{}'.format('\033[1;33m', '\033[m'))
    print('Você ainda pode passar!')
    print('Sua média foi de {:.1f}'.format(média))
else:
    print('Você foi {}APROVADO{}'.format('\033[1;36m', '\033[m'))
    print('Você foi um bom aluno esse ano')
    print('Sua média foi de {:.1f}'.format(média))