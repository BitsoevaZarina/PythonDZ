
# задание 2

old = [1, 2, 2, 33, 5, 65, 65, 7, 8, 8, 8, 10, 101]
new = [old[i] for i in range(len(old)) if old[i] > old[i - 1]]
print(new)