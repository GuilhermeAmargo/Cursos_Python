def eh_primo(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

def maior_primo(n):
    for num in range(n, 1, -1):
        if eh_primo(num):
            return num

# Testes
print(maior_primo(100))  # 97
print(maior_primo(7))    # 7
print(maior_primo(50))   # 47
print(maior_primo(2))    # 2
