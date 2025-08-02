def is_perfect(n):
    for a in range(1, n):
        if n % a == 0:
            return True
        else:
            return False
n = int(input("enter a number: "))
if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} isn't a perfect number")