from time import sleep

def task(sleep_time,message):
     #block for a moment
    sleep(sleep_time)
    #display a message
    print(message)
# task()

from threading import Thread

thread=Thread(target=task,args=(1.5,'New message from another thread'))
print("waiting for the thread....")
thread.start()
