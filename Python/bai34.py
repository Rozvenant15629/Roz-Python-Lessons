n = int(input("nhap n: "))
tong = 0
while n > 0:
    a = n % 10
    if a % 2 == 0:
        tong = tong + a
    n = n // 10
print("tong la:", tong)