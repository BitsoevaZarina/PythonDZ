
# задание 4

old = [1, 2, 2, 33, 5, 65, 65, 7, 8, 8, 8, 10, 101]

new = [i for i in old if old.count(i) == 1]
print(new)