def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
if a > b:
    a, b = b, a
ketqua = []
for c in range(a, b + 1):
    if so_nguyen_to(c):
        ketqua.append(c)
print("cac so nguyen to nam trong khoang la:", ketqua)