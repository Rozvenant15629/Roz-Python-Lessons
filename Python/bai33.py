n = int(input("nhap vao giatri n: "))
tong = 0
while n > 0:
    a = n % 10
    tong = tong + a
    n = n // 10
print("tong la:", tong)