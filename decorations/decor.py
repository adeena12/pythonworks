#
"""def make_pretty(func):
    def inner():
        print("iaam pretty")
        func()
    return inner
@make_pretty
def ordinary():
    print("iam ordinary")
ordinary()

#
def calculator(fuc):
    def add():
        c=a+b
        print(c)

    def mul():
        c=a*b
        print(c)

@calculator
def div(a,b):
    print(a/b)


#
def smart_divide(func):
    def inner(c,d):
        print("am going to divide",c,"and",d)
        if d==0:
            print("whoops")
            return
        return func(c,d)
    return inner
@smart_divide
def div(a,b):
    print(a/b)

div(4,2)
div(0,0)"""

#
def upper_decor(fun):
    def wrapper(name):
        result=fun(name)
        return result.upper()
    return wrapper
@upper_decor
def nm(name):
    return"hello"+name
print(nm("arya"))
#or
def upper_decor(fun):
    def wrapper():
        result=fun()
        return result.upper()
    return wrapper()

def nm():
    return"hello"
f=upper_decor(nm)
print(f)






