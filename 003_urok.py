string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = "extra whitespace string "

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

print(string_sample2.upper())
# print(string_sample2.isupper())
print(string_sample3.lower())
# print(string_sample3.islower())
print(string_sample3.casefold())
# user_entry = input().lower

print(string_sample2.capitalize())
print(string_sample2.title())
user_name = str(input("Введите ваше имя: ").title)
print(str(user_name))
