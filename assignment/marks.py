physics = int(input('enter physics mark'))
chemistry = int(input("enter chemistry mark"))
biology = int(input("enter biology mark"))
maths = int(input("enter maths mark"))
computer = int(input("enter computer mark"))
per = ((physics+chemistry+biology+maths+computer)*100/500)
print("your percentage : ",per,"%")
if per>100:
    print("invalid")
elif per<=100 and per>=90:
    print('A grade')
elif per>=80:
    print('B grade')
elif per>=70:
    print('C grade')
elif per>60:
    print('D grade')
elif per>50:
    print('E grade')
elif per>=40:
    print('F grade')
else:
    print('failed')