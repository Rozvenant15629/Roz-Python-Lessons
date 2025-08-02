def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total
n = int(input("enter a number: "))
divisors_list = []
for a in range(2, n):
    b = sum_of_divisors(a)
    if b > a and b < n and sum_of_divisors(b) == a:
        divisors_list.append((a, b))
if divisors_list:
    print("friendly numbers less than", n, "are", divisors_list)
else:
    print("not found friendly number less than", n)