def so_nguyen_duong(n):
    dem = 0
    while n > 0:
        dem = dem +1
        n = n // 10
    return dem
n = int(input("nhap so nguyen duong can dem: "))
print("so chu so cua so nguyen duong do la:", so_nguyen_duong(n))