from Exercícios_107 import moeda

num = float(input('Digite um preço: R$'))
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'Adicionando 10% fica {moeda.aumentar(num, 10)}')
print(f'Retirando 13% fica {moeda.diminuindo(num, 13)}')
