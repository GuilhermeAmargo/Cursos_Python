n = int(input("Digite o valor de n: "))
f = 1
i = 1

if(n==0):
    print(1)
else:
    while i <= n:
        f *= i
        i += 1
    print(f)