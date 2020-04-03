from time import sleep
from emoji import emojize
print('Os fogos estorarão em:')
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('0')
print(emojize('{}BOOMMM!! :collision:'.format('\033[1;31m'), use_aliases=True))