from datetime import date
dados = {}
dados['Nome'] = str(input('Seu nome: ')).strip()
ano_de_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
dados['Idade'] = ano_atual - ano_de_nascimento
dados['CNPJ'] = int(input('Seu CNPJ: '))
if dados['CNPJ'] != 0:
    dados['Salário'] = int(input('Seu salário: R$'))
    dados['Ano de Contratação'] = int(input('Qual fo o ano de contratação? '))
print('-'*15)
print(f'''Você, { dados["Nome"]},
Que possui {dados['Idade']} anos de idade,''')
if dados['CNPJ'] == 0:
    print('Não trabalha.')
else:
    print(f'Cujo salário é de R${dados["Salário"]:.2f},')
    print(f'Com o número do CNPJ {dados["CNPJ"]},')
    ano_de_aposentadoria = dados['Idade'] - (ano_atual - dados['Ano de Contratação']) + 35
    aposentadoria = dados['Ano de Contratação'] + 35
    print(f'Se aposentará com {aposentadoria} com {ano_de_aposentadoria} anos.')

