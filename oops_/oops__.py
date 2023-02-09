# oops:prgrm based on class and object
# class:way to bind functions
# object:run time entity of a class

#class
class emp:
    x=10
    def display(self):
        print("simple fnctn")
    def dis():
        print("without self")
    def sum(self,a,b):
        print("sum:",a+b)
obj=emp()
obj.display()
print(obj.x)
obj.sum(40,30)
ob=emp
ob.dis()

#
class emp:
    def read(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print("sum:",self.x+self.y)
    def pro(c):
        print("product:",c.x*c.y)
obj=emp()
obj.read(30,40)
obj.sum()
obj.pro()

#factorial
class emp:
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
obj=emp()
n=int(input("enter the no"))
f=obj.fact(n)
print("fact is:",f)

#or
class emp:
    def fact(self,x):
        if x==1:
            return 1
        else:
            return x*self.fact(x-1)
        #   return x*emp.fact(self,x-1)
obj=emp()
x=int(input("enter the value"))
f=obj.fact(n)
print("fact",f)