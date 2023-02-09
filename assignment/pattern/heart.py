#1
num = int(input("enter the number:"))
n =num//2
for i in range(2,n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range