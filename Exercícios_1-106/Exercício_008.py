metros = float(input('Digite um valor em metros: '))
kilometros = metros / 1000
hequitometros = metros / 100
decametros = metros / 10
decimetros = int(metros * 10)
centimetros = int(metros * 100)
milimetros = int(centimetros * 100)

print('A medida de {}m corresponde a'.format(metros))
print('{:.3f}Km\n{:.2f}hm\n{:.1f}dam\n{}dm\n{}cm\n{}mm'.format(kilometros, hequitometros, decametros, decimetros, centimetros, milimetros))
