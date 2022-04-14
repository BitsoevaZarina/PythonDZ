# задание 3

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
def summ(a, b, c):
    if a < b and a < c:
        d = b + c
    elif b < a and b < c:
        d = a + c
    elif c < a and c < b:
        d = a + b
    print(d)
summ(a, b, c)