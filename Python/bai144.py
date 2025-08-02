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
perfect_numbers = []
for a in range(1, n):
    if is_perfect(a):
        perfect_numbers.append(a)
if perfect_numbers:    
    print("the list of perfect numbers less than", n, "is", perfect_numbers)
else:
    print("no perfect numbers found")
