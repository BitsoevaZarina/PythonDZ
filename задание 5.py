# задание 5
# 1 вариант

# list = [7, 5, 3, 3, 2]
# print(list)
# a = int(input('цифра: '))
# if a > 7:
#     list.insert(0, a)
# if a == 7 or a == 6:
#     list.insert(1, a)
# if a == 5 or a == 4:
#     list.insert(2, a)
# if a == 3:
#     list.insert(-2, a)
# if a <= 2:
#     list.append(a)
# print(list)

# 2-ой вариант
# работает с элементами списка(7, 5, 3, 2)
# находит элемент, смотрит индекс, считает сколько подобных в списке
# и вставляет после них

# li = [7, 5, 3, 3, 2]
# print(li)
# a = int(input('число: '))
# a1 = li.index(a)
# a2 = li.count(a)
# c = a1 + a2
# li.insert(c, a)
# print(li)
