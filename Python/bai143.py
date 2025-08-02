def is_perfect(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    if sum(factors) == n:
        return True
    else:
        return False
n = int(input("enter a number: "))
if is_perfect(n):
    print(n, "is a perfect number")
else:
    print(n, "isn't a perfect number")
