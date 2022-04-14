# задание 4

def my_func(a, b):
    res = a ** b
    print(res)
    res2 = round(res, 3)
    print(res2)
my_func(3, -3)

def my_func(a,b):
    a1 = 1
    b = abs(b)
    while b > 0:
        a1 = a1 * a
        b = b - 1
    a1 = 1 / a1
    a1 = round(a1, 3)
    print(a1)

my_func(3, -3)
