from Exercícios_109 import moeda

num = float(input('Digite um preço: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, "U$")}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'Adicionando 10% fica {moeda.aumentar(num, 10, True)}')
print(f'Retirando 13% fica {moeda.diminuindo(num, 13, True)}')
