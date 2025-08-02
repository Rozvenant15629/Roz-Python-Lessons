def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
a = int(input("nhap so nguyen duong a: "))
b = int(input("nhap so nguyen duong b: "))
if a > b:
    a, b = b, a
ketqua = []
for i in range(a, b + 1):
    if so_nguyen_to(i):
        ketqua.append(i)
print("cac so nguyen to nam trong khoan la:", ketqua)
print("tong cac so nguyen to nam trong khoang la:", sum(ketqua))
print("so chu so nguyen to nam trong khoang la:", len(ketqua))