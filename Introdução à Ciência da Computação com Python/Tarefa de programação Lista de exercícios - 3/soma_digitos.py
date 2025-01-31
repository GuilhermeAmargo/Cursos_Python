numero = int(input("Digite um número inteiro: "))

soma = 0

numero = abs(numero)

while numero > 0:
    soma += numero % 10  
    numero //= 10        

print(soma)
