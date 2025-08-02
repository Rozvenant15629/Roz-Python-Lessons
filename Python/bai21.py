n = int(input("nhap so n can kiem tra: "))
a = 1
tong = 0
while a < n:
    if a % 2 != 0:
        tong = tong + a
    a = a + 1
print("vay tong cac so le nho hon", n, "la:", tong)