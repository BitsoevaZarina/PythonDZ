# задание 1

print('Разделить а на b.')
num1 = int(input('a: '))
num2 = int(input('b: '))
def div(num1, num2):
    try:
        res = num1 / num2
        print(res)
        return res
    except ZeroDivisionError:
        print('Делить на ноль нельзя.')
div(num1, num2)

# вариант 2

# здесь создаем функцию, затем ее используем
# def div(num1, num2):
#     try:
#         res = num1 / num2
#         print(res)
#         return res
#     except ZeroDivisionError:
#         print('Делить на ноль нельзя.')
#
# # а) с вводом с клавиатуры
#
# print('Разделить a на b')
# while True:
#     a = input('a: ')
#     if a == '-':
#         break
#     else:
#         a1 = int(a)
#         b = int(input('b: '))
#
#     div(a1, b)
#
# # в) передаем параметры через вызов функции
# # и видим результат на экране
#
# div(87, 0)

# вариант 3

# try:
#     a = lambda a, b: a / b
# except ZeroDivisionError:
#     print("Делить на ноль нельзя")
# print(round(a(4, 9), 3))