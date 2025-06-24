# loops - repeatable statements or interative statements

'''
types of loops 
 for loop
 while loop

'''


'''
while loop

while condtion:
     statement 1
     statement 2
 
  




candies=10
while candies>0:
    print(" happy birthday")
    candies-=1    
    
'''



#for loop

'''
for variable in range(start, end, step):
    statement 1
    statement 2


for i in range(1, 11):
    print(i)


candies=10
for i in range(candies):
    print("happy birthday")'
    



for i in range(0,9,2):
  print(i)


for i in range(1,6):
    for j in range(0,11):
        print(i*j)'
        '
'''


n=10

i=1
sum=0
'''
while i<=n:
    sum+=i
    i+=1

print("sum:", sum)

for i in range(1,11,2):
    sum+=i
    print("sum:", sum)


n=3
for i in range(1,11):
    print(f"{i}*{n}={n*i}")
 
a=10
b=5
a-=b
b+=a
print("a",a)
print("b",b) '''

a=10
print(a)
