print(list(map((lambda x: x * 2), range(1, 11))))
print([2 * x for x in range(1, 11)])
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
print([x for x in range(1, 11) if x % 2 != 0])
 
#genrate 50 values
#take  to the power of 2
#return multiples of 8

print([i ** 2 for i in range(50) if i % 8 == 0])
print([x * y for x in range(1, 4) for y in range(11, 13) ])

#list comprehensions inside list comprehensions
#generate a list of ten values
#multiply them by 2
#return multiples of 8
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])
