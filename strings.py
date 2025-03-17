'''
strings aer used to represent the textual data

1. single quoted = 'gnanesh'
2. double quoted = "gnanesh"   '''
 # 3. triple quoted = '''gnanesh'''( multi line comments)

# string indexing
'''the indexing in pytho will start from zero
      str="p  y  t  h  o  n"
           0  1  2  3  4  5  (positive indexing)
          -6 -5 -4 -3 -2 -1  (negative indexing)

'''

'''
#accessing of character
str="python"
print(str[0])
print(str[-6])
'''



#slicing
'''str_variable =[start:stop:step]
 [strating index : last/end index : increment]


'''
'''str="0123456"
print(str[-1:-7:-2])


s="hello world"
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])


str1=" gnanesh"
str2="DAMARASINGU"
print(str1 + " " +str2)
print(len(str1))
print((str1.upper()))
print(str2.lower())
print(str2.replace ("A", "x"))
print(str1.strip())
print(str2.count('A'))



print("abrakabadra" .count('a'))


#string formatting
name='abrakabadra'
age=10000000
print("the name %s is having %d. " %(name ,age))
print("name is {} and age is {} " .format(name,age))

# escape sequence
print("hello\n world")






# major topics are slicing and string indexing




#problems on strings in decision making

#count of vowels in a string
s=input("enter the you name")
s=s.lower()
a=s.count('a')
e=s.count('e')
i=s.count('i')
o=s.count('o')
u=s.count('u')
print(f"the no of vowels : {a+e+i+o+u}")


#grade calculator


math=int(input("enter the marks in maths"))
science=int(input("enter the marks in science"))
english=int(input("enter the marks in english"))
total_marks=math+science+english
avg=math+science+english/3
percentage=(total_marks/300)*100
grade=" "
if percentage>90:
    grade="A"

elif percentage>80 :
    grade="B"

elif percentage>70 :
    grade="C"

elif percentage>60 :
    grade="D"
else:
    grade="F"

print("total_marks", total_marks  ,"average_marks",avg , "percentage" , percentage,"garde" , grade) 


'''

#palindrom checker



s=input("enter the string")
r=s[::-1]
if s==r:
    print("palindrome")
else:
    print("not a palindrome")