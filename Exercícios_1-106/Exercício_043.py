peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * 2)
if imc < 18.5:
    print('{}Você está abaixo do peso'.format('\033[1;35m'))
elif imc < 25:
    print('{}Você está no seu peso ideal'.format('\033[1;32m'))
elif imc < 30:
    print('Você está com {}sobrepeso'.format('\033[1;33m'))
elif imc < 40:
    print('Você está {}obeso(a)'.format('\033[31m'))
else:
    print('Você tem {}Obesidade Mórbida'.format('\033[1;31m'))
