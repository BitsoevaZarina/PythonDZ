# задание 2

'''
   Персональные данные где,
   n: Имя n2: Фамилия y: год рождения
   c: город проживания e: email
   num: номер телефона
'''
print('Заполните:')
n = input('Имя: ')
n2 = (input('Фамилия: '))
y = (input('Год рождения: '))
c = (input('Город проживания: '))
e = (input('email: '))
num = (input('телефон: '))

def per(n, n2, y, c, e, num):
    print(f'{n.title()} {n2.title()} {y} {c.title()} {e.lower()} {num}')
per(n,n2,y,c,e,num)