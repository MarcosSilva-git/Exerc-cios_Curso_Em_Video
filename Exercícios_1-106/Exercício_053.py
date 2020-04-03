n = input('Digite uma frase: ').strip()
x = ''.join(n.split()).upper()
frase = x[::-1]
if frase == x:
    print('A frase "{}" é um Palíndromo.'.format(n))
else:
    print('A frase "{}" NÂO é um Palíndromo.'.format(n))
