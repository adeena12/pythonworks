#1 reverse a number
"""n=int(input('enter a number:'))
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("reverse number is",rev)

#3 anagram or not
str1=input("enter frst string")
str2=input("enter second string")
if(sorted(str1)==sorted(str2)):
    print("the strings are anagrams")
else:
    print("not anagrams")

#4palindrome or not
str=input("enter a string")
if str==str[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#5count frequency of characters
str=input("enter a string")
for i in str:
    f=str.count(i)
    print((i),f)

#8 find non repeating characters
str=input("enter a string")
for i in str:
    f=str.count(i)
    if f==1:
     print("non repeating character is:",(i))"""

#7 code to check two strings are same
str1="adeena"
str2="adeenasm"
for i in str1 and str2:
    if str1(i)!=str2(i):
        print("not match")
    else:
        print("match")



