def so_nguyen_duong(n):
    tong = 0
    while n > 0:
        a = n % 10
        if a % 2 == 0:
            tong = tong + a
        n = n // 10
    return tong
n = int(input("nhap mot so nguyen duong can tinh tong cac chu so chan: "))
print("tong cac chu so chan cua so nguyen duong do la:", so_nguyen_duong(n))