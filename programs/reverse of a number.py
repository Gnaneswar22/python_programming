"""num=input("enter a number : :")
print(num[: :-1])
"""
#this is a format by using strings



#another format like by using // and %

num=int(input("enter the number :: "))
reversed_num=""
while(num>0):
    rev_digit=num%10
    reversed_num+=str(rev_digit)

    num=num//10
    

print(reversed_num)

