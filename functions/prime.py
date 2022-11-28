def isPrime(num):
    for i in range(2, num):
        if (num % i ) == 0:
            return False
    return True

def getPrimes(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if isPrime(num1):
            list_of_primes.append(num1)
    return list_of_primes
max_num_for_prime = int(input("Enter the maximum number to search: "))
list_of_primes = getPrimes(max_num_for_prime)
for prime in list_of_primes:
    print(prime)