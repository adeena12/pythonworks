#1 adding elements in a list using while loop
"""n=int(input("enter the limits: "))
my_list=[]
i=1
while i<=n:
    my_list.append(i)
    i=i+1
print(my_list)

#2finding average of 5 numbers using while loop
i=1
s=0
while i<=5:
    n = int(input("enter the numbers %d:"%(i)))
    s=s+n
    i=i+1
avg=s/5
print("average is: ",avg)


#3 square of numbers using while loop

n=int(input("enter the limit of numbers: "))
i=1
while i<=n:
    t=i*i
    print("",i,"=",t)
    i=i+1

#4 reversing no
n=int(input("enter no:"))
rev=0
while n>0:
    rev=(rev*10)+n%10
    n=n//10
print("reverse=",rev)


#5 sum of even numbers
n=int(input("enter the limits: "))
i=0
s=0
while i<=n:
    s=s+i
    i=i+2
print("sum of even no is:",s)

#6check whether a no is prime or not
n=int(input("enter a no: "))
i=1
f=0
while i<=n:
    if n%i==0:
        f=f+1
    i=i+1
if f==2:
    print("prime number")
else:
    print("not prime")"""


#7 print even and odd between 1 to entered no
n=int(input("enter the limit: "))
i=1
while i<=n:
    if i%2==0:
        print(i,"is even")
    else:
       print(i,"is odd")
    i=i+1







