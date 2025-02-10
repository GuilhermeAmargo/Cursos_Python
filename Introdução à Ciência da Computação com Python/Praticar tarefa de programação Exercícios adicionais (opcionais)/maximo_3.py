def maximo(n1, n2, n3):
    if(n1>=n2 and n1>=n3):
        return n1
    if(n2>=n1 and n2>=n3):
        return n2
    return n3

print(maximo(10, 20, 10))