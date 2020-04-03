nome = input('Informe o seu nome completo: ').strip()
nome = nome.title()
nome = 'Silva' in nome
if nome:
    print('Seu nome tem "Silva"')
else:
    print('Seu nome não tem Silva')
