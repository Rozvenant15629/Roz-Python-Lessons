def so_nguyen_to(n):
    return n in [2, 3, 5, 7]
n = int(input("nhap so nguyen n: "))
for i in range(1, n + 1):
    s = str(i)
    if int(s[0]) in [2, 3, 5, 7] and int(s[-1]) in [2, 3, 5, 7]:
        print(i, end=" ")