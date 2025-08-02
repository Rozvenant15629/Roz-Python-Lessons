def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
def nguyen_to(i):
    chuoi = str(i)
    print("cac chu so nguyen to trong", i, "la:", end=" ")
    for b in chuoi:
        if so_nguyen_to(int(b)):
            print(b, end=" ")
i = int(input("nhap so nguyen i: "))
nguyen_to(i)
