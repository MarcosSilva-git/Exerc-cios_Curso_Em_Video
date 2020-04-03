s = 0
num = 0
for i in range(3, 500, 3):
    if i % 2 != 0:
        s += i
        num += 1
print('A soma dos {} valores é {}'.format(num, s))
