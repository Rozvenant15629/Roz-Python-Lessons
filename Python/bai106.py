def so_chinh_phuong(n):
    can = int(n ** 0.5)
    if can * can == n:
        return True
    else:
        return False
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    if so_chinh_phuong(i):
        print(i, end=" ")
