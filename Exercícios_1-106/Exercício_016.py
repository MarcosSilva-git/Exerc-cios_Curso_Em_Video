'''
Não use a função floor!!
Ao arredondar um número negativo com essa função
o programa não funcioará direito
Neste exercício, use trunc!!
'''
from math import trunc
num = float(input('Digite um número real: '))
inteira = trunc(num)
print('O número {} tem a parte inteira {}.'.format(num, inteira))
