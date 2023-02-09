f=open("test1",'r')
#print(f.read())#read all in test
#or
for i in f:

    print(i)
f.close()

#print(f.read(8))#read no of character
#
# print(f.readline())#frst line reading
#
# print(f.readline())#second line reading

#append:used append new data at the end of a file
# f=open('test1','a')
# f.write('python is oop')
# f.close()
#
# f=open('test1','r')
# for i in f:
#     print(i)
#     f.close()
#
# f=open('test','w')
# f.write('python')
# f.close()

# f=open('test1','r')
# for i in f:
#     print(i)
# f.close()


#seek method sets current file postion in a file string.it also return the new pstion
#file.seekoffset value is required

# f=open('test1','r')
# f.seek(8)
# print(f.readline())
# f.close()

#tell():returns the current osition of the file
#fileobject.tell()
# f=open('test1','r')
# f.readline()
# pos=f.tell()
# f.close()
# print('position is' ,pos)

#write a prgrm line by line and set to list for this we use readlines
# def file_read(fna):
#     with open(fna) as f:
#         output_list=f.readlines()
#     print(output_list)
# file_read('test1')

# from shutil import copyfile9
# copyfile('test1','test2')
#
# str = 'cat rat mat cat pat rat cat sat cat sat'
# lst = str.split(' ')
# d = {}
# for i in lst:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# print(d)
""""
f=open('test2','r')
dic={}
for i in f:
    var=i.split(' ')
    for j in var:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
print(dic)"""
