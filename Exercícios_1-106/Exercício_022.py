nome = input('Digite o seu nome completo: ').strip()
nomeQtd = nome.split()

nomeMai = nome.upper()
print('Maíuculo: {}'.format(nomeMai))

nomeMin = nome.lower()
print('Minúsculo: {}'.format(nomeMin))

nomeQtdTotal = ''.join(nomeQtd)
nomeQtdTotal = len(nomeQtdTotal)
print('Quantidade de letras (Sem contar os espaços): {}'.format(nomeQtdTotal))

# Ou ...
'''
print('Quantidade de letras (Sem contar os espaços): {}'.format(len(nome) - nome.count(' ')))
'''

priNome = nomeQtd[0]
priNome = len(priNome)
print('Quantidade de letras no primeiro nome: {}'.format(priNome))