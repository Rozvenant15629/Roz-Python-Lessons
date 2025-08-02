def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("enter a number: "))
if is_palindrome(n) and is_prime(n):
    print("YES")
else:
    print("NO")