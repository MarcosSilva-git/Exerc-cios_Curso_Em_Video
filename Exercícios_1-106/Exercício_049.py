num = int(input('Você quer saber a tabuada de qual número? '))
tab = int(input('Até qual número você quer multiplicar? '))
for i in range(1, tab + 1):
    print('{} X {:2} = {}'.format(num, i, num*i))
