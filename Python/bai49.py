n = int(input("nhap so nguyen n: "))
tong = 0
while n > 0:
    a = n % 10
    tong = tong + a
    n = n // 10
print("tong cac chu so la:", tong)