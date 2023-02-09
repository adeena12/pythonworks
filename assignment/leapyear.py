#1 leap year or not
year=int(input("enter the year"))
if (year%4==0) and (year%100!=0):
     print("leapyear")
elif (year%400==0) and (year%100==0):
    print(year,"is aleapyear")
else:
    print(year,"not a leapyear")

#2 vowel or consonant
letter=input("enter a letter")
vowels=['a','e','i','o','u','A','E','I','O','U']
#if letter in vowels:
    #print(letter,"is a vowels")
#else:
   # print(letter,"is consonant")