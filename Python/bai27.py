dem_am = 0
dem_duong = 0
dem_0 = 0
while True:
    n = int(input("nhap so nguyen n: "))
    if n == 999 or n == -999:
        break
    if n > 0:
        dem_duong = dem_duong + 1
    elif n < 0:
        dem_am = dem_am + 1
    else:
        dem_0 = dem_0 + 1
print("so so nguyen duong nguyen am va so 0 lan luot la:", dem_duong, dem_am, dem_0)