#set{}
#immutable,dont allow dupli,unorderd,unindexed
set_sam={1.0,2,"hello",(1,2,3)}
print(set_sam)
a=set([3,4])
print(a)

#operations
a={1,3,4,5}
b={3,5,7,8}
print(a|b)#union
print(a&b)#intersection
print(a-b)#difference
print(a^b)#symmetric difference


#1adding list to set
set1={3,4,67}
li=[1,2]
set1.update(li)
print(set1)

#2 get only unique element
se1={1,7,8,6}
se2={3,7,8,5}
print(se1|se2)

#3
se1={1,7,8,6}
se2={3,7,8,5}
if se1.isdisjoint(se2):
    print("no common")
else:
    print(se1&se2)

#4
se1={1,7,8,6}
se2={3,7,8,5}
se1.intersection_update(se2)
print(se1)



