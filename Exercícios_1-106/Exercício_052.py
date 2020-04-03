# A aula 52 do curso em vídeo de python tem mais detalhes.

# ========================================================

num = int(input('Digite um número: '))
valor = 'primo'
for i in range(2, num):
    n = num % i
    if n == 0:
        valor = 'não primo'
if 1 == num or num == 0:
    valor = 'não primo'
if valor == 'primo':
    print('O número {} é um número primo.'.format(num))
else:
    print('O número {} não é um número primo.'.format(num))
