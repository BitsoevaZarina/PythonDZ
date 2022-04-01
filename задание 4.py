# задание 4

# вариант 1
# print('Введите слова через пробел.')
# while True:
#     a = input('Ввод: ')
#     a1 = a.split()
#     count = 0
#     if 'stop' in a1:
#         break
#     for el in a1:
#         count = count + 1
#         if len(el) > 10:
#             print(count, el[0:10])
#         else:
#             print(count, el)
# print('The end')

# вариант 2

# print('Введите слова через пробел.')
# while True:
#     a = input('Ввод: ')
#     a1 = a.split()
#     if 'stop' in a1:
#         break
#     for el, word in enumerate(a1, 1):
#         print(el, word[0:10])
# print('The end')
