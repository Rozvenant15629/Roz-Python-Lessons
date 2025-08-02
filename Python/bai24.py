n = int(input("nhap so nguyen n: "))
a = 1
tong = 0
dem = 0
while a < n:
    if a % 2 == 0:
        tong = tong + a
        dem = dem + 1
    a = a + 1
print("tong va so so chan lan luot la:", tong, "va", dem)

