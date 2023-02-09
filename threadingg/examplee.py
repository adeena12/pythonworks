#from time import sleep
# def task():
#    sleep(3)
    # print("this is from anoher thread")
#
# task()

# from threading import Thread
# thread=Thread(target=task)
# thread.start()

#
from time import sleep
from threading import Thread

def task(sleep_time,message):
    sleep(sleep_time)
    print(message)
thread=Thread(target=task,args=(1.5,"new message from another thread"))
thread.start()
print("waiting for he thread...")
thread.join()