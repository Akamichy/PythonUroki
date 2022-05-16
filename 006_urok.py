# def double(number):
#     if number % 2 == 0:
#         return number * 2
#     else:
#         return number * 3
# print(double(101))

# x = 10
# def sample():
#     global x
#     x = x**2
#     return x
# print(sample())

# def square_area(a, b):
#     return a * b
# a = 10
# b =20
# print(square_area(a, b))

# def say_hello(name, surname, age):
#     return f'Hello {name} {surname}. You are {age} years old.'
# students = [('Jack', 'Smith', 20), ('Sarah', 'Lincolns', 25)]
# print(say_hello(students[0][0], students[0][1], students[1][2]))
# for student in students:
#     print(say_hello(student[0], student[1], student[2]))

# def sampler(a, b, *args, **kwargs):
#     print(a,b)
#     for x in args:
#         print('Arg', x)
#     for y in kwargs:
#         print('Kwargs', y)
#                                 обязательно сохранять порядок функции
# sampler(10,10, 123, 321, 44444, 120318293, x=5, y=10, z=1)

# def sampler2(a,b,c=1):
#     print(a,b,c)
# (sampler2(2,3))

import math

print(math.sqrt(144))
