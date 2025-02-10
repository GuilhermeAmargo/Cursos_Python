x = int(input("Digite a largura: "))
y = int(input("Digite a altura: "))

for i in range(y):
    if i == 0 or i == y - 1:
        print("#" * x)  
    else:
        print("#" + " " * (x - 2) + "#")  
