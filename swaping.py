#with temporaryvariable
'''
a=int(input("Enter value of a"))

b=int(input("Enter value of b"))

temp=a
a=b
b=temp
print(f"value of a : {a} ,value of b : {b}")

'''
#without temporary variable

a=int(input("Enter value of a"))

b=int(input("Enter value of b"))

a=a+b
b=a-b
a=a-b
print(f"value of a : {a} ,value of b :{b}")
