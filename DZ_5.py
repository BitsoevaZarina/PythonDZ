
# задание 5

from functools import reduce

li = [i for i in range(100, 1001) if i % 2 == 0]

def ogo(a, b):
    return a * b
print(reduce(ogo, li))

#
# # или
#
ogo = lambda a, b: a * b
print(reduce(ogo, li))

# у меня что-то странное получилось(