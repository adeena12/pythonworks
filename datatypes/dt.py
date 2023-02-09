#numbers
a=4
print(a)

#string
name = "adeena"
age = "12"
print(type(name))
print(type(age))

#sringindexing
str1 = "hello world"
print(str1[-2])

#string slicing
print(str1[-1:6:-1])
print(str1.isalpha())


#list ordered,indexed,list keyword,mutable
list[1,2,3]
print(type(list))

#dict orderd,allow duplicate,mutable,dict keyword,mutable
dict ={"age":12}
print(type(dict))


#tuple
a = ("adeena","amrin")
print(type(a))

#q)
# swaping
a,b=int(input("enter a no:")),int(input("second no:"))
a,b=b,a
print("a",a)
print("b",b)