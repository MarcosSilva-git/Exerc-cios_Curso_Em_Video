nome = input('Informe-nos seu nome completo: ').strip().split()
primeiroNome = nome[0]
ultimoNome = nome[len(nome) - 1]
print('Primeiro nome: {}'.format(primeiroNome))
print('Último nome: {}'.format(ultimoNome))
