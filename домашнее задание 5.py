# задание 5

# в этом варианте break останавливает цикл for
# введенные до дефиса числа прибавляет, но while продолжается

# def summ1():
#     s1 = 0
#     while True:
#         a = input(': ').split()
#         s = 0
#         for i in a:
#             if i == '-':
#                 break
#             else:
#                 i = int(i)
#                 s = s + i
#         s1 = s1 + s
#         print(s1)
# summ1()

# здесь ввод дефиса завершает программу, но предыдущие числа не прибавляет

# def summ1():
#     s1 = 0
#     while True:
#         a = input(': ').split()
#         s = 0
#         for i in a:
#             if i == '-':
#                 return
#             else:
#                 i = int(i)
#                 s = s + i
#         s1 = s1 + s
#         print(s1)
# summ1()