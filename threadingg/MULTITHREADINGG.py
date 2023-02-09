# import time
# import threading
#
# def cal_square(num):
#     print("calculate sqr root")
#     for n in num:
#         time.sleep(0.3)
#         print("square is:",n*n)
# def cal_cube(num):
#     print("calculate cube")
#     for n in num:
#         time.sleep(0.3)
#         print("cube is:",n*n*n)
# arr=[4,5,6,7,2]
#
# t1=time.time()
# th1=threading.Thread(target=cal_square,args=(arr,))
# th2=threading.Thread(target=cal_cube,args=(arr,))
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print("total ime s:",time.time()-t1)







import threading
def coder(number):
    print("coders:",number)
    return
threads=[]
for i in range(5):
    #creating threads
    t=threading.Thread(target=coder,args=(i,))
    threads.append(t)
    #starting threads
    t.start()
