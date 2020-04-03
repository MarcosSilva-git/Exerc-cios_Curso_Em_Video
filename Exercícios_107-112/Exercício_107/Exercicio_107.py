import moeda

num = int(input('Digite um preço: R$'))
print('-='*20)
print(f'O dobro de R${num} é R${moeda.dobro(num):.2f}')
print(f'A metade de R${num} é R${moeda.metade(num):.2f}')
print(f'Aumentando 10%, temos: R${moeda.aumentar(num, 10):.2f}')
print(f'Aumentando 13%, temos: R${moeda.diminuir(num, 13):.2f}')

