import emoji

algo = input('Digite algo: ')

print('o tipo primitivo desse valor é {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em maiúsculo? {}'.format(algo.isupper()))
print('Está em minúsculo? {}'.format(algo.islower()))
print('Quantos caracteres tem esse valor? {}'.format(len(algo)))
print('Está capitalizado? {}'.format(algo.istitle()))
