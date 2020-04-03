from math import cos, tan, sin, radians
angulo = int(input('Digite um ângulo: '))
radiano = radians(angulo)
seno = sin(radiano)
coss = cos(radiano)
tang = tan(radiano)
print('O ângulo {}° tem como seno {:.2f}°, cosseno de {:.2f}° e tangente de {:.2f}°.'.format(angulo, seno, coss, tang))
