'''
creating a calculator for performing all +,-,*,/ operations for 2 numbers.

'''

number_1 =int(input("enter number 1 : "))
number_2 =int(input("enter number 2 : "))
operators =input("enter operator : ")
if operators == "+":
    print("the sum is: ",number_1+number_2)

elif operators == "-":
    print("the difference is: ",number_1-number_2)

elif operators == "*":
    print("the product is: ",number_1*number_2)

elif operators == "/":
    if number_2 == 0:
        print("Error: Division by zero")
    else:
        print("the quotient is: ",number_1/number_2)

else :
    print("Error: Invalid operator")