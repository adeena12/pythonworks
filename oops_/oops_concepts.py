#oops concepts
#1)encapsulation: wrapping up of data and functions into a single unit.ex:class

#2)inheritance:acquire properties of one class to another class.advntg:code reusabilty
#types
#a)single inheritace:has one base class or parent class and derived or child class.b is derived frm a
#b)multilevelinheritance:one base class one intermediatory class and one derived class.a,b,c here b is intermediatry
#c)multiple inheritance: a child class c is derived from more than one baseclass a and b
#d)hierarchical inheritance:more than one class b,c,d is derived from one base class
#e)hybrid:combination of hierarchical and multiple

#3)POLYMORPHISM:one in many form.2types .1)run time(late/dynamic binding):fnctn over riding 2)compiletime polymorphism(early/static:fncn overloading
#fnctn overldng means one clsshv mr than one fnctn wih same fnctn name and diff signature(number,order,and type of parametrers
#over ridng is diff class have diff fnctn with same fnctn same signature

#4abstraction is to represent the essential features wthout representing explntn or background .advng:data hiding.abstrtact only contain declaration means no staement or definition
#abstract base classes abc is the builtin module

#a)single inheritance
""""
class A:
    def displayA(self):
        print("base class")
class B(A):
    def displayB(self):
        print("derived class")
obj=B()
obj.displayA()
obj.displayB()

#multilevel inheritance
class A:
    def read(self):
       self.x=int(input("enter no"))
       self.y=int(input("enter y"))
class B(A):
    def sum(self):
        self.s=self.x+self.y
        print("sum",self.x+self.y)
class C(B):
    def avg(self):
        print("avg",self.s/2)

obj=C()
obj.read()
obj.sum()
obj.avg()

#hierarchical
class A:
    def read(self):
       self.x=int(input("enter no"))
       self.y=int(input("enter y"))
       self.s = self.x + self.y
class B(A):
    def sum(self):
        print("sum",self.x+self.y)
class C(A):
    def avg(self):
        print("avg",self.s/2)
class D(A):
    def pro(self):
        print("pro",self.x*self.y)
ob1=B()
ob1.read()
ob1.sum()

ob2=C()
ob2.read()
ob2.avg()

ob3=D()
ob3.read()
ob3.pro()


#multiple inheritance
class A:
    def read(self):
       self.x=input("enter name")
       self.y=int(input("enter age"))

class B:
    def sum(self):
        self.n=int(input("enter salary"))
class C(A,B):
    def avg(self):
        print(self.x,self.y,self.n)
obj=C()
obj.read()
obj.sum()
obj.avg()

#3)plymorphism
#a overloading:python doesnt support
class A:
    def sum(self,a,b):
        print("sum",a+a)
    def sum(self,a,b):
        print("sum",a+b)
ob=A()
ob.sum(10,20)#only scnd fnctn wll work

#or:this mehod will wrk
class A:
    def display(self,name=None):
        if name is None:
            print("hello")
        else:
            print("hello"+name)
ob=A()
ob.display()
ob.display("anu")


#b overriding:diff class,same sig,run time
class rectangle:
    def Area(self,l,b):
        print("area of rectangle is",l+b)
class square:
    def Area(self,l,b):
        print("area of square is")
ob=square()
ob.Area(10,20)

#4 abstraction
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("non abstract ")
class triangle(polygon):
    def sides(self):
        print("triangle")
s=triangle()
s.display()
s.sides()"""

#constructor:cunsrct are  he member fnctns of a class which will automatically executed when an object of aclass is created
#do not hv return value we can define cnstrct by usng__init__.mainly 2 types cnstrctr,non parameterised cnstrct and parameterised cnstrctr
#non parametrised or default cnstrctr
class A:
    def __init__(self):
        print("non")
ob=A()
#PARAMETERISDE
class A:
    def __init__(self,NAME):
        print("parameterised")
        self.na=NAME
    def display(self):
        print(self.na)
ob=A("ADEENA")
ob.display()

#destructor(del)
class A:
    def __init__(self,NAME):
        print("parameterised")
        self.na=NAME
    #def __del__(self):
    #    print("distrooctr")

    def display(self):
        print(self.na)
ob=A("ADEENA")
del ob
ob.display()







