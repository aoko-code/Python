class FibGenerator:
    #initialize 
    def __init__(self):
        self.first = 0
        self.second = 1
    
    #iterator
    def __iter__(self):
        return self
    
    #next
    def __next__(self):
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum

fibSeq = FibGenerator()
for i in range(10):
    print("Fib: ", next(fibSeq))