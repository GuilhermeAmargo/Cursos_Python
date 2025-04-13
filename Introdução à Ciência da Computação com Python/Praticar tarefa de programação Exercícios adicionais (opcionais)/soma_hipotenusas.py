def é_hipotenusa(h):
    for i in range(1, h):
        for j in range(i, h):
            if i * i + j * j == h * h:
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for h in range(1, n + 1):
        if é_hipotenusa(h):
            soma += h
    return soma

print(soma_hipotenusas(25))