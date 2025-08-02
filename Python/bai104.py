def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
def tong_nguyen_to(i):
    for b in range(1, i + 1):
        chuoi = str(b)
        tong = sum(int(c) for c in chuoi)
        if so_nguyen_to(tong):
            print(b, end=" ")
i = int(input("nhap so nguyen: "))
tong_nguyen_to(i)
    