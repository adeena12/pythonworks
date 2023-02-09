#TUPLE
#immutable,orderd,indexed,allow duplicate,coma separated(if not paranthesis),using paramthesis,muliple dt possible
tple=(1,2,4,6,"adeena",{1},1.3,[2])
print(type(tple))
print(tuple(tple))#to convert to tuple if ts a list or some other
print(len(tple))
print(tple[0])#assessing element using index
print(tple[-1])
print(tple[1:3])
print(tple[::-1])
print(tple[:-5])#last 5 digits will b removed

#to update a tuple we have to frst convert to mutable dt
y=list(tple)
y[0]="dona"#mutable data type like list here
tple=tuple(y)#changing list to tuple
print(tple)

#to append we have to frst convert to mutable dt
c=list(tple)
c.append('rrr')
tple=tuple(c)
print(tple)

#add a tuple
b=("d","f")
tple +=b
print(tple)

#remove
x=list(tple)
x.remove("d")
tple=tuple(x)
print(tple)

#delete
#tple2=(7,8)
#del tple2
#print(tple2)

#unpacking
fruits=("apple","mango","stwbrry","papaya","raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#iteration using for
tp=("a","b","c")
for i in tp:
    print(i)
for i in range(len(tp)):
    print(tp[i])

#using while
tp1=("v","h","c")
i=0
while i < len(tp1):
    print(tp1[i])
    i=i+1
#nested
tple=(1,2,4,6,"adeena",{1},1.3,[2])
print(tple[0])
print(tple[4][1])
tple[7][0]=3#replacing a list in a tuple(we can only change mutable dt in a nested tuple)
print(tple)

#concatenation
print((1,2)+(5,6))
#repeat
print(("ad",)*3)
#count
print(tple.count(2))
#index
print(tple.index("adeena"))
#in not in
print(1 in tple)
print("adeena" not in tple)
#all
print(all(tple))

a=(1,2,3,6,8)
print(len(a))
print(all(a))
print(max(a))
print(min(a))
print(sorted(a))
print(sum(a))
y=enumerate(a)
print(tuple(y))
#or
names=("a","b")
age=(1,2)
for i, (names,age) in enumerate (zip(names,age)):
    print(i,names,age)

#or
letters=[('a','A'),('b','B')]
for i,letters in enumerate(letters):
    print("letter #%d is %s/%s"%(i,letters[0],letters[1]))

#map
l=['sat','bat']
test=set(map(tuple,l))
print(test)


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