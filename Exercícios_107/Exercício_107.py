from Exercício_107 import moeda

num = float(input('Digite um preço: R$'))
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'Adicionando 10% fica R${moeda.aumentar(num, 10)}')
print(f'Retirando 13% fica R${moeda.diminuindo(num, 13)}')
