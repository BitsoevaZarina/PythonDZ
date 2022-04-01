# задание 1

list = [10, ('a', 'b'), 40, 'can', [3, 15]]
print(list)
count = 0
for element in list:
    count = count + 1
    print(count, '.', element, '-', type(element))
