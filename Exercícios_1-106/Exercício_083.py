expressao = []
testando = list()
x = input('Digite uma expressão matemática: ')
for valor in x:
    if valor in '()':
        expressao.append(valor)
for i in expressao:
    if i in '(':
        testando.append(i)
    elif i in ')':
        if len(testando) > 0:
            testando.pop()
        else:
            testando.append(i)
            break
if len(testando) > 0:
    print('A expressão é inválida')
else:
    print('A expressão é válida')
