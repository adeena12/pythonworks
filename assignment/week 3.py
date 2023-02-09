#1 remove empty string

str1=["john","","jack","jins"]
i=0
while i <len(str1):
    if len(str1[i])==0:
       str1.pop(i)
    i=i+1
print(str1)

#2 remove duplicate
str="lets google the pineapple"
str1=str.split(' ')
str2=[]
for i in str1:
    l=" "
    for j in i:
        if j in l:
            continue
        else:
            l=l+j
    str2.append(l)
print("".join(str2))

#or
str="lets google the pineapple"
str2=str.split(" ")
str3= " "
str4= " "
for i in str2:
    str3=dict.fromkeys(i,2)
    #print(str3)
    str5=" ".join(str3)
    str4=str4+str5+" "
print(str4)


#3

str1='/johnis @developer & musician!!'
str1=str1.replace('/','#').replace('@','#')
print(str1)

#4 reverse a list
list1=[100,200,300]
print(list1[::-1])

#5
list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list=["h","i","j"]
for i in sub_list:
    list1[2][1][2].append(i)
print(list1)
#or use extend


#6
str1='restart'
str2=str1[0]
for i in range(1,len(str1)):
    if str1[i]==str1[0]:
        str2=str2+"$"

    else:
        str2=str2+str1[i]
print(str2)
#or
str1='restart'
char=str1[0]
#length=len(str1)
str1=str1.replace(char,"$")
str1=char+str1[1:]
print(str1)


#7
list1=input("enter the sentence").split()
m=max(list1)
print(m)