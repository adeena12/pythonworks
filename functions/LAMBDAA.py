#lambda function :its a small anonymous fuction.it can take any no of args but can only have one expression
#lambda dont have name ,lambda keywordd,only one sttmnt,auto return
#normal
"""def sum(a,b):
    return a+b
print(sum(10,20))

#using lambda
add=lambda a,b:a+b
print(add(2,3))

#finding largest
largest=lambda a,b:a if a>b else b
print(largest(300,500))"""

#filter,map,reduce
#filter:all item will go iterarion only condition satisfied will be oreturn
l=[10,2,3,4,50]
lst=list(filter(lambda x:x%2==0,l))
print(lst)

#map:all items iterate and all item return
l=[10,2,3,4,50,77,11]
lst1=list(map(lambda x:x>2,l))
print(lst1)

#reduce
from functools import reduce
l1=[1,2,3,4,5]
product=reduce(lambda a,b:a*b,l1)
print(product)