def fizzbuzz(number):
    if(number%3==0 and number%5==0):
        return "FizzBuzz"
    if(number%5==0):
        return "Buzz"
    if(number%3==0):
        return "Fizz"
    else:
        return number

print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(4))

