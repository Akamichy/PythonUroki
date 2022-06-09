# Sample string
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
Wall Ball Mall Hall
123.123-1233
'''

sentence = 'Start a sentence and then bring it to an end'
'''
\. - находит конкретно точку
просто точка - находит все, кроме переноса строки
^ - находит слово в начале строки
$ - находит слово в конце строки(ставится после объекта поиска(start$))

'''

# pattern = re.compile(r'M(rs|s|r)\.? [A-Z][a-z]*')
# # pattern = re.compile(r'')
# matches = pattern.finditer(text_to_search)
# # matches = pattern.finditer(sentence)
# print(matches)
# for match in matches:
#     print(match.start(), match.end(), match.group())


# with open('people.txt', 'r', encoding='utf8') as file:
#     people_data = file.read()
#
#     pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
#     matches = pattern.finditer(people_data)
#     for match in matches:
#         print(match.group())

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
example.co.uk
'''
# pattern = re.compile(r'[A-Za-z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+')
pattern = re.compile(r'(http://|https://)?(www\.)?(\w+)(\.\w+)+')
# subbed = pattern.sub(r'\3\4', urls)
# print(subbed)
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3)+match.group(4))
print(9/10)

