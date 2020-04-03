media = 0
homem_mais_velho = '0'
mulheres_com_menos_de_20 = 0
idadeVelho = 0
for i in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(i)).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    genero = input('Digite o gênero da {}ª pessoa (M / F): '.format(i)).strip().upper()
    media += idade
    if genero == 'M' and idade > idadeVelho:
        homem_mais_velho = nome
        idadeVelho = idadeVelho
    if genero == 'F' and idade < 20:
        mulheres_com_menos_de_20 += 1
    print('-'*20)
print('A media de idade do grupo é de {} anos,'.format(media / 4))
print('O nome do homem mais velho é {},'.format(homem_mais_velho))
print('e há {} mulher(es) com menos de 20 anos.'.format(mulheres_com_menos_de_20))
