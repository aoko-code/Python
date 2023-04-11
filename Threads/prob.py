import threading
import time
import random

class BankAccount(threading.Thread):
    accBalance = 100
    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)

        self.name = name
        self.moneyRequest = moneyRequest


    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()
    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw Ksh {} at {} ".format(customer.name, customer.moneyRequest, time.strftime("%H: %M: %S", time.gmtime())))

        if BankAccount.accBalance - customer.moneyRequest > 0:
            BankAccount.accBalance -= customer.moneyRequest
            print("New acc balance: KSH{}".format(BankAccount.accBalance))
        else:
            print("not enough money in account")
            print("Current balance: KSH{}".format(BankAccount.accBalance))
        time.sleep(3)

        

threadLock = threading.Lock()
doug = BankAccount("doug", 1)
paul = BankAccount("paul", 100)
sally = BankAccount("sally", 50)
doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()

print("Execution ends")