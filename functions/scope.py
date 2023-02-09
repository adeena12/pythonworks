#local and global functions
#1local
def myfunc():
  x = 300
  print(x)

myfunc()

#2global
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#3 non local
def programme():
    def python():
        name="adeena"

    def mean_stack():
        name="amree"

    def flutter():
        nonlocal name
        name="sdf"

    name= "asdf"
    flutter()#("we can get this as o/p bcs it's non locaal")
    #python()("dont get no non local so cant call")
    print(name)

programme()



