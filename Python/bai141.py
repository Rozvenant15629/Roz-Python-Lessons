def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("enter a number: "))
primes = []
for a in range(1, n):
    if is_prime(a) and "5" not in str(a):
        primes.append(a)
print("the sum of prime numbers less than n is:", primes)