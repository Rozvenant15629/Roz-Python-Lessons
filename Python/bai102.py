def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
def nguyen_to(i):
    dem = 0
    chuoi = str(i)
    for b in chuoi:
        if so_nguyen_to(int(b)):
            dem = dem + 1
    if dem == len(chuoi):
        print("YES")
    else:
        print("NO")
i = int(input("nhap so can kiem tra xem tat ca chu so trong so do co toan la so nguyen to khong: "))
nguyen_to(i)