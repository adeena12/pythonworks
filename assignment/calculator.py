choice = input("enter the choice : +,-,*,/ :")
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
if choice=='+':
    print("sum is ", a+b)
elif choice=="-":
    print("difference is ",a-b)
elif choice=="*":
    print("result is ",a*b)
elif choice=="/":
    print("product is ",a/b)
else:
    print("invalid")


