cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'azul': '\033[36m',
    'branco': '\033[1;30m',
    'roxo': '\033[1;35m'
}
produto = float(input('{1}Qual é o preço do produto?{0} '.format(cores['limpa'], cores['branco'])))
print('''Formas de pagamento:
{2}1{0} - {1}Dinheiro / Cheque{0}
{2}2{0} - {1}Débito{0}
{2}3{0} - {1}Cŕedito{0}'''.format(cores['limpa'], cores['azul'], cores['vermelho']))
pagamento = input('{1}Qual forma de pagamento prefere? {0}'.format(cores['limpa'], cores['branco']))
if pagamento == '1' or pagamento == 'Dinheiro' or pagamento == 'Cheque':
    desconto = produto / 10
    print('{2}O novo valor do produto é de {1}R${3}{0}'.format(cores['limpa'], cores['azul'], cores['branco'], produto - desconto))
    print('{1}Ele recebeu {2}R${3} {1}de desconto{0}'.format(cores['limpa'], cores['branco'], cores['azul'], desconto))
elif pagamento == '2' or pagamento == 'Débito':
    desconto = produto * 5 / 100
    print('{1}O novo valor do produto é de {2}R${3}{0}'.format(cores['limpa'], cores['branco'], cores['azul'],produto - desconto))
    print('{1}Ele recebeu {2}R${3} {1}de desconto{0}'.format(cores['limpa'], cores['branco'], cores['azul'],desconto))
elif pagamento == '3' or pagamento == 'Cŕedito':
    prestacao = int(input('{1}Em quantas vezes você quer pagar? {0}'.format(cores['limpa'], cores['branco'])))
    if prestacao <= 2:
        print('{1}O valor do produto é de {2}R${3}{0}'.format(cores['limpa'], cores['branco'], cores['roxo'], produto))
    else:
        juros = produto * 20 / 100
        print('{1}O novo valor do produto é de {2}R${3}{0}'.format(cores['limpa'], cores['branco'], cores['vermelho'], produto + juros))
        print('{1}Ele recebeu {2}R${3} {1}de jutos{0}'.format(cores['limpa'], cores['branco'], cores['vermelho'], juros))
