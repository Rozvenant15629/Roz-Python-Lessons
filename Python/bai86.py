def so_nguyen_duong(n):
    tong = 0
    while n > 0:
        a = n % 10
        tong = tong + a
        n = n // 10
    return tong
n = int(input("nhap mot so nguyen duong can tinh tong: "))
print("tong la:", so_nguyen_duong(n))