class Alphabet:
    
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
    #iterator method
    def __iter__(self):
        return self
    #next method
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index +=1
        return self.letters[self.index]
#custom object
alpha = Alphabet()
for letter in alpha:
    print(letter)
    