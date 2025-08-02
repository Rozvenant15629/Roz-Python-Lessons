n = int(input("nhap so nguyen n: "))
tong = 0
for a in range(1, n + 1):
    if a % 2 != 0:
        tong = tong + a
print("tong la:", tong)