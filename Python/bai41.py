n = int(input("nhap so nguyen n: "))
tong = 0
while n > 0:
    a = n % 10
    tong = tong + a
    n = n // 10
print("tong cac so trong so nguyen duong la:", tong)