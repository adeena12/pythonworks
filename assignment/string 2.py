#1 check each word in a strng begins with cap
string1 = "Adeena Sherin"
print(string1.istitle())

#2 CHECK SUBSTRING IN A STRING
print('Adee' in string1)
print('gh' in string1)

#3
pos = string1.find("S")
print(pos)

#4 length of a string
print(len(string1))

#5 count the no of muliple character in a string
print(string1.count("n"))

#6 capitalize frst letter of a string
print(string1.capitalize())

#7 check if string is num
print(string1.isalnum())

#8 SPLIT A SRING
a = string1.split()
print(a)

#9 REVERSE A STRING
str= "hello world"
print(str[::-1])

#10 JOINT 2 STRING
str1 = "hello"
str2 = "adeena"
b = "".join([str1,str2])
print(b)

#11 STRING SLICING
print(string1[4:8])

#12 CONVERT NUMTO STRING
num = 89
print(type(num))
converted_num = format(num)
print(type(converted_num))

#13 replace all instance of substring in a string
strng = "hello adeena"
strng1 = strng.replace("hello adeena","hi adeena")
print(strng1)

#14 REMOVE SPACING
strng2 =" adeena sherin "
print(strng2.rstrip())
print(strng2.lstrip())
print(strng2.strip())

#15
#strings are immutable  so that programmer cannot alter the contents of the object.
# name = 'adeena'
# name [0] = 'm'









