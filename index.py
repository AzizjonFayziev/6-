# age = int(input('Enter your age: '))

# if 18 <= age <=50: print('Welcome!')
# else: print('Bye!')

# num = int(input('Введите число'))
# print(num % 10)

# num = int(input('Введите число'))
# print(num // 1 % 10)
# print(num // 10 % 10)
# print(num // 100 % 10)
# print(num // 1000 % 10)

# cost = int(input('Введите сумму:'))
# money = int(input('Сумма:'))
# if cost % 100 == 0 and money % 100 == 0:
#     change=money - cost
# five_hundred = change // 500
# change = change % 500

# two_hundred = change // 200
# change = change % 200

# hundred = change // 100
# print(five_hundred , two_hundred, hundred)



a = float(input('Enter 1st number:'))
b = float(input('Enter 2nd number:'))
c = float(input('Enter 3rd number:'))
# if a > b > c: print(a, b, c)
# if a > c > b: print(a, c, b)
# if b > a > c: print(b, a, c)
# if b > c > a: print(b, c, c)
# if c > a > b: print(c, a, b)
# if c > b > a: print(c, b, a)
# print a == b == c: print(a, b, c)

large = max(a, b, c)
small = min(a, b, c)
midlle = a + b + c - large - small
print(large, midlle, small)