try:
    n1=int(input("enter frst no:"))
    n2=int(input("enter scnd no:"))
    n3=n1/n2
    print("outputis : ", n3)
#if we dont knw where exception may occur
except Exception as ex:
    print(ex)
#if we knw where exception may occur
# except ZeroDivisionError as er:
#     print(er)
# except ValueError as er:
#     print(er)
