#covert string to tuple
x="hello"
print(tuple(x))

#list to tuple
l=[1,2,3]
print(tuple(l))

#finding repeated items
tple=(1,2,2,3,5,5)
i=0
for i in tple:
    if tple.count(i)>1:
     print(i)


#1 reverse a tuple
tpl=(1,2)
print(tpl[::-1])

#2 remove dupli and accessing value 20
tup=(1,2,40,30,20,30)
print(tup[len(tup)-2])
tup=tuple(set(tup))#remove dupli
print(tup)

#3 check all elements are same
tup=(1,2,3,4)
f=1
for i in tup:
    for j in range(i,len(tup)-1):
        if tup[i]!=tup[j+1]:
            f=0
            break
if f==1:
    print("same")
else:
    print("not same")
#or
tup=(1,2,3,4)
tup=set(tup)
if len(tup)==1:
    print("same")
else:
    print("not same")

#4 copy spcfc element from one tple to new
t=1,2,3,4,"adee"
newt=t[4:5]
print(newt)

#5 swaping two tples
t1=(1,2,3,4)
t2=(1,1,1)
temp=t1
t1=t2
t2=temp
print(t2)