#half pyramid pattern with number
row=int(input("enter the number"))
for i in range(0,row+1):
    for j in range(i):
        print(j+1,end=" ")
    print()

#reverse pattern
row=int(input("enter the number"))
for i in range(row+1,0,-1):
    for j in range(i-1):
        print(j+1,end=" ")
    print()

#pyramid with stars
n = int(input("enter rows"))
for i in range(n):#row5
    for j in range(n-i-1):#space 5-0-1=4
        print(" ",end="")
    for j in range(i+1):#column
        print("*", end=" ")
    print()














