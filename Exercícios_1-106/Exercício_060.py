# A aula do Curso em Vídeo de Python, Exercício 60, tem mais funcionalidades!

num = int(input('Digite um número para calcular o fatoial: '))
n = num
fat = 1
while n > 1:
    fat *= n
    n -= 1
print('O fatorial de {} é igual a {}'.format(num, fat))
