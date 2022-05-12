'''Программа, которая находит простые числа и ищет их общую сумму'''
# primes = []
# n = int(input('Введите число N:'))
# for num in range(1, n + 1):
#     cnt = 0
#     if num == 1:
#         primes.append(num)
#     for num1 in range(1, num + 1):
#         if cnt > 2:
#             break
#         if num%num1 == 0:
#             cnt += 1
#     if cnt == 2:
#         primes.append(num)
# print(sum(primes))
x = 5
'''такие скобки создают словарь
str:str - структура словаря, не разрешены дубликаты ключей внутри(они в левой позиции), значение может повторяться
ключи можно переносить таким образом: {
                                        }
значение ключу присваивается двоеточием'''
student = {'name':'John', 'age':32, 'courses':['Math', 'Biology', 'Art'], 1:'int_key', 2.0:'float_key',
           x:'variable', 'Hello': x, 'y':{'new_name':'Mary', 'new_surname':'Smith'}}
# print(student.keys())
# print(student.values())
# print(student.items())
# print(list(student.items())[0])
# for key in student.items():
#     print(key[0])
# for x in student:
#     print(student[x])
