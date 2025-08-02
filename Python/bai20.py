n = int(input("nhap so can dem: "))
dem = 0
while n > 0:
    n = n // 10
    dem = dem + 1
print("vay so chu so la:", dem)