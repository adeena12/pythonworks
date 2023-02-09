#regular expression :sequence of chrcter used tosearch patter.used to check if a strng contains specfied search patter.pythn has a builtin pattern re ,can be used to wrk with regulr expression.
#4 methods

#1)findall:return a list cntn all matches
import re
str="rose is a beautiful and colorful flower"
s=re.findall('ful',str)
print(s)

d='cat mat pat rat  sat'
a=re.findall('[scr]',d)#contain scr
print(a)

d='cat mat pat rat  sat'
a=re.findall('[^scr]',d)#except scr
print(a)

d='cat mat pat rat  sat 99988 998'
a=re.findall("\d{3}",d)
print(a)

d='cat mat pat rat  sat 99988 998'
a=re.findall("\d{1,3}",d)
print(a)

d='cat mat pat rat  sat 99988 9999 6666'
a=re.findall(r"\b\d{4}\b",d)
print(a)

#search(:it returns match object if threr is  a  mach anywhere on the string)
str='class will start at 10am'
s=re.search('\s',str)
print(s)
print(s.start())

s1=re.search('\d',str)
print(s1.start())

s2=re.search('python',str)
print(s2)

str='class will start at 10am'
s=re.search('^class.*10am$',str)
print(s)
if s:
    print('find')
else:
    print("not find")

#split()
strt='class will start at 10am'
s=re.split(" ",str)
print(s)

s1=re.split("a",str)
print(s1)

s2=re.split(' ',str,2)
print(s2)

#fullmatch()
str="python is a lang"
b=re.fullmatch(str,'python is a lang')
print(b)

#sub():replaces one or many wrds in strng
input="rose and jasmines are flowes"
g=re.sub(" ","*",input)
print(g)

g=re.sub(" ",'*',input,3)
print(g)