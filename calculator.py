#Calculator done by Aryan
a=int(input("Enter the First Number : "))
b=int(input("Enter the Second Number : "))

print("1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division")

c=input("Enter the Operation you want to perform : ")

if c=="1":
    print("The Sum is : ",a+b)

elif c=="2":
    print("The Difference is : ",a-b)

elif c=="3":
    print("The Product is : ",a*b)
else:
    if b!=0:
        print("The Quotient is : ",a/b)
    else:
        print("Division by zero is not allowed.")