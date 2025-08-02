def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
def dem_nguyen_to(i):
    dem = 0
    chuoi = str(i)
    for b in chuoi:
        if so_nguyen_to(int(b)):
            dem = dem + 1
    return dem
i = int(input("nhap so nguyen i: "))
print("so chu so trong so", i, "la:", dem_nguyen_to(i))
