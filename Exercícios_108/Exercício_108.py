from Exercícios_108 import moeda

num = float(input('Digite um preço: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Adicionando 10% fica {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Retirando 13% fica {moeda.moeda(moeda.diminuindo(num, 13))}')
