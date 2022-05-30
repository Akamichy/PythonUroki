'''
1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
	HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.

2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)

3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.

4. Написать программу котороая будет выбирать из файла people.txt:
	1) Все имена и фамилии
	2) Все адреса

5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-9.

6. Написать регулярное выражение для определения эстонского личного кода (isikukood)

Все строки произвольные.
'''
import csv
import re
color = ''' 
#A58E44
#574714
#GGGHUJ
FFFF
#FFFF
#CFCBC0
#3D2F07
'''
pluses = '''
3+4-5
2*9-6*5
(3+5)-9*4
3/5
'''
times = '''
9:00
00:23
00:00
23:59
34:78
'''
symbols1 = '''
HAHAHAHhahahahaha12389aaaa
HAhahahhajhahahah123---11110099...
'''
isikukoods = '''
50205057028
99503127029
34563345532
64512317029
'''
colors = re.compile(r'#([0-9]|[A-F]){6}')
colormatches = colors.finditer(color)
for match in colormatches:
        print(match.group())
plusfinder = re.compile(r'[0-9]+([*]|[/]|[-]|[()])[^+]')
plusmatches = plusfinder.finditer(pluses)
for match in plusmatches:
    print(match.group())
time = re.compile(r'[0-23]+:[0-59]+')
timematches = time.finditer(times)
for match in timematches:
    print(match.group())
symbols = re.compile(r'[a-zA-Z0-9]+')
symbolsmatches = symbols.finditer(symbols1)
for match in symbolsmatches:
    print(match.group())

isikukood = re.compile(r'[1-8][\d][\d][0-1][\d][0-3][\d][0-7][\d][\d][\d]')
                        # 5   0   2  0     5   0    5   7    0   2   8
isikmatch = isikukood.finditer(isikukoods)
for match in isikmatch:
    print(match.group())
# with open('people.txt', 'r', encoding='utf8') as file:
#     data = csv.reader(file, delimiter='\n')
#     for info in data:
#         print(type(info))
    # for line in data:
    #     print(line)