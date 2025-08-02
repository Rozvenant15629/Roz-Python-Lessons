def is_perfect(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    if sum(factors) == n:
        return True
    else:
        return False
a = int(input("enter a number: "))
b = int(input("enter a number: "))
if a > b:
    a, b = b, a
perfect_number = []
for c in range(a, b + 1):
    if is_perfect(c):
        perfect_number.append(c)
if perfect_number:
    print("the list of perfect numbers is:", perfect_number)
else:
    print("no perfect numbers found")