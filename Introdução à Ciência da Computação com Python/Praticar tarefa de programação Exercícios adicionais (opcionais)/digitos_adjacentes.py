numero = input("Digite um número inteiro: ")

for i in range(1, len(numero)):
    if numero[i] == numero[i-1]:
        print("sim")
        break
else:
    print("não")
