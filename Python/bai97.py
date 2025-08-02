def so_hoan_hao(n):
    tong = 0
    for a in range (1, n):
        if n % a == 0:
            tong = tong + a
    if tong == n:
        return True
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b :"))
if a > b:
    a, b = b, a
print("cac so hoan hao nam trong khoang tu", a, "den", b, "la:")
for i in range(a, b + 1):
    if so_hoan_hao(i):
        print(i, end=" ")