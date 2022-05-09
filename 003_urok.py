user_id = input('Please enter id code: ')
if len(user_id) !=11:
    if len(user_id) > 11:
        print('Code is too long')
    else:
        print('Code is too short')
else:
    if user_id.isdigit():
        print(f'Your ID is {user_id}')
    else:
        print('You have to use numbers only')
# user_input = input('Please input:')
# if user_input == '1':
#     print('1')
# elif user_input == '2':
#     print('2')
# elif user_input == '3':
#     print('3')
# else:
#     print('Choice is out of range')

# x = 'Hello world'
# if 'world' in x:
#     print('greater than 100')
# elif x == 150:
#     print('X is 150')
# elif x != 150:
#     print('X is not 150')
# else:
#     print('Hello world')



#если все условия провалились, то else выполняет в таком случае выбранную команду (exmpl:если все условия провалились, напиши привет мир)
#если условие if проверилось, остальные не проверяются, игнорируются
# x = 0
# x += 1
# print(x)
# x += 5
# print(x)
# x == y - equal (False)
# x! = y - not equal (true)

# price = 500
# name = 'john'
# surname = 'smith'
# age = '35'
# result = f'Hello {name.capitalize()} {surname.capitalize()}. You are {age} years old. Your salary is {price:.2f}$.' #- автоматом поставило заглавные буквы у слова с помощью capitalize
# print(result)
# byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_sting.decode('utf-16'))
# sample = 'Hello world'
# print(sample.encode('utf-8'))
# result = 'Price is {:.2f}'
# print(result.format(float(price)))


# print(round(1.5))
# print(round(2.5))


# name = 'John'
# surname = 'Smith'
# age = input("Введите ваш возраст: ")
# result = '{} {} is {} years old'
# result = '{1} {0} is {2} years old'
# result = '{user_name} {user_surname} is {user_age} years old'
# print(result.format(user_name=name, user_surname=surname, user_age=age))

# .format ищет {} в строке и заменяет ее на переменную в зависимости от последовательности в скобках, последовательность можно выставлять в {}, последовательность начинается от нуля
# \n = перенос строки
# print('Hello\nWorld')
# string_sample = "Hello world world"
# string_sample2 = "first letteR is lowErcase"
# string_sample3 = "extra whitespace string "

# x = 'hello world'.split() #возвращает список, массив, разделяя после каждого после делителя(по стандарту пробел)
# print(x)

# name, surname = input('Please enter your Name and Surname ').split(' ')
# print(name)
# print(surname)

# x = "hel\"lo" - "\\" один такой слэш означает окончание строки
# print(string_sample.find("world", 7)) - считает с какого символа (по порядку) находит выбранное слово
# print(string_sample.count("world")) - считает сколько раз найдено слово
# print(string_sample[-7:-1])
# x = string_sample[3]
# print(x)
# for x in range(1, 101):
#     print(x)
# print(string_sample[::-1])
#[START:END:STEP]
# print(string_sample[5:len(string_sample)])
# print(len(string_sample))
# print(string_sample[16])
# print(type(len(string_sample))) - class int!!!!!
# print(string_sample in string_sample) - clas bool
# print(string_sample2.upper()) все буквы капсом
# # print(string_sample2.isupper()) тру/фолс
# print(string_sample3.lower()) делает все буквы в переменной маленькими
# # print(string_sample3.islower()) тру/фолс
# print(string_sample3.casefold())
# # user_entry = input().lower
# print(string_sample2.capitalize())
# print(string_sample2.title()) все первые буквы в слове заглавные
# string_sample = ("********* kfbksdfbsdfbb ****")
# print(string_sample.strip("* ")) убирает выбранный символ из переменной, не меняя ее тип
# print(string_sample.rstrip("*"))
# print(string_sample.lstrip("*"))
