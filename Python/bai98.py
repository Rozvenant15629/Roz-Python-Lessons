def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
def nguyen_to(i):
    tong = 0
    chuoi = str(i)
    for b in chuoi:
        if so_nguyen_to(int(b)):
            tong = tong + int(b)
    return tong
i = int(input("nhap mot so nguyen duong: "))
print("tong cac so nguyen to nam trong so vua nhap la:", nguyen_to(i))

        