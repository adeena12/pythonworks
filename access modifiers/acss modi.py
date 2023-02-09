#to specify accebility,3 types
#public,protect,private
class A:
    var1= None#public data member

    _var2= None#proteced data member

    __var3= None#privatedata member

    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

    def displayPublicMembers(self):#public  member fnctn
        print("public datamember:",self.var1)#accessing public data member
    def _displayProtectedMembers(self):#protected membee fnctn
        print("protected datamember:", self._var2)  #accessing protected data member
    def __displayPrivateMembers(self):
        print("private datamember:", self.__var3)  # accesing private data member

    def accessPrivateMembers(self):
        self.__displayPrivateMembers()

#derivedclass
class B(A):

    #constructor
    def __init__(self,var1,var2,var3):
        A. __init__(self,var1,var2,var3)
    #public member fnctn
    def accessProtectedMembers(self):
        self._displayProtectedMembers()#accessing procted member fnctn of super class

#creating object of derived class
obj=B("pub_red","pro_white","pri_green")
#calling public member fnctn of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
print("object is accessing public members:",obj.var1)
print("object is accesing protected members:",obj._var2)
#obj cant access private member it will giveattribute error
print(obj._A__var3)#accessingname mangled variable
#name mangled
#a process in which any given identifier with one trailing nderscore and tw leading underscore
