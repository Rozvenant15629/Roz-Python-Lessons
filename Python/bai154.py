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
perfect_list = []
for a in range(1, n):
    if is_perfect(a):
        perfect_list.append(a)
if perfect_list:
    print("the list of perfect numbers less than", n, "are", perfect_list)
else:
    print("not found any perfect numbers less than", n)
