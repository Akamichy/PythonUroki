range = range(1,101)
for num in range:
    if num % 15 == 0:
        print(num)
        print('FizzBuzz')
    elif num % 3 == 0:
        print(num)
        print('Fizz')
    elif num % 5 == 0:
        print(num)
        print('Buzz')
