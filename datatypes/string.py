#concatenation
str1 = "hello"

str2 = "4" #or str(str2)
new_str = str1+str2
print(new_str)
print(len(new_str))
#searching a string using find
fruit = "banana"
pos =fruit.find('b')
print(pos)
pos = fruit.find('z')
print(pos)

#replacing
greet ="hello adeena"
a = greet.replace("adeena","jane")
print(a)
b = greet.replace("a","h")
print(b)
#replc specific letter
print(greet.replace("l","j",1))

#string formating
name = "adeena"
age =23
print("%s is %d years old" %(name,age))#1
print("{} is {} years old".format(name,age))#2
print(f"{name} is {age} years old")#3

my_name= 'adeena'
bags= 5
apple_in_bags= 34
print(f'there are total of {bags*apple_in_bags}apple')