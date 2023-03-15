#iterable-stored sequence of value-list of values and can act as object
#act as an object that produce objects one at a time

#iterator is different from iterables
#oject with a method __iter__ __next __ return the next value from a sequence of vvalues
sampstr = iter("Sample")
print("Char : ", next(sampstr))
print("Char : ", next(sampstr))
print("Char : ", next(sampstr))
print("Char : ", next(sampstr))
print("Char : ", next(sampstr))