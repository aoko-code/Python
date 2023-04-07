# return a result generator whenever called 
#return results one at a time unlike list comprehensions

def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
def gen_primes(max_num):
    for num1 in range(2, max_num):
        if isprime(num1):
            yield num1

prime = gen_primes(50)

print("prime : ", next(prime))
print("prime : ", next(prime))
print("prime : ", next(prime))
print("prime : ", next(prime))
print("prime : ", next(prime))
    