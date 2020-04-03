from time import sleep
produto = 1
cont = total = preço = maisBarato = maisBaratoNome = maisCaro = 0
continuar = '0'
while True:
    print('=-='*15)
    print(f'{produto:>17}º Produto')
    print('=-='*15)
    nome = input('Digite o nome do produto: ').strip().capitalize()
    preço = float(input('Qual é o preço do produto? '))
    total += preço
    if produto == 1 or preço < maisBarato:
        maisBarato = preço
        maisBaratoNome = nome
    if preço > 1000:
        maisCaro += 1
    print('=-='*15)
    while not (continuar in 'SsNn'):
        continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    print('=-='*15)
    if continuar in 'Nn':
        break
    continuar = '0'
    produto += 1
    sleep(0.5)
print('Calculando o total...')
sleep(2)
print(f'''O total da compra foi de R${total:.2f}.
{maisCaro:.2f} produtos custam mais de R$1000 e,
O nome do produto mais barato é {maisBaratoNome},
Ele custa R${maisBarato:.2f}.''')

