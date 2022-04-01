# задание 2

# этот вариант работает с готовым списком
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = len(li)
# print(len(li))
# print(li)
# a = 0
# b = 1
# while True:
#     if b == c or a == c:
#         break
#     li[a], li[b] = li[b], li[a]
#     # print(li)
#     a = a + 2
#     b = b + 2
# print(li)

# li = [1, 2, 'abc', 4, [5, 6], 7, 8, 9]
# c = len(li)
# print(len(li))
# print(li)
# a = 0
# b = 1
# while True:
#     if b == c or a == c:
#         break
#     li[a], li[b] = li[b], li[a]
#     # print(li)
#     a = a + 2
#     b = b + 2
# print(li)

# этот вариант работает с введением цифр или букв без пробелов и запятых
# l = input('Введите последовательность чисел: ')
# li = list(l)
# c = len(li)
# print(len(li))
# print(li)
# a = 0
# b = 1
# while True:
#     if b == c or a == c:
#         break
#     li[a], li[b] = li[b], li[a]
#     a = a + 2
#     b = b + 2
# print(li)

# этот вариант работает с цифрами и буквами с пробелами и запятыми и без них,
# но слова и числа разбивает на буквы и цифры

# l = input('Введите последовательность чисел: ')
# li = list(l)
# print(li)
# if ' ' or ',' in li:
#     while ' ' in li:
#         li.remove(' ')
#         print(li)
#
#     while ',' in li:
#         li.remove(',')
#         print(li)
# c = len(li)
# print(len(li))
# a = 0
# b = 1
# while True:
#     if b == c or a == c:
#         break
#     li[a], li[b] = li[b], li[a]
#     print(li)
#     a = a + 2
#     b = b + 2
# print(l)
# print(li)

# этот вариант работает с введением чисел или слов с пробелами, а запятые "приклеивает"
# к предыдущему слову или числу, без пробелов не работает

# l = input('Введите последовательность чисел: ').split()
# print(l)
# print(type(l))
# li = list(l)
# c = len(li)
# print(len(li))
# a = 0
# b = 1
# while True:
#     if b == c or a == c:
#         break
#     li[a], li[b] = li[b], li[a]
#     print(li)
#     a = a + 2
#     # print(a)
#     b = b + 2