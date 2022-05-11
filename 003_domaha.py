range = range(1,101)
for num in range:
    if num % 3 == 0:
        print(num)
        print('Fizz')
    if num % 5 == 0:
        print(num)
        print('Buzz')
    if num % 15 == 0:
        print(num)
        print('FizzBuzz')
