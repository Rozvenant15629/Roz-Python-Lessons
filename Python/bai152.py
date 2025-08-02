def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total
a = int(input("enter first number: "))
b = int(input("enter second number: "))
if sum_of_divisors(a) == b and sum_of_divisors(b) == a:
    print(f"{a} and {b} are friendly numbers!")
else:
    print(f"{a} and {b} are't friendly numbers!")