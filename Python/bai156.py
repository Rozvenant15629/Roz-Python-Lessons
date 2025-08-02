def is_perfect(n):
    total = []
    for i in range(1, n):
        if n % i == 0:
            total.append(i)
    if sum(total) == n:
        return True
    else:
        return False
n = int(input("enter a number: "))
if is_perfect(n):
    print(f"{n} is a perfect number!")
else:
    print(f"{n} isn't perfect number!")