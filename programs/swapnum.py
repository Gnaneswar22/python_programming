a=10
b=20
a,b=b,a
print(a)
print(b)

#with using temp variable

a=5
b=15
c=0
c=a
a=b
b=c
print("a",a)
print("b",b)


# by using assignment operators
a=15
b=10
a=a+b
b=a-b
a=b+a
print(a)
print(b)