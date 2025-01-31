number = input("Digite um número inteiro: ")
intNumber = int(number)

if(intNumber%3==0 and intNumber%5==0):
    print("FizzBuzz")
else:
    print(intNumber)