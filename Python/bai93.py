def so_amstrong(n):
    chuoi = str(n)
    so_chu_so = len(chuoi)
    tong = sum(int(a) ** so_chu_so for a in chuoi)
    if tong == n:
        return tong
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
for i in range(a, b + 1):
    if so_amstrong(i):
        print(i, end=" ")