def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def n_primos(n):
    contador = 0
    for i in range(2, n + 1):
        if eh_primo(i):
            contador += 1
    return contador

print(n_primos(121))