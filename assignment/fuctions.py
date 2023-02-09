"""
#calculator using fnctns
num1=int(input("enter frst no"))
num2=int(input("enter sec no"))
op=int(input("1.addition\n2.substraction\n3.multiplication\n4.division\n""please enter your operation "))
def add(a,b):
    print("sum is",a+b)
def sub(a,b):
    print("result is",a-b)
def mul(a,b):
    print("product is",a*b)
def div(a,b):
    print("result",a/b)

if op==1:
    add(num1,num2)
elif op==2:
    sub(num1,num2)
elif op==3:
    mul(num1,num2)
elif op==4:
    div(num1,num2)
else:
    print("select valid option")

#multiply all no using function
def multiply(l1):
    total=1
    for i in l1:
        total=total*i
    return total
print(multiply(l1=[5,4,3,2]))

#reverse a string
str1=input("enter the string")
def reverse(str1):
    words=str1[::-1]
    print(words)
reverse(str1)

#calculate factorial of number
num=int(input("enter the no"))
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(num))

#prime or not
def prime(x):
    if x==1:
        print("1 is neither prime or compute")
    elif x<1:
        print("enter a pstv value")
    elif x==2:
        print("2 is prime")
    else:
        flag=1
        for j in range(2,x):
            if x%j==0:
                flag=0
                break
            else:
                continue
        if flag==0:
            print("the number {x}  not prime"")

#
def calculator(a,b):
    def addition():
        c=a+b
        return c
    return addition()+5
print(calculator(2,3))

#find eve no from 4 t 30
s=int(input("enter strng pos"))
e=int(input("enter ending pos"))
def even(a,b):
    e=[]
    for i in range(a,b,2):
        e.append(i)
    return e
print(even(s,e))"""


#1acces a fnctn inside afnctn

def outer(a,b):
    def inner():
        c=a+b
        return c
    return inner()
print(outer(2,3))


#2
"""def square():
    li=[]
    for i in range(1,31):
        li.append(i**2)
    return li
print(square())

#3aasign diff name o fn and call through new name
def fun(a,b):
    print(a+b)
newname=fun
newname(4,5)

#4  generate list contain all even no b/w 4 and 30
def even():
    li=[]
    for i in range(4,30):
        if i%2==0:
            li.append(i)
    return li
print(even())

#5 fnctn accept two argument and return sum
def sum(a,b):
    print(a+b)
sum(3,4)

#6 fn accptdiff values as parameters and return list
def vlues():


#present or absent
rollno=int(input("enter a no"))
def stu(rollno):
    i=[1,3,4,5,7,9]
    if rollno in i:
        print("present")
    else:
        print("absent")
stu(rollno)

#count of vowels or consonent
def count(val):
    vow=0
    con=0
    for i in range(len(val)):
        if val[i] in ["a","e","i","o","u"]:
            vow=vow+1
        else:
            con=con+1
    print(vow)
    print(con)
x=input("enter string")
count(x)

#find max
def max(a,b,c):
    if a>b and a>c:
        print("a is max")
    if b>a and b>c:
        print("b is max")
    else:
        print("c is max")
max(34,56,28)"""

