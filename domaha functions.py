"""
Под каждым комментарием нужно написать одну функцию
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a function that takes a list of numbers
# And returns same list but numbers multiplied by 2
# input: list of numbers
# output: list of numbers multiplied by 2
def double(a,b):
    return a*2, b*2
print(double(2, 4))


# Write a function that takes a list of numbers
# And returns same list but numbers multiplied by 4
# USE PREVIOUS FUNCTION TO CREATE THIS ONE
# input: list of numbers
# output: list of numbers multiplied by 4
def double(a,b):
    return a*4, b*4
print(double(2, 4))

# Write a function that will check if users input is palindrome
# "Able was I ere I saw Elba" is a palindrome!!!
# input: nothing
# output: boolean
a = input('Введите слово, которое хотите проверить: ')
def palindrome():
    global a
    if str.lower(a) == str.lower(a[::-1]):
        return True
    else:
        return False
print(palindrome())

# Write a function that prints a list of squared numbers from 1 to 30
# input: nothing
# output: nothing
def squared(number):
    return number**2
for num in range(1,31):
    print(squared(num), num)



# Write a function that multiplies all numbers in a list provided by user
# input: nothing
# output: float of multiplied numbers
list = [8, 3, 4, 5, 6, 7]
def mult(position, number):
    return float(list[position]*number)
print(mult(1, 2))