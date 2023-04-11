#like running multiple functions at a time
import threading
import time
import random
def executethread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%H: %M: %S", time.gmtime())))
    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

    print("Thread {} stops sleeping at {}".format(i, time.strftime("%H: %M: %S", time.gmtime())))

for i in range(10):
    thread = threading.Thread(target=executethread, args=(i, ))

    thread.start()

    print("Active Threads :", threading.activeCount())
    print("Thread Objects :", threading.enumerate())