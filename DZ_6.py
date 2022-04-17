
# задание 6

from itertools import count, cycle
for i in count(10):
    if i > 37:
        break
    else:
        print(i)
#
li = [12, 21, 24, 32, 14, 55, 42]
i = 0
for el in cycle(li):
    i = i + 1
    if i > 5:
        break
    print(el)

# не успела: седьмая на уровне "показывать стыдно",
# в шестую можно было добавить диалог с пользователем
# ((