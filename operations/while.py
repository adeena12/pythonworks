#while loop
str1 = "banana"
index = 0
while index<len(str1):
    letter = str1[index]
    print(index,letter)
    index = index+1

#print 1-10
i=1
while(i<=10):
    print(i)
    i=i+1

#print table of numbes
i=1
number=int(input("enter the no: "))
while i<=10:
    print("%d x %d=%d\n"%(number,i,number*i))
    i=i+1

#break
i=1
while(i<=10):
    if i==3:
     break
    print(i)
else:
    i=i+1

#sum of natural no sing whilw
n = int(input("enter the number"))
i=1
sum=0
while i<=n:
        sum =sum+i
        i=i+1
print("result is",sum)

#reverse of a no
n=123
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)

#product
n = 123
rev = 0
p=0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    p=p*r
    n = n // 10
print(p)

#sum
n = 123
rev = 0
s=0
while n > 0:
    r = n % 10
    s=s+r
    n=n//10

print(s)




