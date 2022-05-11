print(56)
print(type(56))
print(23.123123)
print(type(2131.123123))

x = 5
print(x/2, "hello")
print(10**2)

print("Hello world")
print(type("Hello world"))

x = " "
print(type(x))

string_1 = 'hello world'
string_2 = "hello world"
string_3 = '''Hello world'''
string_4 = """Hello world"""
x = True
y = False
print(x)
x=123123123
print(x)
x= True
print(x)
# Integer (int)
# Float (float)
# String (str)
# Boolean (bool)
# Nonetype (None)
a = True
b= None
c = 12312312.1111
x = 5
y = "Hello"
z = "456"
print(int(z))
print(int((c)))

print(bool(-1)) #True
print(bool(0)) #False
print(bool("asdasdasd")) #True
print(bool()) #False
print(bool(None)) #False
user_name = "Jack"
user_surname = "Smith"
user_age = 25
has_job = True
print("Hello " + user_name + " " + user_surname + ". You are " + str(user_age) + " years old. It is", str(has_job), "that you have a job.")
username = input("Please enter something: ")
print(username)

side_a = float(input("Please enter side A: "))
side_b = float(input("Please enter side B: "))
side_c = float(input("Please enter side C: "))
half_perimetr = (side_a + side_b + side_c) / 2
triangle_area = (half_perimetr * (half_perimetr - side_a) * (half_perimetr - side_b) * (half_perimetr - side_c)) ** 0.5
print(triangle_area)