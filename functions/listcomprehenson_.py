#list cmhns provide easyway to apply oprtns on a list.it creats a new list in wich each elmnt is the reslt of applying given oprtns on list
# syntax:list=[exprssn for item in list if condition
# #print([x for x in "helloworld"])


#
"""x=["ad,bg,mg"]
new=[x for a in x]
print(x)
#
prime=[x for x in range(2,21) if all(x%y!=0 for y in range(2,x))]
print(prime)

#
num=[y for y in range(100) if y%2==0 if y%5==0]
print(num)

#
letter_=[letter for letter in 'human']
print(letter_)

#
even=[x for x in range(10,50) if x%2==0]
print(even)
odd=[x for x in range(10,50) if x%2!=0]
print(odd)
sum_=[x for x in range(11)]
print(sum(sum_))
#or
print(sum([i for i in range(1,int(input("enter the no"))+1)]))
#or
print([(n*(n+1)/2) for n in range(1,int(input("enter no"))+1)])

l=[x+3 for x in [1,2,3]]
print(l)

l=[i for i in range(25) if i%2==0]
print(l)

l=[i for i in 'how are you' if i in ["a","e","i","o"]]
print(l)

str="hi how are you"
wrds=str.split( )
frstletter=[i[0] for i in wrds]
print(frstletter)"""

colors=["red","green","pink"]
x=[i for i in colors if "e" in i]
print(x)

colors=["red","green","pink"]
x=[i.upper() for i in colors]
print(x)

colors=["red","green","pink"]
x=["hello "for i in colors]
print(x)

colors=["red","green","pink"]
x=[i if i!="pink" else "blue" for i in colors]
print(x)

colors=["red","green","pink"]
x=["hello "for i in colors]
print(x)

words="hi how are u"
x={i:len(i) for i in words}
print(x)

