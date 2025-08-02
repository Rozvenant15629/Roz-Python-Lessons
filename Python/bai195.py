n = int(input("enter a number: "))
rev = 0
while n > 0:
    i = n % 10
    rev = (rev * 10) + i
    n = n // 10
if rev % 7 == 0:
    print("YES")
else:
    print("NO")
