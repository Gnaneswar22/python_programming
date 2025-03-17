#functions in pyton
def add(a,b):
    return a+b


def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Error: Division by zero is not allowed"
    else:
        return a/b
    

a=input("Enter first number:")

b=input("Enter second number:")

a=int(a)
b=int(b)
result=mul(a,b)
print (result)