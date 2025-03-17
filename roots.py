a,b,c=input("give the values of a,b and c").split(",")
a=int(a)
b=int(b)
c=int(c)
d=(b**2)-4*a*c
r1=(-b+d**0.5)/2*a
r2=(-b-d**0.5)/2*a
print(r1)
print(r2)