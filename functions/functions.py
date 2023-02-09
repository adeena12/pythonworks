"""
#
def sample():
    print("hi")
sample()
sample()

#
def sum():
    a=1
    b=3
    c=a+b
    return c
print("sum is ",sum())

#arguments
def sample(name1,name2):
    print("hi",name1,name2)
sample("adeena","amrin")

#arbitary
def sample(*name):
    print("my name",*name)
sample("h","j","g")

#keywrd argu
def my_function(child3, child2, child1):
    print("the youngest child is"+child3)
my_function(child1="thon",child2="ghos",child3="vor")

#arbitary keyword argu
def my_function(**kid):
    print("hs last name is "+kid["lname"])
my_function(fname="fgd",lname="gfd")

#default parameter value
def my_function(country="norway"):
    print("iam from"+country)
my_function("sweden")
my_function("india")
my_function()

#sum of numbers
def sum(a,b):
    print("sum is ",a+b)
sum(4,5)

#square
def square(num):
    return num**2
print("square is ",square(9))

#sum of list
list=[1,2,3]
def sum[1,2,3]:
    print("sum is",sum(1,2))"""

#creating a list
l=[]
def create():
    number=int(input("enter the no f elements:"))
    for i in range(number):
        item=int(input("enter the item :"))
        l.append(item)
    print(l)
def search():
    item2=int(input("searched item:"))
    if item2 in l:
        print("found")
    else:
        print("not found")
def remove():
    item3=int(input("enter the removed item"))
    if item3 in l:
        l.remove(item3)
        print(l)
def replace():
    item4=int(input("enter the replace item"))
    item5= int(input("enter the chaged item"))
    for i in range(len(l)):
        if l[i]==item4:
            l[i]=item5
    print(l)
while True:
    opt=int(input('1.create\n2.search\n3.remove\n4.replace\n enter ur choice'))
    if opt==1:
        create()
    elif opt==2:
        search()
    elif opt==3:
        remove()
    elif opt==4:
        replace()
    else:
        break

# create()
# search()
# remove()
# replace()