import datetime
"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
# dt_str3 = '7 Июнь 2021, 12:56'
# dt_str3 = dt_str3.replace('Июнь', 'June')
# str_to_date3 = datetime.datetime.strptime(dt_str3, '%d %B %Y, %H:%M')
# print(str_to_date3)
# print(type(str_to_date3))

# Write a program that converts given string to datetime object
sample1 = 'Jan 01 2014, 2:43PM'
sample1w = datetime.datetime.strptime(sample1, "%b %d %Y, %I:%M%p")
print(sample1w)
print(type(sample1w))
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample2w = datetime.datetime.strptime(sample2, "%H:%M %y/%m/%d")
# print(sample2w.strftime("%y/%m/%d %H:%M"))
print(sample2w)
print(type(sample2w))


sample3 = 'Tuesday, September 24, 2019'
sample3w = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(sample3w)
print(type(sample3w))

sample4 = '01.01.1970 - 00:00:01'
sample4w = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(sample4w)
print(type(sample4w))

# Write a program to print yesterdays, today and tomorrow dates
today = datetime.datetime.today()

dif = datetime.timedelta(days=1)
yesterday = (today - dif)
tomorrow = (today + dif)
print('Yesterday was', yesterday)
print('Today is', today)
print('Tommorow will be', tomorrow)


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
someday = datetime.datetime.fromtimestamp(some_day)
print(someday)

# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)
timestamp1 = '17 Jan 2024'
timestamp1converted = datetime.datetime.strptime(timestamp1, '%d %b %Y')
timestamp12 = datetime.datetime.timestamp(timestamp1converted)
print(timestamp12)
def substraction(x, y):
    return x-y
print(substraction(1705442400.0, (604800.0*2.0)))

