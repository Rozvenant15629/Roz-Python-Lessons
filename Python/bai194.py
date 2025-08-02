def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
strings = input("enter a strings: ")
nums = list(map(int, strings.split()))
prime_list = 0
for a in nums:
    if is_prime(a):
        prime_list = prime_list + 1
print("Have", prime_list, "of prime number in string")