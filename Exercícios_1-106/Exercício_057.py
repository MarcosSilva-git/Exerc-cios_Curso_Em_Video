genero = input('Digite o seu gênero [M/F]: ').strip().upper()[0]
while genero != 'M' and genero != 'F':
    genero = input('Digite um gênero válido [M/F]: ').strip().upper()[0]
if genero == 'M':
    print('Seu sexo é Masculino.')
else:
    print('Seu sexo é Feminino.')