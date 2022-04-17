
# задание 1

from sys import argv

path, a, b, c = argv
a, b, c, = map(float, argv[1:])
zp = lambda a, b, c: a * b + c
#
print(zp(a, b, c))
print(f'Заработная плата за текущий приод составила {zp(a, b, c)} рублей')