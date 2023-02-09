#1 print unique values
dict=[{"v":"s001"},{"v":"s002"},{"vi":"s001"},{"vi":"s005"},{"vii":"s005"},{"v":"s009"},{"viii":"s007"}]
setofuvalues=set()
for i in dict:
    for value in i.values():
        setofuvalues.add(value)
print(setofuvalues)
#or
dict=[{"v":"s001"},{"v":"s002"},{"vi":"s001"},{"vi":"s005"},{"vii":"s005"},{"v":"s009"},{"viii":"s007"}]
ul=[]
for i in dict:
    ul.extend(list(i.values()))
ul= set(ul)
print(ul)


#2combine values
dict=[{"item":"item1","amount":"400"},{"item":"item2","amount":"300"},{"item":"item1","amount1":"750"}]
print("the given dictionary is: ")
newdict ={}
list1 = []
for d in dict:
    p=list(d.values())
    list1.append(p[0])
    list1.append([p[1]])

for i in range(0,len(list1),2):
    if list1[i] in newdict:
      rep=list1[i]
      index=list1.index(rep)
      list1[index+1]=list1[index+1]+list1[i+1]
      newdict[list[i]]=list1[index +1]
    else:
      newdict.setdefault(list1[i],list1[i+1])
print("the combined dic is: ",newdict)

#or



listofdict = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
#print("The given dictionary is : ",listofdict)
newdict = {}
list1 = []
for d in listofdict: #d gives each dictionary
    p = list(d.values()) #creates list of values
    list1.append(p[0])
    list1.append(p[1])#list1 contains all individual values in a single list

for i in range(0,len(list1),2): #taking each 2nd item in list1
    if list1[i] in newdict:
        rep = list1[i]
        index = list1.index(rep)#finding index of repeated variable
        list1[index+1] = list1[index+1]+list1[i+1] #adding corresponding value
        newdict[list1[i]] = list1[index +1] #updating value of repeated element
    else:
        newdict.setdefault(list1[i],list1[i+1]) #adding values to dicitonary as key:value pairs

print("The combined dictionary is : ",newdict)

#or
d=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
lst={}
for i in d:
    if i['item']not in lst:
        lst[i['item']]=i['amount']
else:
    lst[i['item']]+=i['amount']
    print(lst)



#3
dict1 ={"MATHS":87,"SCIENCE":90,"ENGLISH":95,"MALAYALAM":100}
name = "CR7"
print("Student name : ",name)
for key,value in dict1.items():
    print("The student scored ",value,"marks in subject ",key)"""

#4
"""
setdefault():
-------------
If key is in the dictionary, return its value.
If not, insert key with a value of default and return default.
default defaults to None.

"""
"""str1 = 'Luminar'
#print("The given string is :",str1)
dict1 = {}
for index in range (1,len(str1)+1): #1, 7+1 = 1, 8
    #print(index)
    dict1.setdefault(index,str1[index-1])
    #print(index-1)
    # print(str1[index-1])
    # print(index,str1[index-1])
print("The corresponding dicitonary of the given string is :",dict1)

#or
str1="luminar"
str_dict={}
for i in range(1,len(str1)+1):
    str_dict[i]=str1[i-1]
    #str_dict.update({i:str1[i-1]})
print(str_dict)

#5 printing in table format
dict1 ={"MATHS":87,"SCIENCE":90,"ENGLISH":95,"MALAYALAM":100}
print("SUBJECT\t\t\t\t\tMARKS\n*****************************")
for key,value in dict1.items():
    if key =="MATHS":
        print(key,"\t\t\t\t\t",value)
    else:
        print(key, "\t\t\t\t", value)

#6 ascending and descending
"""dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("thegiven dict is:",dict1,"\n")
val=list(dict1.items())
newval=[]
newvalf=[]

for i in val:
    irev=i[::-1]
    newval.append(irev)
val.clear()
newval.sort()

for i in newval:
    irevf=i[::-1]
    val.append(irevf)
in complt"""


