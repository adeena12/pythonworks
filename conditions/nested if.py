"""a = 41
if a >10:
    print('above ten')
    if a > 50:
        print('above 50')
    else:
        print('not above 50')
else:
    print('invalid')"""

#largest using nested if
a,b,c=int(input("enter frst no")),int(input("enter second no")),int(input("enter third no"))
if a>b:
    if a>c:
        print("a is greater",a)
    else:
        print(c)
elif b>c:
    print(b)
else:
    print(c)
