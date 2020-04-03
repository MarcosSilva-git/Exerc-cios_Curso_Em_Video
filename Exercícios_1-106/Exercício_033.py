num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digiite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num1 >= num2 and num1 >= num3:
    maior = num1
if num2 >= num1 and num2 >= num3:
    maior = num2
if num3 >= num1 and num3 >= num2:
    maior = num3
if num1 <= num2 and num1 <= num3:
    menor = num1
if num2 <= num1 and num2 <= num3:
    menor = num2
if num3 <= num1 and num3 <= num2:
    menor = num3
print('O menor é {} e o maior é {}'.format(menor, maior))