import time
import threading

def csl_sqre(num):
    print("calculate the root of the given numbers")
    for n in num :
        time.sleep(0.3)
        print('Squre is :',n*n)
def cal_cube(num):
    print("calculate the cube of the given number ")
    for n in num:
        time.sleep(0.3)
        print("cube :",n*n*n)
arr=[6,7,5,3]
t1=time.time()
th1=threading.Thread(target=csl_sqre,args=(arr, ))
th2=threading.Thread(target=cal_cube,args=(arr, ))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by thread is :",time.time()-t1)
