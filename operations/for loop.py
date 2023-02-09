fruit = "banana"
for i in fruit:
    print(i)

#2
for i in range(1,10):
    print(i)

#3
list = [1,2,3,4,5,6,7,8,9,10]
n=5
for i in list:
    c = n*i
    print(c)

#4 sum of no
list = [1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list:
    sum = sum+i


print("sum is" ,sum)
#or
sum=0
for i in range(1,11):
    sum =sum+i

print(sum)

#or
n=int(input("enter he number:"))
for i in range(1,n):
    n=n+i
print(n)


#5 print even no
for i in range(0,11,2):
    print("even",i)




#6 create table
n = int(input("enter the no"))
for i in range(1,11):
    c=n*i
    print(n,"*",i,"=",c)

#nested loop
rows=int(input("enter rows"))
for i in range(0,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()

#inverted
rows=int(input("enter rows"))
for k in range(rows+1,0,-1):
    for l in range(k-1):
        print("*",end=" ")
    print()

#printing numbers
rows=int(input("enter rows"))
for i in range(0,rows+1):
    for j in range(i):
        print(j+1,end=" ")
    print()







