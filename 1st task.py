# Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#         Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>
user_name = input('Enter your name: ')
user_surname = input('Enter your surname: ')
user_age = input('Enter your age: ')
print('Hello,', user_surname, user_name + '.', 'Your age is:', user_age + '.')