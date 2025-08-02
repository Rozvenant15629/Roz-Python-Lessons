def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = int(input("enter a number: "))
total = []
for a in range(1, n):
    if is_palindrome(a) and is_prime(a):
        total.append(a)
print("the list of palindrome and prime numbers less than", n, "is:", total)
print("the sum of that list is:", sum(total))