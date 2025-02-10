def vogal(vogal):
    if(vogal=="a" or vogal=="A"):
        return True
    if(vogal=="e" or vogal=="E"):
        return True
    if(vogal=="i" or vogal=="I"):
        return True
    if(vogal=="o" or vogal=="O"):
        return True
    if(vogal=="u" or vogal=="U"):
        return True
    else:
        return False

print(vogal("a"))  # True
print(vogal("A"))  # True
print(vogal("e"))  # True
print(vogal("E"))  # True
print(vogal("i"))  # True
print(vogal("I"))  # True
print(vogal("o"))  # True
print(vogal("O"))  # True
print(vogal("u"))  # True
print(vogal("U"))  # True
print(vogal("b"))  # False
print(vogal("B"))  # False
print(vogal("1"))  # False
print(vogal("@"))  # False