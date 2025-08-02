chuoi = input("nhap cac so nguyen: ")
so = list(map(int, chuoi.split()))
tong = 0
for a in so:
    if a % 5 == 0:
        tong = tong + a
print("tong cac so chia het cho 5 la:", tong)