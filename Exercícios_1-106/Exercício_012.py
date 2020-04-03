produto = float(input('Digite o preço do produto: R$'))
produto = produto - (produto * (5 / 100))

print('O novo preço do produto é de {:.2f}'.format(produto))