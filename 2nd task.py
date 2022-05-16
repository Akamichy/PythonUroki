# Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника
# по двум катетам. (с = sqrt(a * a  +  b * b))
import math
a = float(input('Side A: '))
b = float(input('Side B: '))
c = (a * a  +  b * b)**0.5
print('Side C = ', c)