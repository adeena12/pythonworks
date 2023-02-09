#recursion is calling a function multiple times itself

#find sum of natural no
def getsum(num):
    if num==1:
        return 1
    return num+getsum(num-1)
num=10
print(getsum(num))


#find factorial
def fact(no):
    if no==1:
        return 1
    else:
        return no*fact(no-1)
fact(5)#or no=5
print(fact(5))

#nth fibonacci no
def fibo(n):
    if n<0:
        print("incorrect")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(9))
