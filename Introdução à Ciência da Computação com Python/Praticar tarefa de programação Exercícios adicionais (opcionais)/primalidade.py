number = int(input("Digite um número inteiro: "))

if number <= 1:
    print("não primo")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("não primo")
            break
    else:
        print("primo")